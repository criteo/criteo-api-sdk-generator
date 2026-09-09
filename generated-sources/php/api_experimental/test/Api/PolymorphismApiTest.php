<?php
namespace criteo\api\api\experimental;

use criteo\api\api\experimental\Api\AnalyticsApi;
use criteo\api\api\experimental\Configuration;
use criteo\api\api\experimental\ApiException;
use criteo\api\api\experimental\Model\BaseTypeListRequest;
use criteo\api\api\experimental\Model\BaseTypeRequest;
use criteo\api\api\experimental\Model\BaseTypeResource;
use criteo\api\api\experimental\Model\DerivedTypeOne;
use criteo\api\api\experimental\Model\DerivedTypeOneRequest;
use criteo\api\api\experimental\Model\DerivedTypeOneResource;
use criteo\api\api\experimental\Model\DerivedTypeTwo;
use Jchook\AssertThrows\AssertThrows;
use PHPUnit\Framework\TestCase;

class PolymorphismApiTest extends TestCase
{
    use AssertThrows;

    // A valid bearer token has a short lifetime; fill it in here (single place) before running the success tests.
    private const VALID_TOKEN = "";

    private const TYPE_ONE_VALUE = "type-one";
    private const TYPE_TWO_VALUE = 42;
    private const COMMON_DATA_LENGTH = 12;

    private function apiWithToken(string $token): AnalyticsApi
    {
        $config = (new Configuration())->setAccessToken($token);
        // Client omitted: AnalyticsApi defaults it to a new GuzzleHttp\Client internally.
        return new AnalyticsApi(null, $config);
    }

    // commonData is a byte field, serialized as a base64 string.
    private function commonData(): string
    {
        return base64_encode(str_repeat("\0", self::COMMON_DATA_LENGTH));
    }

    // NOTE on typeDiscriminator: the generated model defaults it to the model name
    // ("DerivedTypeOne"), but the server expects the discriminator mapping value
    // ("derivedTypeOne"), so it is set explicitly (after construction, since the
    // BaseType constructor overwrites it with the model name).
    private function sampleDerivedTypeOne(): DerivedTypeOne
    {
        $attributes = new DerivedTypeOne([
            'type_one_value' => self::TYPE_ONE_VALUE,
            'common_data' => $this->commonData(),
        ]);
        $attributes->setTypeDiscriminator('derivedTypeOne');
        return $attributes;
    }

    private function sampleDerivedTypeTwo(): DerivedTypeTwo
    {
        $attributes = new DerivedTypeTwo([
            'type_two_value' => self::TYPE_TWO_VALUE,
            'common_data' => $this->commonData(),
        ]);
        $attributes->setTypeDiscriminator('derivedTypeTwo');
        return $attributes;
    }

    private function sampleInheritanceRequest(): DerivedTypeOneRequest
    {
        return new DerivedTypeOneRequest([
            'data' => new DerivedTypeOneResource([
                'type' => 'DerivedTypeOne',
                'attributes' => $this->sampleDerivedTypeOne(),
            ]),
        ]);
    }

    public function testPostInheritanceWithEmptyTokenShouldReturnUnauthorized()
    {
        $this->assertThrows(ApiException::class,
            function () {
                // Arrange
                $api = $this->apiWithToken("");

                // Act
                $api->postInheritanceWithHttpInfo($this->sampleInheritanceRequest());
            },
            function ($exception) {
                // Assert
                $this->assertEquals(401, $exception->getCode());
            }
        );
    }

    public function testPostInheritanceShouldSucceedWithValidToken()
    {
        // Arrange
        $api = $this->apiWithToken(self::VALID_TOKEN);

        // Act
        $response = $api->postInheritanceWithHttpInfo($this->sampleInheritanceRequest());

        // Assert
        $this->assertEquals(200, $response[1]);

        $attributes = $response[0]->getData()->getAttributes();
        $this->assertNotNull($attributes);
        $this->assertEquals(self::COMMON_DATA_LENGTH, strlen(base64_decode($attributes->getCommonData())));
        $this->assertEquals(self::TYPE_ONE_VALUE, $attributes->getTypeOneValue());
    }

    public function testPostPolymorphismWithDerivedTypeOneShouldSucceed()
    {
        // Arrange
        $api = $this->apiWithToken(self::VALID_TOKEN);
        $request = new BaseTypeRequest([
            'data' => new BaseTypeResource([
                'type' => 'DerivedTypeOne',
                'attributes' => $this->sampleDerivedTypeOne(),
            ]),
        ]);

        // Act
        $response = $api->postPolymorphismWithHttpInfo($request);

        // Assert
        $this->assertEquals(200, $response[1]);

        $attributes = $response[0]->getData()->getAttributes();
        $this->assertInstanceOf(DerivedTypeOne::class, $attributes);
        $this->assertEquals(self::COMMON_DATA_LENGTH, strlen(base64_decode($attributes->getCommonData())));
        $this->assertEquals(self::TYPE_ONE_VALUE, $attributes->getTypeOneValue());
    }

    public function testPostPolymorphismWithDerivedTypeTwoShouldSucceed()
    {
        // Arrange
        $api = $this->apiWithToken(self::VALID_TOKEN);
        $request = new BaseTypeRequest([
            'data' => new BaseTypeResource([
                'type' => 'DerivedTypeTwo',
                'attributes' => $this->sampleDerivedTypeTwo(),
            ]),
        ]);

        // Act
        $response = $api->postPolymorphismWithHttpInfo($request);

        // Assert
        $this->assertEquals(200, $response[1]);

        $attributes = $response[0]->getData()->getAttributes();
        $this->assertInstanceOf(DerivedTypeTwo::class, $attributes);
        $this->assertEquals(self::COMMON_DATA_LENGTH, strlen(base64_decode($attributes->getCommonData())));
        $this->assertEquals(self::TYPE_TWO_VALUE, $attributes->getTypeTwoValue());
    }

    public function testPostPolymorphicListWithDerivedTypesShouldSucceed()
    {
        // Arrange
        $api = $this->apiWithToken(self::VALID_TOKEN);
        $request = new BaseTypeListRequest([
            'data' => [
                new BaseTypeResource([
                    'type' => 'DerivedTypeOne',
                    'attributes' => $this->sampleDerivedTypeOne(),
                ]),
                new BaseTypeResource([
                    'type' => 'DerivedTypeTwo',
                    'attributes' => $this->sampleDerivedTypeTwo(),
                ]),
            ],
        ]);

        // Act
        $response = $api->postPolymorphicListWithHttpInfo($request);

        // Assert
        $this->assertEquals(200, $response[1]);

        $data = $response[0]->getData();
        $this->assertCount(2, $data);

        // First element should round-trip as DerivedTypeOne.
        $first = $data[0]->getAttributes();
        $this->assertInstanceOf(DerivedTypeOne::class, $first);
        $this->assertEquals(self::COMMON_DATA_LENGTH, strlen(base64_decode($first->getCommonData())));
        $this->assertEquals(self::TYPE_ONE_VALUE, $first->getTypeOneValue());

        // Second element should round-trip as DerivedTypeTwo.
        $second = $data[1]->getAttributes();
        $this->assertInstanceOf(DerivedTypeTwo::class, $second);
        $this->assertEquals(self::COMMON_DATA_LENGTH, strlen(base64_decode($second->getCommonData())));
        $this->assertEquals(self::TYPE_TWO_VALUE, $second->getTypeTwoValue());
    }
}
