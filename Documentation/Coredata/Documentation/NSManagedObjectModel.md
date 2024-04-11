Initializer

# init(contentsOf:)

Initializes the managed object model using the model file at the specified
URL.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    convenience init?(contentsOf url: URL)

##  Parameters

`url`

    

An URL object specifying the location of a model file.

## Return Value

A managed object model initialized using the file at `url`.

## See Also

### Creating a managed object model

`init()`

Initializes an empty managed object model.

`class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?`

Returns a model created by merging all the models found in given bundles.

`class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) ->
NSManagedObjectModel?`

Returns a merged model from a specified array for the version information in
provided metadata.

`init?(byMerging: [NSManagedObjectModel]?)`

Creates a single model from an array of existing models.

`init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])`

Returns, for the version information in given metadata, a model merged from a
given array of models.

### Related Documentation

Core Data Programming Guide

Core Data Model Versioning and Data Migration Programming Guide

Initializer

# init()

Initializes an empty managed object model.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating a managed object model

`init?(contentsOf: URL)`

Initializes the managed object model using the model file at the specified
URL.

`class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?`

Returns a model created by merging all the models found in given bundles.

`class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) ->
NSManagedObjectModel?`

Returns a merged model from a specified array for the version information in
provided metadata.

`init?(byMerging: [NSManagedObjectModel]?)`

Creates a single model from an array of existing models.

`init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])`

Returns, for the version information in given metadata, a model merged from a
given array of models.

Type Method

# mergedModel(from:)

Returns a model created by merging all the models found in given bundles.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func mergedModel(from bundles: [Bundle]?) -> NSManagedObjectModel?

##  Parameters

`bundles`

    

An array of instances of `NSBundle` to search. If you specify `nil`, then the
main bundle is searched.

## Return Value

A model created by merging all the models found in `bundles`.

## See Also

### Creating a managed object model

`init?(contentsOf: URL)`

Initializes the managed object model using the model file at the specified
URL.

`init()`

Initializes an empty managed object model.

`class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) ->
NSManagedObjectModel?`

Returns a merged model from a specified array for the version information in
provided metadata.

`init?(byMerging: [NSManagedObjectModel]?)`

Creates a single model from an array of existing models.

`init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])`

Returns, for the version information in given metadata, a model merged from a
given array of models.

Type Method

# mergedModel(from:forStoreMetadata:)

Returns a merged model from a specified array for the version information in
provided metadata.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func mergedModel(
        from bundles: [Bundle]?,
        forStoreMetadata metadata: [String : Any]
    ) -> NSManagedObjectModel?

##  Parameters

`bundles`

    

An array of bundles.

`metadata`

    

A dictionary containing version information from the metadata for a persistent
store.

## Return Value

The managed object model used to create the store for the metadata. If a model
cannot be created to match the version information specified by `metadata`,
returns `nil`.

## Discussion

This method is a companion to `mergedModel(from:)`.

## See Also

### Creating a managed object model

`init?(contentsOf: URL)`

Initializes the managed object model using the model file at the specified
URL.

`init()`

Initializes an empty managed object model.

`class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?`

Returns a model created by merging all the models found in given bundles.

`init?(byMerging: [NSManagedObjectModel]?)`

Creates a single model from an array of existing models.

`init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])`

Returns, for the version information in given metadata, a model merged from a
given array of models.

Initializer

# init(byMerging:)

Creates a single model from an array of existing models.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init?(byMerging models: [NSManagedObjectModel]?)

##  Parameters

`models`

    

An array of instances of `NSManagedObjectModel`.

## Return Value

A single model made by combining the models in `models`.

## Discussion

You use this method to combine multiple models (typically from different
frameworks) into one.

## See Also

### Creating a managed object model

`init?(contentsOf: URL)`

Initializes the managed object model using the model file at the specified
URL.

`init()`

Initializes an empty managed object model.

`class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?`

Returns a model created by merging all the models found in given bundles.

`class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) ->
NSManagedObjectModel?`

Returns a merged model from a specified array for the version information in
provided metadata.

`init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])`

Returns, for the version information in given metadata, a model merged from a
given array of models.

Initializer

# init(byMerging:forStoreMetadata:)

Returns, for the version information in given metadata, a model merged from a
given array of models.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init?(
        byMerging models: [NSManagedObjectModel],
        forStoreMetadata metadata: [String : Any]
    )

##  Parameters

`models`

    

An array of instances of `NSManagedObjectModel`.

`metadata`

    

A dictionary containing version information from the metadata for a persistent
store.

## Return Value

A merged model from `models` for the version information in `metadata`. If a
model cannot be created to match the version information in `metadata`,
returns `nil`.

## Discussion

This is the companion method to `mergedModel(from:forStoreMetadata:)`.

## See Also

### Creating a managed object model

`init?(contentsOf: URL)`

Initializes the managed object model using the model file at the specified
URL.

`init()`

Initializes an empty managed object model.

`class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?`

Returns a model created by merging all the models found in given bundles.

`class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) ->
NSManagedObjectModel?`

Returns a merged model from a specified array for the version information in
provided metadata.

`init?(byMerging: [NSManagedObjectModel]?)`

Creates a single model from an array of existing models.

Instance Property

# entities

The entities in the model.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entities: [NSEntityDescription] { get set }

## Discussion

Entities are instances of `NSEntityDescription`.

### Special Considerations

Setting the entities for an object model raises an exception if the object
model has been used by an object graph manager.

## See Also

### Managing entities and configurations

`var entitiesByName: [String : NSEntityDescription]`

The entities of the model, keyed by name.

`var configurations: [String]`

All the available configuration names of the model.

`func entities(forConfigurationName: String?) -> [NSEntityDescription]?`

Returns the entities of the model for a specified configuration.

`func setEntities([NSEntityDescription], forConfigurationName: String)`

Associates the specified entities with the model using the given configuration
name.

Instance Property

# entitiesByName

The entities of the model, keyed by name.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entitiesByName: [String : NSEntityDescription] { get }

## Discussion

Entities are instances of `NSEntityDescription`.

## See Also

### Managing entities and configurations

`var entities: [NSEntityDescription]`

The entities in the model.

`var configurations: [String]`

All the available configuration names of the model.

`func entities(forConfigurationName: String?) -> [NSEntityDescription]?`

Returns the entities of the model for a specified configuration.

`func setEntities([NSEntityDescription], forConfigurationName: String)`

Associates the specified entities with the model using the given configuration
name.

### Related Documentation

`class func entity(forEntityName: String, in: NSManagedObjectContext) ->
NSEntityDescription?`

Returns the entity with the specified name from the managed object model
associated with the specified managed object context’s persistent store
coordinator.

Instance Property

# configurations

All the available configuration names of the model.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var configurations: [String] { get }

## See Also

### Managing entities and configurations

`var entities: [NSEntityDescription]`

The entities in the model.

`var entitiesByName: [String : NSEntityDescription]`

The entities of the model, keyed by name.

`func entities(forConfigurationName: String?) -> [NSEntityDescription]?`

Returns the entities of the model for a specified configuration.

`func setEntities([NSEntityDescription], forConfigurationName: String)`

Associates the specified entities with the model using the given configuration
name.

Instance Method

# entities(forConfigurationName:)

Returns the entities of the model for a specified configuration.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func entities(forConfigurationName configuration: String?) -> [NSEntityDescription]?

##  Parameters

`configuration`

    

The name of a configuration in the receiver.

## Return Value

An array containing the entities of the receiver for the configuration
specified by `configuration`.

## See Also

### Managing entities and configurations

`var entities: [NSEntityDescription]`

The entities in the model.

`var entitiesByName: [String : NSEntityDescription]`

The entities of the model, keyed by name.

`var configurations: [String]`

All the available configuration names of the model.

`func setEntities([NSEntityDescription], forConfigurationName: String)`

Associates the specified entities with the model using the given configuration
name.

Instance Method

# setEntities(_:forConfigurationName:)

Associates the specified entities with the model using the given configuration
name.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setEntities(
        _ entities: [NSEntityDescription],
        forConfigurationName configuration: String
    )

##  Parameters

`entities`

    

An array of instances of `NSEntityDescription`.

`configuration`

    

A name for the configuration.

## Discussion

This method raises an exception if the receiver has been used by an object
graph manager.

## See Also

### Managing entities and configurations

`var entities: [NSEntityDescription]`

The entities in the model.

`var entitiesByName: [String : NSEntityDescription]`

The entities of the model, keyed by name.

`var configurations: [String]`

All the available configuration names of the model.

`func entities(forConfigurationName: String?) -> [NSEntityDescription]?`

Returns the entities of the model for a specified configuration.

Instance Property

# fetchRequestTemplatesByName

A dictionary of the receiver’s fetch request templates, keyed by name.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>] { get }

## Discussion

If the template contains a predicate with substitution variables, you should
instead use `fetchRequestFromTemplate(withName:substitutionVariables:)` to
create a new fetch request.

## See Also

### Manipulating fetch request templates

`func fetchRequestTemplate(forName: String) -> NSFetchRequest<any
NSFetchRequestResult>?`

Returns the fetch request with a specified name.

`func fetchRequestFromTemplate(withName: String, substitutionVariables:
[String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?`

Returns a copy of the fetch request template with the variables substituted by
values from the substitutions dictionary.

`func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?,
forName: String)`

Associates the specified fetch request with the receiver using the given name.

Instance Method

# fetchRequestTemplate(forName:)

Returns the fetch request with a specified name.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func fetchRequestTemplate(forName name: String) -> NSFetchRequest<any NSFetchRequestResult>?

##  Parameters

`name`

    

A string containing the name of a fetch request template.

## Return Value

The fetch request named `name`.

## Discussion

If the template contains substitution variables, you should instead use
`fetchRequestFromTemplate(withName:substitutionVariables:)` to create a new
fetch request.

## See Also

### Manipulating fetch request templates

`var fetchRequestTemplatesByName: [String : NSFetchRequest<any
NSFetchRequestResult>]`

A dictionary of the receiver’s fetch request templates, keyed by name.

`func fetchRequestFromTemplate(withName: String, substitutionVariables:
[String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?`

Returns a copy of the fetch request template with the variables substituted by
values from the substitutions dictionary.

`func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?,
forName: String)`

Associates the specified fetch request with the receiver using the given name.

Instance Method

# fetchRequestFromTemplate(withName:substitutionVariables:)

Returns a copy of the fetch request template with the variables substituted by
values from the substitutions dictionary.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func fetchRequestFromTemplate(
        withName name: String,
        substitutionVariables variables: [String : Any]
    ) -> NSFetchRequest<any NSFetchRequestResult>?

##  Parameters

`name`

    

A string containing the name of a fetch request template.

`variables`

    

A dictionary containing key-value pairs where the keys are the names of
variables specified in the template; the corresponding values are substituted
before the fetch request is returned. The dictionary must provide values for
all the variables in the template.

## Return Value

A copy of the fetch request template with the variables substituted by values
from `variables`.

## Discussion

The `variables` dictionary must provide values for all the variables. If you
want to test for a nil value, use `[NSNull null]`.

This method provides the usual way to bind an “abstractly” defined fetch
request template to a concrete fetch. For more details on using this method,
see Creating Predicates.

## See Also

### Manipulating fetch request templates

`var fetchRequestTemplatesByName: [String : NSFetchRequest<any
NSFetchRequestResult>]`

A dictionary of the receiver’s fetch request templates, keyed by name.

`func fetchRequestTemplate(forName: String) -> NSFetchRequest<any
NSFetchRequestResult>?`

Returns the fetch request with a specified name.

`func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?,
forName: String)`

Associates the specified fetch request with the receiver using the given name.

Instance Method

# setFetchRequestTemplate(_:forName:)

Associates the specified fetch request with the receiver using the given name.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setFetchRequestTemplate(
        _ fetchRequestTemplate: NSFetchRequest<any NSFetchRequestResult>?,
        forName name: String
    )

##  Parameters

`fetchRequest`

    

A fetch request, typically containing predicates with variables for
substitution.

`name`

    

A string that specifies the name of the fetch request template.

## Discussion

For more details on using this method, see Creating Predicates.

### Special Considerations

This method raises an exception if the receiver has been used by an object
graph manager.

## See Also

### Manipulating fetch request templates

`var fetchRequestTemplatesByName: [String : NSFetchRequest<any
NSFetchRequestResult>]`

A dictionary of the receiver’s fetch request templates, keyed by name.

`func fetchRequestTemplate(forName: String) -> NSFetchRequest<any
NSFetchRequestResult>?`

Returns the fetch request with a specified name.

`func fetchRequestFromTemplate(withName: String, substitutionVariables:
[String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?`

Returns a copy of the fetch request template with the variables substituted by
values from the substitutions dictionary.

Instance Property

# localizationDictionary

The localization dictionary of the model.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var localizationDictionary: [String : String]? { get set }

## Discussion

Table 1 describes the key and value pattern for the localization dictionary.

**Table 1**  Key and value pattern for the localization dictionary.Key| Value|
Note  
---|---|---  
"Entity/NonLocalizedEntityName"| "LocalizedEntityName"|  
"Property/NonLocalizedPropertyName/Entity/EntityName"|
"LocalizedPropertyName"| (1)  
"Property/NonLocalizedPropertyName"| "LocalizedPropertyName"|  
"ErrorString/NonLocalizedErrorString"| "LocalizedErrorString"|  
  
(1) For properties in different entities with the same non-localized name but
that should have different localized names.

### Special Considerations

In OS X v10.4, `localizationDictionary` may return `nil` until Core Data
lazily loads the dictionary for its own purposes (for example, reporting a
localized error).

Instance Property

# versionChecksum

The Base64-encoded 128-bit model version hash.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var versionChecksum: String { get }

## Discussion

This value is also available in the versioned model’s `VersionInfo.plist` file
and in Xcode’s build log.

## See Also

### Versioning and migrating entities

`var versionIdentifiers: Set<AnyHashable>`

The set of developer-defined version identifiers for the object model.

`var entityVersionHashesByName: [String : Data]`

The dictionary of the model’s entity names and their corresponding version
hashes.

`func isConfiguration(withName: String?, compatibleWithStoreMetadata: [String
: Any]) -> Bool`

Returns a Boolean value that indicates whether a given configuration in the
model is compatible with given metadata from a persistent store.

Instance Property

# versionIdentifiers

The set of developer-defined version identifiers for the object model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionIdentifiers: Set<AnyHashable> { get set }

## Discussion

Merged models return the combined collection of identifiers. The Core Data
framework does not assign a default identifier to object models, nor does it
depend on this value at runtime. For models you create in Xcode, set this
value in the model inspector.

Use this value when debugging to help determine the models that Core Data
merges to create the merged model.

## See Also

### Versioning and migrating entities

`var versionChecksum: String`

The Base64-encoded 128-bit model version hash.

`var entityVersionHashesByName: [String : Data]`

The dictionary of the model’s entity names and their corresponding version
hashes.

`func isConfiguration(withName: String?, compatibleWithStoreMetadata: [String
: Any]) -> Bool`

Returns a Boolean value that indicates whether a given configuration in the
model is compatible with given metadata from a persistent store.

Instance Property

# entityVersionHashesByName

The dictionary of the model’s entity names and their corresponding version
hashes.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entityVersionHashesByName: [String : Data] { get }

## Discussion

Core Data use the dictionary of version hash information is to determine
schema compatibility.

## See Also

### Versioning and migrating entities

`var versionChecksum: String`

The Base64-encoded 128-bit model version hash.

`var versionIdentifiers: Set<AnyHashable>`

The set of developer-defined version identifiers for the object model.

`func isConfiguration(withName: String?, compatibleWithStoreMetadata: [String
: Any]) -> Bool`

Returns a Boolean value that indicates whether a given configuration in the
model is compatible with given metadata from a persistent store.

Instance Method

# isConfiguration(withName:compatibleWithStoreMetadata:)

Returns a Boolean value that indicates whether a given configuration in the
model is compatible with given metadata from a persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func isConfiguration(
        withName configuration: String?,
        compatibleWithStoreMetadata metadata: [String : Any]
    ) -> Bool

##  Parameters

`configuration`

    

The name of a configuration in the receiver. Pass `nil` to specify no
configuration.

`metadata`

    

Metadata for a persistent store.

## Return Value

`true` if the configuration in the receiver specified by `configuration` is
compatible with the store metadata given by `metadata`, otherwise `false`.

## Discussion

This method compares the version information in the store metadata with the
entity versions of a given configuration. For information on specific
differences, use `entityVersionHashesByName` and perform an entity-by-entity
comparison.

## See Also

### Versioning and migrating entities

`var versionChecksum: String`

The Base64-encoded 128-bit model version hash.

`var versionIdentifiers: Set<AnyHashable>`

The set of developer-defined version identifiers for the object model.

`var entityVersionHashesByName: [String : Data]`

The dictionary of the model’s entity names and their corresponding version
hashes.

Instance Method

# makeManagedObjectModel(for:mergedWith:)

SwiftData  Core Data  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 14.4+

    
    
    func makeManagedObjectModel(
        for schema: Schema,
        mergedWith managedObjectModel: NSManagedObjectModel? = nil
    ) -> NSManagedObjectModel?

Type Method

# makeManagedObjectModel(for:mergedWith:)

SwiftData  Core Data  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 14.4+

    
    
    static func makeManagedObjectModel(
        for entityTypes: [any PersistentModel.Type],
        mergedWith managedObjectModel: NSManagedObjectModel? = nil
    ) -> NSManagedObjectModel?

