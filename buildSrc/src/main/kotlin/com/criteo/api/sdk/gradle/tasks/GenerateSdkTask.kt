package com.criteo.api.sdk.gradle.tasks

import groovy.lang.Closure
import java.nio.file.Paths
import java.nio.file.Path
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import org.gradle.api.provider.Property
import org.gradle.api.Task
import org.gradle.api.tasks.Input
import org.gradle.api.tasks.Optional
import org.gradle.api.tasks.TaskAction
import org.gradle.kotlin.dsl.property
import org.openapitools.generator.gradle.plugin.tasks.GenerateTask

open class GenerateSdkTask : GenerateTask()
{
    @Input
    val criteoPackage = project.properties["package.name.base"]

    @Input
    val generatorVersion = project.properties["generator.version"]

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

    override fun configure(closure : Closure<*>) : Task {
        val task = super.configure(closure)
        computeGeneratorOptions()
        return task;
    }

    open protected fun computeGeneratorOptions()
    {

        val swaggerFilePath = inputSpec.get()
        val technologyStack = configOptions.get()["technologyStack"].toString()
        val language = technologyStack.replace("[^a-zA-Z]".toRegex(),"").toLowerCase()

        val parsedApiName = Paths.get(swaggerFilePath,"").getFileName().toString().replace(".json", "").toLowerCase();
        val (criteoService : String, apiVersionFromName : String )= parsedApiName.split('_'); // ex: ("marketingsolutions", "2021-10")
        val criteoApiVersion = apiVersionFromName.replace('-', '_');

        var groupId = "criteo"
        var packageBase =  criteoApiVersion; 
        if (packageBase.matches("[0-9].*".toRegex()))
            packageBase= "v" + packageBase;
        

        packageBase = "${criteoPackage}.${criteoService}.${packageBase}".replace('.', nameSeparator(language)) // ex: "com.criteo.api.marketingsolutions.v2021_10""
        when (language) {
            "java" -> {
                packageBase = "com." + packageBase
                groupId = "com." + groupId
            }
        }
        val packageVersion = "${criteoApiVersion}.${generatorVersion}.${formattedDate()}"; // example : 2021_10.1.211110

        generatorName.set(language)
        removeOperationIdPrefix.set(true)
        generateApiTests.set(false)
        generateModelTests.set(false)
        gitUserId.set("criteo")
        gitRepoId.set("criteo-api-${language}-sdk")
        configOptions.put("groupId"                  , groupId)
        configOptions.put("invokerPackage"           , "${packageBase}")
        configOptions.put("artifactId"               , "criteo-api-${criteoService}-sdk-${technologyStack}")
        configOptions.put("packageName"              , "criteo-api-${criteoService}-sdk-${technologyStack}")
        configOptions.put("packageVersion"           , "${packageVersion}")
        configOptions.put("artifactDescription"      , "${language.toUpperCase()} SDK for Criteo API ${criteoService} for ${criteoApiVersion} version")
        configOptions.put("Description"              , "${language.toUpperCase()} SDK for Criteo API ${criteoService} for ${criteoApiVersion} version")
        configOptions.put("packageUrl"               , "https://github.com/criteo/criteo-api-${language}-sdk")
        configOptions.put("artifactUrl"              , "https://github.com/criteo/criteo-api-${language}-sdk")
        configOptions.put("scmConnection"            , "scm:git:git://github.com/criteo/criteo-api-${technologyStack}-sdk.git")
        configOptions.put("scmDeveloperConnection"   , "scm:git:ssh://github.com:criteo/criteo-api-${technologyStack}-sdk.git")
        configOptions.put("scmUrl"                   , "https://github.com/criteo/criteo-api-${language}-sdk")
        configOptions.put("developerName"            , "Criteo")
        configOptions.put("developerEmail"           , "open-source@criteo.com")
        configOptions.put("developerOrganization"    , "Criteo")
        configOptions.put("developerOrganizationUrl" , "https://www.criteo.com/")
        configOptions.put("licenseName"              , "Apache License, version 2.0")
        configOptions.put("licenseUrl"               , "https://www.apache.org/licenses/LICENSE-2.0.txt")
        configOptions.put("hideGenerationTimestamp"  , "true")
        configOptions.put("dateLibrary"              , technologyStack)
        configOptions.put("version"                  , "1.0.0") // OpenAPI-Generator version
        when (language) {
            "java" -> {
                configOptions.put("artifactVersion"  , "${packageVersion}")
                configOptions.put("modelPackage"     , "${packageBase}.model")
                configOptions.put("apiPackage"       , "${packageBase}.api")
            }
            "python" -> {
                configOptions.put("packageName"      , "${packageBase}")
            }
        }
    }

    open fun formattedDate() : String {
        val date = LocalDate.now()
        return date.format(DateTimeFormatter.ofPattern("yyMMdd"))
    }

    open fun nameSeparator(language : String) : Char {
        when (language) {
            "php" -> return '\\'
            "python" -> return '_'
            else -> return '.'
        }
    }

}