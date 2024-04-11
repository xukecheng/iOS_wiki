Initializer

# init(from:forSourceModel:destinationModel:)

Returns the mapping model that will translate data from the source to the
destination model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init?(
        from bundles: [Bundle]?,
        forSourceModel sourceModel: NSManagedObjectModel?,
        destinationModel: NSManagedObjectModel?
    )

##  Parameters

`bundles`

    

An array of bundles in which to search for mapping models.

`sourceModel`

    

The managed object model for the source store.

`destinationModel`

    

The managed object model for the destination store.

## Return Value

Returns the mapping model to translate data from `sourceModel` to
`destinationModel`. If a suitable mapping model cannot be found, returns
`nil`.

## Discussion

This method is a companion to the `mergedModel(from:)` and
`mergedModel(from:forStoreMetadata:)` methods. In this case, the framework
uses the version information from the models to locate the appropriate mapping
model in the available bundles.

## See Also

### Creating a Mapping

`class func inferredMappingModel(forSourceModel: NSManagedObjectModel,
destinationModel: NSManagedObjectModel) -> NSMappingModel`

Returns a newly created mapping model that will migrate data from the source
to the destination model.

`init?(contentsOf: URL?)`

Returns a mapping model initialized from a given URL.

### Related Documentation

Core Data Model Versioning and Data Migration Programming Guide

Type Method

# inferredMappingModel(forSourceModel:destinationModel:)

Returns a newly created mapping model that will migrate data from the source
to the destination model.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func inferredMappingModel(
        forSourceModel sourceModel: NSManagedObjectModel,
        destinationModel: NSManagedObjectModel
    ) throws -> NSMappingModel

##  Parameters

`source`

    

The source managed object model.

`destination`

    

The destination managed object model.

`error`

    

If a problem occurs, on return contains an `NSInferredMappingModelError` error
that describes the problem.

The error’s user info will contain additional details about why inferring the
mapping model failed (check for the following keys: `reason`, `entity`,
`property`.

## Return Value

A newly-created mapping model to migrate data from the source to the
destination model. If the mapping model can not be created, returns `nil`.

## Discussion

A model will be created only if all changes are simple enough to be able to
reasonably infer a mapping (for example, removing or renaming an attribute,
adding an optional attribute or relationship, or adding renaming or deleting
an entity). Element IDs are used to track renamed properties and entities.

Handling Errors in Swift:

In Swift, this method returns a nonoptional result and is marked with the
`throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Creating a Mapping

`init?(from: [Bundle]?, forSourceModel: NSManagedObjectModel?,
destinationModel: NSManagedObjectModel?)`

Returns the mapping model that will translate data from the source to the
destination model.

`init?(contentsOf: URL?)`

Returns a mapping model initialized from a given URL.

Initializer

# init(contentsOf:)

Returns a mapping model initialized from a given URL.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init?(contentsOf url: URL?)

##  Parameters

`url`

    

The location of an archived mapping model.

## Return Value

A mapping model initialized from `url`.

## See Also

### Creating a Mapping

`init?(from: [Bundle]?, forSourceModel: NSManagedObjectModel?,
destinationModel: NSManagedObjectModel?)`

Returns the mapping model that will translate data from the source to the
destination model.

`class func inferredMappingModel(forSourceModel: NSManagedObjectModel,
destinationModel: NSManagedObjectModel) -> NSMappingModel`

Returns a newly created mapping model that will migrate data from the source
to the destination model.

Instance Property

# entityMappings

The entity mappings for the mapping model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entityMappings: [NSEntityMapping]! { get set }

## Discussion

The order of the mappings in the array determines the order in which they will
be processed during migration.

## See Also

### Managing Entity Mappings

`var entityMappingsByName: [String : NSEntityMapping]`

The entity mappings for the mapping model, keyed by name.

Instance Property

# entityMappingsByName

The entity mappings for the mapping model, keyed by name.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entityMappingsByName: [String : NSEntityMapping] { get }

## See Also

### Managing Entity Mappings

`var entityMappings: [NSEntityMapping]!`

The entity mappings for the mapping model.

