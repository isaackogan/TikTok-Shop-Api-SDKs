import org.jetbrains.kotlin.gradle.dsl.JvmTarget

plugins {
    kotlin("jvm") version "2.4.0"
    id("com.vanniktech.maven.publish") version "0.37.0"
}

group = "com.isaackogan"
version = "0.1.0"

repositories {
    mavenCentral()
}

dependencies {
    // The generated clients take an OkHttp Call.Factory and expose gson-annotated models, so both are API.
    api("com.squareup.okhttp3:okhttp:5.4.0")
    api("com.google.code.gson:gson:2.14.0")

    testImplementation(platform("org.junit:junit-bom:5.11.4"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testImplementation(kotlin("test"))
    testImplementation(kotlin("reflect"))
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
    testImplementation("com.squareup.okhttp3:mockwebserver3:5.4.0")
}

// JVM 11 bytecode and API. No JDK 11 is needed to build: -Xjdk-release limits the visible JDK API to Java 11's.
kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_11)
        freeCompilerArgs.add("-Xjdk-release=11")
    }
}

java {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}

// Maven Central publishing (release workflow: ./gradlew publishToMavenCentral). The plugin attaches the sources
// jar and an empty javadoc jar (Central requires one; Dokka over ~2,100 generated files is not worth it).
// Signing is only switched on when a key is supplied (ORG_GRADLE_PROJECT_signingInMemoryKey or a gradle
// property), so local builds, ./gradlew test and publishToMavenLocal need no keys.
mavenPublishing {
    publishToMavenCentral()
    if (providers.gradleProperty("signingInMemoryKey").isPresent) {
        signAllPublications()
    }
    coordinates("com.isaackogan", "tiktok-shop-api-kotlin", version.toString())
    pom {
        name.set("TikTok Shop API for Kotlin")
        description.set("Unofficial Kotlin and JVM client for the TikTok Shop API: signed requests, OAuth helper, typed webhook events.")
        url.set("https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin")
        licenses {
            license {
                name.set("MIT License")
                url.set("https://opensource.org/licenses/MIT")
            }
        }
        developers {
            developer {
                id.set("isaackogan")
                name.set("Isaac Kogan")
                url.set("https://github.com/isaackogan")
            }
        }
        scm {
            url.set("https://github.com/isaackogan/TikTok-Shop-Api-SDKs")
            connection.set("scm:git:https://github.com/isaackogan/TikTok-Shop-Api-SDKs.git")
            developerConnection.set("scm:git:ssh://git@github.com/isaackogan/TikTok-Shop-Api-SDKs.git")
        }
    }
}

tasks.test {
    useJUnitPlatform()
    testLogging {
        events("passed", "failed", "skipped")
        exceptionFormat = org.gradle.api.tasks.testing.logging.TestExceptionFormat.FULL
    }
}
