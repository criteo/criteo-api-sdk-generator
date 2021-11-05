package com.criteo.api.sdk.gradle.tasks

import org.openapitools.generator.gradle.plugin.tasks.GenerateTask
import org.gradle.api.tasks.TaskAction
import org.gradle.api.tasks.Input
import java.nio.file.Paths
import java.nio.file.Path
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import org.gradle.api.provider.Property

open class GenerateSdkTask : GenerateTask
{
    @Input
    val criteoPackage = project.properties["package.name"]

    constructor() : super()
    {
        inputSpec.ifSpecified { value ->
            configure(value)
            }
    }

    private fun <T : Any?> Property<T>.ifSpecified(block: Property<T>.(T) -> Unit) {
        if (isPresent) {
            val item: T? = get()
            if (item != null) {
                when (get()) {
                    is String -> if ((get() as String).isNotEmpty()) {
                        block(get())
                    }
                    is String? -> if (true == (get() as String?)?.isNotEmpty()) {
                        block(get())
                    }
                    else -> block(get())
                }
            }
        }
    }

    @TaskAction
    fun doGenerate() {
        val formattedDate : String = LocalDate.now().format(DateTimeFormatter.ofPattern("yyMMdd"))
//            def jsonFile = file(it.path);
////            def parsedJson = new groovy.json.JsonSlurper().parseText(jsonFile.text);
//
////            def parsedApiName = it.getName().replace(".json", "").toLowerCase(); 
////            def (criteoService, apiVersionFromName) = parsedApiName.tokenize('_');
////            def criteoApiVersion = apiVersionFromName.replace('-', '_');
//        
//            def clientOutputDirPerVersion = clientOutputDir + "/" + parsedApiName;
//            def specPath = it.path;
////            def packageBase =  criteoApiVersion; // com.criteo.api.marketingsolutions.v2021_10
////            if (packageBase.matches("[0-9].*"))
////                    packageBase= "v" + packageBase;
////            packageBase = "${criteoPackage}.${criteoService}.${packageBase}".toString();
//
//            def generateTask = task("openApiGenerate_java_" + parsedApiName, type: GenerateSdkTask.class) {
//                generatorName = "java"
//                templateDir = "$resourcesDir/templates/".toString()
//                inputSpec = specPath
//                outputDir = clientOutputDirPerVersion
//                removeOperationIdPrefix = true
//                generateApiTests = false
//                generateModelTests = false
//                configOptions = [
//                        groupId                  : 'com.criteo',
//                        apiPackage               : "${packageBase}.api".toString(), // com.criteo.api.marketingsolutions.v2021_10.api
//                        artifactId               : "criteo-api-${criteoService}-${technologyStack}".toString(), // criteo-api-marketingsolutions-sdk-java8
//                        artifactVersion          : "${criteoApiVersion}.${generatorVersion}.${getFormattedDate()}".toString(), // v2021_10. 
//                        apiVersion               : parsedJson.info.version,  // 2021-10
//                        artifactDescription      : "Java SDK for Criteo API ${criteoService} for ${criteoApiVersion} version".toString(),
//                        artifactUrl              : 'https://github.com/criteo/criteo-api-java-sdk',
//                        modelPackage             : "${packageBase}.model".toString(),
//                        scmConnection            : 'scm:git:git://github.com/criteo/criteo-api-java-sdk.git',
//                        scmDeveloperConnection   : 'scm:git:ssh://github.com:criteo/criteo-api-java-sdk.git',
//                        scmUrl                   : 'https://github.com/criteo/criteo-api-java-sdk',
//                        developerName            : 'Criteo',
//                        developerEmail           : 'open-source@criteo.com',
//                        developerOrganization    : 'Criteo',
//                        developerOrganizationUrl : 'https://www.criteo.com/',
//                        licenseName              : 'Apache License, version 2.0',
//                        licenseUrl               : 'https://www.apache.org/licenses/LICENSE-2.0.txt',
//                        hideGenerationTimestamp  : 'true',
//                        dateLibrary              : technologyStack.toString(),
//                ]
    }

    fun configure(swaggerFilePath : String)
    {
        val parsedApiName : String = Paths.get(swaggerFilePath,"").getFileName().toString().replace(".json", "").toLowerCase();
        val (criteoService : String, apiVersionFromName : String )= parsedApiName.split('_'); // ex: ("marketingsolutions", "2021-10")
        val criteoApiVersion = apiVersionFromName.replace('-', '_');
        var packageBase =  criteoApiVersion; 
        if (packageBase.matches("[0-9].*".toRegex()))
                packageBase= "v" + packageBase;
        packageBase = criteoPackage.toString() + "." + criteoService + "." + packageBase // ex: "com.criteo.api.marketingsolutions.v2021_10""

        configOptions.put("apiPackage","brbi")
//        configOptions[apiPackage] = packageBase +".api" // ex: "com.criteo.api.marketingsolutions.v2021_10.api"
//        configOptions[artifactId] = "criteo-api-" + criteoService + "- " + technologyStack
    }
}