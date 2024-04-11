Instance Property

# sourceEntityName

The source entity name for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sourceEntityName: String? { get set }

## Discussion

Mappings are not directly bound to entity descriptions; you can use the
`sourceEntity(for:)` method on the migration manager to retrieve the entity
description for this entity name.

## See Also

### Managing Source Information

`var sourceEntityVersionHash: Data?`

The version hash of the source entity for the entity mapping.

`var sourceExpression: NSExpression?`

The source expression for the entity mapping.

### Related Documentation

Core Data Model Versioning and Data Migration Programming Guide

`var destinationEntityName: String?`

The destination entity name for the entity mapping.

Instance Property

# sourceEntityVersionHash

The version hash of the source entity for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sourceEntityVersionHash: Data? { get set }

## Discussion

The version hash is calculated by Core Data based on the property values of
the entity (see `NSEntityDescription`’s `versionHash` method). The
`sourceEntityVersionHash` must equal the version hash of the source entity
represented by the mapping.

## See Also

### Managing Source Information

`var sourceEntityName: String?`

The source entity name for the entity mapping.

`var sourceExpression: NSExpression?`

The source expression for the entity mapping.

### Related Documentation

`var destinationEntityVersionHash: Data?`

The version hash for the destination entity for the entity mapping.

Instance Property

# sourceExpression

The source expression for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var sourceExpression: NSExpression? { get set }

## Discussion

The source expression is used to obtain the collection of managed objects to
process through the mapping. The expression can be a fetch request expression,
or any other expression that evaluates to a collection.

## See Also

### Managing Source Information

`var sourceEntityName: String?`

The source entity name for the entity mapping.

`var sourceEntityVersionHash: Data?`

The version hash of the source entity for the entity mapping.

Instance Property

# destinationEntityName

The destination entity name for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var destinationEntityName: String? { get set }

## Discussion

Mappings are not directly bound to entity descriptions. You can use the
migration manager’s `destinationEntity(for:)` method to retrieve the entity
description for this entity name.

## See Also

### Managing Destination Information

`var destinationEntityVersionHash: Data?`

The version hash for the destination entity for the entity mapping.

### Related Documentation

`var sourceEntityName: String?`

The source entity name for the entity mapping.

Instance Property

# destinationEntityVersionHash

The version hash for the destination entity for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var destinationEntityVersionHash: Data? { get set }

## Discussion

The version hash is calculated by Core Data based on the property values of
the entity (see `NSEntityDescription`’s `versionHash` method). The
`destinationEntityVersionHash` must equal the version hash of the destination
entity represented by the mapping.

## See Also

### Managing Destination Information

`var destinationEntityName: String?`

The destination entity name for the entity mapping.

### Related Documentation

`var sourceEntityVersionHash: Data?`

The version hash of the source entity for the entity mapping.

Instance Property

# name

The name of the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var name: String! { get set }

## Discussion

The name is used only as a means of distinguishing mappings in a model. If not
specified, the value defaults to SOURCE->DESTINATION.

## See Also

### Managing Mapping Information

`var mappingType: NSEntityMappingType`

The mapping type for the entity mapping.

`var entityMigrationPolicyClassName: String?`

The class name of the migration policy for the entity mapping.

`var attributeMappings: [NSPropertyMapping]?`

The array of attribute mappings for the entity mapping.

`var relationshipMappings: [NSPropertyMapping]?`

The array of relationship mappings for the entity mapping.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary for the entity mapping.

Instance Property

# mappingType

The mapping type for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var mappingType: NSEntityMappingType { get set }

## Discussion

If you specify a custom entity mapping type, you must specify a value for the
migration policy class name as well (see `entityMigrationPolicyClassName`).

## See Also

### Managing Mapping Information

`var name: String!`

The name of the entity mapping.

`var entityMigrationPolicyClassName: String?`

The class name of the migration policy for the entity mapping.

`var attributeMappings: [NSPropertyMapping]?`

The array of attribute mappings for the entity mapping.

`var relationshipMappings: [NSPropertyMapping]?`

The array of relationship mappings for the entity mapping.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary for the entity mapping.

Instance Property

# entityMigrationPolicyClassName

The class name of the migration policy for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entityMigrationPolicyClassName: String? { get set }

## Discussion

If not specified, the default migration class name is
`NSEntityMigrationPolicy`. You can specify a subclass to provide custom
behavior.

## See Also

### Managing Mapping Information

`var name: String!`

The name of the entity mapping.

`var mappingType: NSEntityMappingType`

The mapping type for the entity mapping.

`var attributeMappings: [NSPropertyMapping]?`

The array of attribute mappings for the entity mapping.

`var relationshipMappings: [NSPropertyMapping]?`

The array of relationship mappings for the entity mapping.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary for the entity mapping.

Instance Property

# attributeMappings

The array of attribute mappings for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var attributeMappings: [NSPropertyMapping]? { get set }

## Discussion

The order of mappings in the array specifies the order in which the mappings
will be processed during a migration.

## See Also

### Managing Mapping Information

`var name: String!`

The name of the entity mapping.

`var mappingType: NSEntityMappingType`

The mapping type for the entity mapping.

`var entityMigrationPolicyClassName: String?`

The class name of the migration policy for the entity mapping.

`var relationshipMappings: [NSPropertyMapping]?`

The array of relationship mappings for the entity mapping.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary for the entity mapping.

Instance Property

# relationshipMappings

The array of relationship mappings for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var relationshipMappings: [NSPropertyMapping]? { get set }

## Discussion

The order of mappings in the array specifies the order in which the mappings
will be processed during a migration.

## See Also

### Managing Mapping Information

`var name: String!`

The name of the entity mapping.

`var mappingType: NSEntityMappingType`

The mapping type for the entity mapping.

`var entityMigrationPolicyClassName: String?`

The class name of the migration policy for the entity mapping.

`var attributeMappings: [NSPropertyMapping]?`

The array of attribute mappings for the entity mapping.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary for the entity mapping.

Instance Property

# userInfo

The user info dictionary for the entity mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var userInfo: [AnyHashable : Any]? { get set }

## Discussion

You can use the info dictionary in any way that might be useful in your
migration. You can set the contents of the dictionary directory or using the
appropriate inspector in the Xcode mapping model editor.

## See Also

### Managing Mapping Information

`var name: String!`

The name of the entity mapping.

`var mappingType: NSEntityMappingType`

The mapping type for the entity mapping.

`var entityMigrationPolicyClassName: String?`

The class name of the migration policy for the entity mapping.

`var attributeMappings: [NSPropertyMapping]?`

The array of attribute mappings for the entity mapping.

`var relationshipMappings: [NSPropertyMapping]?`

The array of relationship mappings for the entity mapping.

Enumeration Case

# NSEntityMappingType.undefinedEntityMappingType

Specifies that the developer handles destination instance creation.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case undefinedEntityMappingType = 0

Enumeration Case

# NSEntityMappingType.customEntityMappingType

Specifies a custom mapping.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case customEntityMappingType = 1

Enumeration Case

# NSEntityMappingType.addEntityMappingType

Specifies that this is a new entity in the destination model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case addEntityMappingType = 2

## Discussion

Instances of the entity only exist in the destination.

Enumeration Case

# NSEntityMappingType.removeEntityMappingType

Specifies that this entity is not present in the destination model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case removeEntityMappingType = 3

## Discussion

Instances of the entity only exist in the source—source instances are not
mapped to destination.

Enumeration Case

# NSEntityMappingType.copyEntityMappingType

Specifies that source instances are migrated as-is.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case copyEntityMappingType = 4

Enumeration Case

# NSEntityMappingType.transformEntityMappingType

Specifies that entity exists in source and destination and is mapped.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case transformEntityMappingType = 5

