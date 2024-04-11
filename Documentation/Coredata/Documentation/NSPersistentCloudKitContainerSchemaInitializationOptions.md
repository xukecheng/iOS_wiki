Type Property

# dryRun

A flag that indicates the container validates the model and generates the
records, but doesn’t upload them to CloudKit.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var dryRun: NSPersistentCloudKitContainerSchemaInitializationOptions { get }

## Discussion

This option is useful for unit testing to ensure your managed object model is
valid for use with CloudKit.

Type Property

# printSchema

Prints the generated records to the console.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var printSchema: NSPersistentCloudKitContainerSchemaInitializationOptions { get }

Initializer

# init(rawValue:)

Creates the schema initialization options using the specified raw value.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 11.0+

    
    
    init(rawValue: UInt)

##  Parameters

`rawValue`

    

The raw unsigned integer value.

