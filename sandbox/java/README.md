## Steps

1. [Optional] Update package version in pom.xml
2. Update import in App.java
3. Run command `mvn clean install exec:java -D"exec.mainClass=com.criteo.app.App"`

## Tips

1. To get some examples, see API documentations (e.g. CatalogApi.md, AdvertiserApi.md, etc.)
2. To compile again the source, without having to install all the sources again, run `mvn compile`
3. To (re)install dependencies: `mvn install`
4. The command may slightly differ on IOS/Linux environment