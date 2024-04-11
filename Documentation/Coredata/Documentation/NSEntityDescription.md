Instance Property

# name

The entity name of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var name: String? { get set }

## Discussion

Setting the name raises an exception if the receiver’s model has been used by
an object graph manager.

## See Also

### Getting descriptive information

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

### Related Documentation

Core Data Programming Guide

Instance Property

# managedObjectModel

The managed object model with which the receiver is associated.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

### Related Documentation

`func setEntities([NSEntityDescription], forConfigurationName: String)`

Associates the specified entities with the model using the given configuration
name.

`var entities: [NSEntityDescription]`

The entities in the model.

Instance Property

# managedObjectClassName

The name of the class that represents the receiver’s entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var managedObjectClassName: String! { get set }

## Discussion

The class specified by `name` must `NSManagedObject` or a subclass of
`NSManagedObject`.

### Special Considerations

Setting the class name raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# renamingIdentifier

The renaming identifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var renamingIdentifier: String? { get set }

## Discussion

The renaming identifier is used to resolve naming conflicts between models.
When creating a mapping model between two managed object models, a source
entity and a destination entity that share the same identifier indicate that
an entity mapping should be configured to migrate from the source to the
destination.

If you do not set this value, the identifier will return the entity’s name.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# isAbstract

A Boolean value that indicates whether the receiver represents an abstract
entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isAbstract: Bool { get set }

## Return Value

`true` if the receiver represents an abstract entity, otherwise `false`.

## Discussion

`true` if the receiver represents an abstract entity, otherwise `false`. An
abstract entity might be Shape, with concrete sub-entities such as Rectangle,
Triangle, and Circle.

### Special Considerations

Setting whether an entity is abstract raises an exception if the receiver’s
model has been used by an object graph manager.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# userInfo

The user info dictionary of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var userInfo: [AnyHashable : Any]? { get set }

## Discussion

Setting the user info dictionary raises an exception if the receiver’s model
has been used by an object graph manager.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# coreSpotlightDisplayNameExpression

The expression that computes the CoreSpotlight display name for instances of
the entity.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var coreSpotlightDisplayNameExpression: NSExpression { get set }

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# subentitiesByName

A dictionary containing the receiver’s sub-entities.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var subentitiesByName: [String : NSEntityDescription] { get }

## Return Value

The keys in the dictionary are the sub-entity names, the corresponding values
are instances of `NSEntityDescription`.

## See Also

### Managing inheritance

`var subentities: [NSEntityDescription]`

An array containing the sub-entities of the receiver.

`var superentity: NSEntityDescription?`

The super-entity of the receiver.

`func isKindOf(entity: NSEntityDescription) -> Bool`

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

Instance Property

# subentities

An array containing the sub-entities of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var subentities: [NSEntityDescription] { get set }

## Discussion

The sub-entities are instances of `NSEntityDescription`.

### Special Considerations

Setting the sub-entities raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Managing inheritance

`var subentitiesByName: [String : NSEntityDescription]`

A dictionary containing the receiver’s sub-entities.

`var superentity: NSEntityDescription?`

The super-entity of the receiver.

`func isKindOf(entity: NSEntityDescription) -> Bool`

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

Instance Property

# superentity

The super-entity of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var superentity: NSEntityDescription? { get }

## Discussion

If the receiver has no super-entity, returns `nil`.

## See Also

### Managing inheritance

`var subentitiesByName: [String : NSEntityDescription]`

A dictionary containing the receiver’s sub-entities.

`var subentities: [NSEntityDescription]`

An array containing the sub-entities of the receiver.

`func isKindOf(entity: NSEntityDescription) -> Bool`

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

Instance Method

# isKindOf(entity:)

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func isKindOf(entity: NSEntityDescription) -> Bool

##  Parameters

`entity`

    

An entity.

## Return Value

`true` if the receiver is a sub-entity of `entity`, otherwise `false`.

## See Also

### Managing inheritance

`var subentitiesByName: [String : NSEntityDescription]`

A dictionary containing the receiver’s sub-entities.

`var subentities: [NSEntityDescription]`

An array containing the sub-entities of the receiver.

`var superentity: NSEntityDescription?`

The super-entity of the receiver.

Instance Property

# propertiesByName

A dictionary containing the properties of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var propertiesByName: [String : NSPropertyDescription] { get }

## Discussion

The keys in the dictionary are the property names and the values are instances
of `NSAttributeDescription` and/or `NSRelationshipDescription`.

## See Also

### Working with properties

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Property

# properties

An array containing the properties of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var properties: [NSPropertyDescription] { get set }

## Discussion

The elements in the array are instances of `NSAttributeDescription`,
`NSRelationshipDescription`, and/or `NSFetchedPropertyDescription`.

### Special Considerations

Setting the properties raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Property

# attributesByName

The attributes of the receiver in a dictionary.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var attributesByName: [String : NSAttributeDescription] { get }

## Discussion

The keys in the dictionary are the attribute names and the values are
instances of `NSAttributeDescription`. .

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Property

# relationshipsByName

The relationships of the receiver in a dictionary.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var relationshipsByName: [String : NSRelationshipDescription] { get }

## Discussion

The keys in the dictionary are the relationship names and the values are
instances of `NSRelationshipDescription`.

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Method

# relationships(forDestination:)

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func relationships(forDestination entity: NSEntityDescription) -> [NSRelationshipDescription]

##  Parameters

`entity`

    

An entity description.

## Return Value

An array containing the relationships of the receiver where the entity
description of the relationship is `entity`. Elements in the array are
instances of `NSRelationshipDescription`.

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

Instance Property

# indexes

An array of fetch index descriptions for the entity.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var indexes: [NSFetchIndexDescription] { get set }

## Discussion

This value doesn’t form part of the entity’s version hash, and stores that
don’t natively support indexing may ignore it.

Important

Set indexes last in a model. Changing an entity hierarchy in any way that
affects the validity of indexes drops all existing indexes for entities in
that hierarchy, such as adding or removing superentities or subentities, or
adding and removing properties anywhere in the hierarchy.

## See Also

### Configuring indexes and constraints

`var uniquenessConstraints: [[Any]]`

An array of arrays that contains one or more attributes with a value that must
be unique over the instances of that entity.

`var compoundIndexes: [[Any]]`

The compound indexes for the entity as an array of arrays.

Deprecated

Instance Property

# uniquenessConstraints

An array of arrays that contains one or more attributes with a value that must
be unique over the instances of that entity.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var uniquenessConstraints: [[Any]] { get set }

## Discussion

Each inner array contains one or more `NSAttributeDescription` objects or
strings that contain the names of attributes on the entity.

This value forms part of the entity’s version hash. Stores that don’t support
uniqueness constraints must refuse to initialize when receiving a model that
contains such constraints.

Note

Uniqueness constraint violations can be computationally expensive to handle.
The recommendation is to use only one uniqueness constraint per entity
hierarchy, although subentites may extend a superentity’s constraint.

## See Also

### Configuring indexes and constraints

`var indexes: [NSFetchIndexDescription]`

An array of fetch index descriptions for the entity.

`var compoundIndexes: [[Any]]`

The compound indexes for the entity as an array of arrays.

Deprecated

Instance Property

# compoundIndexes

The compound indexes for the entity as an array of arrays.

iOS 3.0–11.0  Deprecated  iPadOS 3.0–11.0  Deprecated  macOS 10.5–10.13
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–11.0  Deprecated
watchOS 2.0–4.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    var compoundIndexes: [[Any]] { get set }

## Discussion

The arrays contained in the returned array contain instances of
`NSAttributeDescription`, `NSRelationshipDescription` that represent
properties of the entity, or of `NSString` that match the name of attributes
or relationships of the entity.

Compound indexes are only used by stores that natively support compound
indices—setting them is only advisory. Indexes apply to the entire inheritance
hierarchy.

## See Also

### Configuring indexes and constraints

`var indexes: [NSFetchIndexDescription]`

An array of fetch index descriptions for the entity.

`var uniquenessConstraints: [[Any]]`

An array of arrays that contains one or more attributes with a value that must
be unique over the instances of that entity.

Type Method

# insertNewObject(forEntityName:into:)

Creates, configures, and returns an instance of the class for the entity with
a given name.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func insertNewObject(
        forEntityName entityName: String,
        into context: NSManagedObjectContext
    ) -> NSManagedObject

##  Parameters

`entityName`

    

The name of an entity.

`context`

    

The managed object context to use.

## Return Value

A new, autoreleased, fully configured instance of the class for the entity
named `entityName`. The instance has its entity description set and is
inserted it into `context`.

## Discussion

This method makes it easy for you to create instances of a given entity
without worrying about the details of managed object creation. The method is
conceptually similar to the following code example.

## See Also

### Related Documentation

`init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)`

Initializes a managed object from an entity description and inserts it into
the specified managed object context.

Type Method

# entity(forEntityName:in:)

Returns the entity with the specified name from the managed object model
associated with the specified managed object context’s persistent store
coordinator.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func entity(
        forEntityName entityName: String,
        in context: NSManagedObjectContext
    ) -> NSEntityDescription?

##  Parameters

`entityName`

    

The name of an entity.

`context`

    

The managed object context to use. Must not be `nil`.

## Return Value

The entity with the specified name from the managed object model associated
with `context`’s persistent store coordinator.

## Discussion

Raises `internalInconsistencyException` if `context` is `nil`.

This method is functionally equivalent to the following code example.

## See Also

### Related Documentation

`var entitiesByName: [String : NSEntityDescription]`

The entities of the model, keyed by name.

Instance Property

# versionHash

The version hash for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

The version hash is used to uniquely identify an entity based on the
collection and configuration of properties for the entity. The version hash
uses only values which affect the persistence of data and the user-defined
`versionHashModifier` value. (The values which affect persistence are: the
name of the entity, the version hash of the superentity (if present), if the
entity is abstract, and all of the version hashes for the properties.) This
value is stored as part of the version information in the metadata for stores
which use this entity, as well as a definition of an entity involved in an
`NSEntityMapping` object.

## See Also

### Managing versioning

`var versionHashModifier: String?`

The version hash modifier for the receiver.

Instance Property

# versionHashModifier

The version hash modifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHashModifier: String? { get set }

## Discussion

This value is included in the version hash for the entity. You use it to mark
or denote an entity as being a different “version” than another even if all of
the values which affect persistence are equal. (Such a difference is important
in cases where, for example, the structure of an entity is unchanged but the
format or content of data has changed.)

## See Also

### Managing versioning

`var versionHash: Data`

The version hash for the receiver.

Instance Property

# name

The entity name of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var name: String? { get set }

## Discussion

Setting the name raises an exception if the receiver’s model has been used by
an object graph manager.

## See Also

### Getting descriptive information

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

### Related Documentation

Core Data Programming Guide

Instance Property

# managedObjectModel

The managed object model with which the receiver is associated.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

### Related Documentation

`func setEntities([NSEntityDescription], forConfigurationName: String)`

Associates the specified entities with the model using the given configuration
name.

`var entities: [NSEntityDescription]`

The entities in the model.

Instance Property

# managedObjectClassName

The name of the class that represents the receiver’s entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var managedObjectClassName: String! { get set }

## Discussion

The class specified by `name` must `NSManagedObject` or a subclass of
`NSManagedObject`.

### Special Considerations

Setting the class name raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# renamingIdentifier

The renaming identifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var renamingIdentifier: String? { get set }

## Discussion

The renaming identifier is used to resolve naming conflicts between models.
When creating a mapping model between two managed object models, a source
entity and a destination entity that share the same identifier indicate that
an entity mapping should be configured to migrate from the source to the
destination.

If you do not set this value, the identifier will return the entity’s name.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# isAbstract

A Boolean value that indicates whether the receiver represents an abstract
entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isAbstract: Bool { get set }

## Return Value

`true` if the receiver represents an abstract entity, otherwise `false`.

## Discussion

`true` if the receiver represents an abstract entity, otherwise `false`. An
abstract entity might be Shape, with concrete sub-entities such as Rectangle,
Triangle, and Circle.

### Special Considerations

Setting whether an entity is abstract raises an exception if the receiver’s
model has been used by an object graph manager.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# userInfo

The user info dictionary of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var userInfo: [AnyHashable : Any]? { get set }

## Discussion

Setting the user info dictionary raises an exception if the receiver’s model
has been used by an object graph manager.

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var coreSpotlightDisplayNameExpression: NSExpression`

The expression that computes the CoreSpotlight display name for instances of
the entity.

Instance Property

# coreSpotlightDisplayNameExpression

The expression that computes the CoreSpotlight display name for instances of
the entity.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var coreSpotlightDisplayNameExpression: NSExpression { get set }

## See Also

### Getting descriptive information

`var name: String?`

The entity name of the receiver.

`var managedObjectModel: NSManagedObjectModel`

The managed object model with which the receiver is associated.

`var managedObjectClassName: String!`

The name of the class that represents the receiver’s entity.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

`var isAbstract: Bool`

A Boolean value that indicates whether the receiver represents an abstract
entity.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# subentitiesByName

A dictionary containing the receiver’s sub-entities.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var subentitiesByName: [String : NSEntityDescription] { get }

## Return Value

The keys in the dictionary are the sub-entity names, the corresponding values
are instances of `NSEntityDescription`.

## See Also

### Managing inheritance

`var subentities: [NSEntityDescription]`

An array containing the sub-entities of the receiver.

`var superentity: NSEntityDescription?`

The super-entity of the receiver.

`func isKindOf(entity: NSEntityDescription) -> Bool`

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

Instance Property

# subentities

An array containing the sub-entities of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var subentities: [NSEntityDescription] { get set }

## Discussion

The sub-entities are instances of `NSEntityDescription`.

### Special Considerations

Setting the sub-entities raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Managing inheritance

`var subentitiesByName: [String : NSEntityDescription]`

A dictionary containing the receiver’s sub-entities.

`var superentity: NSEntityDescription?`

The super-entity of the receiver.

`func isKindOf(entity: NSEntityDescription) -> Bool`

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

Instance Property

# superentity

The super-entity of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var superentity: NSEntityDescription? { get }

## Discussion

If the receiver has no super-entity, returns `nil`.

## See Also

### Managing inheritance

`var subentitiesByName: [String : NSEntityDescription]`

A dictionary containing the receiver’s sub-entities.

`var subentities: [NSEntityDescription]`

An array containing the sub-entities of the receiver.

`func isKindOf(entity: NSEntityDescription) -> Bool`

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

Instance Method

# isKindOf(entity:)

Returns a Boolean value that indicates whether the receiver is a sub-entity of
another given entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func isKindOf(entity: NSEntityDescription) -> Bool

##  Parameters

`entity`

    

An entity.

## Return Value

`true` if the receiver is a sub-entity of `entity`, otherwise `false`.

## See Also

### Managing inheritance

`var subentitiesByName: [String : NSEntityDescription]`

A dictionary containing the receiver’s sub-entities.

`var subentities: [NSEntityDescription]`

An array containing the sub-entities of the receiver.

`var superentity: NSEntityDescription?`

The super-entity of the receiver.

Instance Property

# propertiesByName

A dictionary containing the properties of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var propertiesByName: [String : NSPropertyDescription] { get }

## Discussion

The keys in the dictionary are the property names and the values are instances
of `NSAttributeDescription` and/or `NSRelationshipDescription`.

## See Also

### Working with properties

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Property

# properties

An array containing the properties of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var properties: [NSPropertyDescription] { get set }

## Discussion

The elements in the array are instances of `NSAttributeDescription`,
`NSRelationshipDescription`, and/or `NSFetchedPropertyDescription`.

### Special Considerations

Setting the properties raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Property

# attributesByName

The attributes of the receiver in a dictionary.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var attributesByName: [String : NSAttributeDescription] { get }

## Discussion

The keys in the dictionary are the attribute names and the values are
instances of `NSAttributeDescription`. .

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Property

# relationshipsByName

The relationships of the receiver in a dictionary.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var relationshipsByName: [String : NSRelationshipDescription] { get }

## Discussion

The keys in the dictionary are the relationship names and the values are
instances of `NSRelationshipDescription`.

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`func relationships(forDestination: NSEntityDescription) ->
[NSRelationshipDescription]`

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

Instance Method

# relationships(forDestination:)

Returns an array containing the relationships of the receiver where the entity
description of the relationship is a given entity.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func relationships(forDestination entity: NSEntityDescription) -> [NSRelationshipDescription]

##  Parameters

`entity`

    

An entity description.

## Return Value

An array containing the relationships of the receiver where the entity
description of the relationship is `entity`. Elements in the array are
instances of `NSRelationshipDescription`.

## See Also

### Working with properties

`var propertiesByName: [String : NSPropertyDescription]`

A dictionary containing the properties of the receiver.

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

`var attributesByName: [String : NSAttributeDescription]`

The attributes of the receiver in a dictionary.

`var relationshipsByName: [String : NSRelationshipDescription]`

The relationships of the receiver in a dictionary.

Instance Property

# indexes

An array of fetch index descriptions for the entity.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var indexes: [NSFetchIndexDescription] { get set }

## Discussion

This value doesn’t form part of the entity’s version hash, and stores that
don’t natively support indexing may ignore it.

Important

Set indexes last in a model. Changing an entity hierarchy in any way that
affects the validity of indexes drops all existing indexes for entities in
that hierarchy, such as adding or removing superentities or subentities, or
adding and removing properties anywhere in the hierarchy.

## See Also

### Configuring indexes and constraints

`var uniquenessConstraints: [[Any]]`

An array of arrays that contains one or more attributes with a value that must
be unique over the instances of that entity.

`var compoundIndexes: [[Any]]`

The compound indexes for the entity as an array of arrays.

Deprecated

Instance Property

# uniquenessConstraints

An array of arrays that contains one or more attributes with a value that must
be unique over the instances of that entity.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var uniquenessConstraints: [[Any]] { get set }

## Discussion

Each inner array contains one or more `NSAttributeDescription` objects or
strings that contain the names of attributes on the entity.

This value forms part of the entity’s version hash. Stores that don’t support
uniqueness constraints must refuse to initialize when receiving a model that
contains such constraints.

Note

Uniqueness constraint violations can be computationally expensive to handle.
The recommendation is to use only one uniqueness constraint per entity
hierarchy, although subentites may extend a superentity’s constraint.

## See Also

### Configuring indexes and constraints

`var indexes: [NSFetchIndexDescription]`

An array of fetch index descriptions for the entity.

`var compoundIndexes: [[Any]]`

The compound indexes for the entity as an array of arrays.

Deprecated

Instance Property

# compoundIndexes

The compound indexes for the entity as an array of arrays.

iOS 3.0–11.0  Deprecated  iPadOS 3.0–11.0  Deprecated  macOS 10.5–10.13
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–11.0  Deprecated
watchOS 2.0–4.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    var compoundIndexes: [[Any]] { get set }

## Discussion

The arrays contained in the returned array contain instances of
`NSAttributeDescription`, `NSRelationshipDescription` that represent
properties of the entity, or of `NSString` that match the name of attributes
or relationships of the entity.

Compound indexes are only used by stores that natively support compound
indices—setting them is only advisory. Indexes apply to the entire inheritance
hierarchy.

## See Also

### Configuring indexes and constraints

`var indexes: [NSFetchIndexDescription]`

An array of fetch index descriptions for the entity.

`var uniquenessConstraints: [[Any]]`

An array of arrays that contains one or more attributes with a value that must
be unique over the instances of that entity.

Type Method

# insertNewObject(forEntityName:into:)

Creates, configures, and returns an instance of the class for the entity with
a given name.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func insertNewObject(
        forEntityName entityName: String,
        into context: NSManagedObjectContext
    ) -> NSManagedObject

##  Parameters

`entityName`

    

The name of an entity.

`context`

    

The managed object context to use.

## Return Value

A new, autoreleased, fully configured instance of the class for the entity
named `entityName`. The instance has its entity description set and is
inserted it into `context`.

## Discussion

This method makes it easy for you to create instances of a given entity
without worrying about the details of managed object creation. The method is
conceptually similar to the following code example.

## See Also

### Related Documentation

`init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)`

Initializes a managed object from an entity description and inserts it into
the specified managed object context.

Type Method

# entity(forEntityName:in:)

Returns the entity with the specified name from the managed object model
associated with the specified managed object context’s persistent store
coordinator.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class func entity(
        forEntityName entityName: String,
        in context: NSManagedObjectContext
    ) -> NSEntityDescription?

##  Parameters

`entityName`

    

The name of an entity.

`context`

    

The managed object context to use. Must not be `nil`.

## Return Value

The entity with the specified name from the managed object model associated
with `context`’s persistent store coordinator.

## Discussion

Raises `internalInconsistencyException` if `context` is `nil`.

This method is functionally equivalent to the following code example.

    
    
    NSManagedObjectModel *managedObjectModel = [[context persistentStoreCoordinator] managedObjectModel];
    NSEntityDescription *entity = [[managedObjectModel entitiesByName] objectForKey:entityName];
    return entity;
    

## See Also

### Related Documentation

`var entitiesByName: [String : NSEntityDescription]`

The entities of the model, keyed by name.

Instance Property

# versionHash

The version hash for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

The version hash is used to uniquely identify an entity based on the
collection and configuration of properties for the entity. The version hash
uses only values which affect the persistence of data and the user-defined
`versionHashModifier` value. (The values which affect persistence are: the
name of the entity, the version hash of the superentity (if present), if the
entity is abstract, and all of the version hashes for the properties.) This
value is stored as part of the version information in the metadata for stores
which use this entity, as well as a definition of an entity involved in an
`NSEntityMapping` object.

## See Also

### Managing versioning

`var versionHashModifier: String?`

The version hash modifier for the receiver.

Instance Property

# versionHashModifier

The version hash modifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHashModifier: String? { get set }

## Discussion

This value is included in the version hash for the entity. You use it to mark
or denote an entity as being a different “version” than another even if all of
the values which affect persistence are equal. (Such a difference is important
in cases where, for example, the structure of an entity is unchanged but the
format or content of data has changed.)

## See Also

### Managing versioning

`var versionHash: Data`

The version hash for the receiver.

