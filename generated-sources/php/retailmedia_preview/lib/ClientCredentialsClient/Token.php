<?php
namespace criteo\api\retailmedia\preview\ClientCredentialsClient;

use DateTime;

class Token
{
    /**
     * @var DateTime
     */
    private $expiresOn;
    private $value;

    public function __construct($value, $expiresIn)
    {
        $this->expiresOn = $this->computeExpiresOn($expiresIn);
        $this->value = $value;
    }

    public function getValue(): string
    {
        return $this->value;
    }

    public function computeExpiresOn($expiresIn): DateTime
    {
        $now = new DateTime();
        return $now->modify('+' . $expiresIn . ' second');
    }

    public function isValidEnough(): bool
    {
        $now = new DateTime();
        return $this->expiresOn > $now->modify('+15 second');
    }
}
