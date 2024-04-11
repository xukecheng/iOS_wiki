Instance Property

# inverseRelationship

The relationship that represents the inverse of the current relationship.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var inverseRelationship: NSRelationshipDescription? { get set }

## Discussion

The inverse relationship is the description of the current relationship from
the destination entity’s perspective. For example, the inverse of a
department’s relationship to an employee (a to-many relationship) is the
employees’ relationship to the department (a to-one relationship).

## See Also

### Configuring the Destination

`var destinationEntity: NSEntityDescription?`

The type of object the relationship contains.

`var isOrdered: Bool`

A Boolean value that determines whether the relationship preserves the order
of the referenced managed objects.

Instance Property

# destinationEntity

The type of object the relationship contains.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var destinationEntity: NSEntityDescription? { get set }

## See Also

### Configuring the Destination

`var inverseRelationship: NSRelationshipDescription?`

The relationship that represents the inverse of the current relationship.

`var isOrdered: Bool`

A Boolean value that determines whether the relationship preserves the order
of the referenced managed objects.

Instance Property

# isOrdered

A Boolean value that determines whether the relationship preserves the order
of the referenced managed objects.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isOrdered: Bool { get set }

## Discussion

The default value is `false`.

## See Also

### Configuring the Destination

`var inverseRelationship: NSRelationshipDescription?`

The relationship that represents the inverse of the current relationship.

`var destinationEntity: NSEntityDescription?`

The type of object the relationship contains.

Instance Property

# isToMany

Returns a Boolean value that indicates whether the relationship can contain
many managed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isToMany: Bool { get }

## Discussion

If `maxCount` is equal to `1`, implying a to-one relationship, this property
returns `false`; otherwise, it returns `true`.

## See Also

### Configuring Cardinality

`var minCount: Int`

The minimum number of managed objects the relationship can reference.

`var maxCount: Int`

The maximum number of managed objects the relationship can reference.

Instance Property

# minCount

The minimum number of managed objects the relationship can reference.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var minCount: Int { get set }

## Discussion

If you declare a relationship attribute as optional when defining your
entities, the framework only enforces `minCount` and `maxCount` when that
attribute is not `nil`.

The default value is `0`.

## See Also

### Configuring Cardinality

`var isToMany: Bool`

Returns a Boolean value that indicates whether the relationship can contain
many managed objects.

`var maxCount: Int`

The maximum number of managed objects the relationship can reference.

Instance Property

# maxCount

The maximum number of managed objects the relationship can reference.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var maxCount: Int { get set }

## Discussion

If you declare a relationship attribute as optional when defining your
entities, the framework only enforces `minCount` and `maxCount` when that
attribute is not `nil`.

The default value is `0`.

## See Also

### Configuring Cardinality

`var isToMany: Bool`

Returns a Boolean value that indicates whether the relationship can contain
many managed objects.

`var minCount: Int`

The minimum number of managed objects the relationship can reference.

Instance Property

# deleteRule

The rule to apply when you delete the relationship’s owning managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var deleteRule: NSDeleteRule { get set }

## Discussion

The default value is `NSDeleteRule.nullifyDeleteRule`. For possible values,
see `NSDeleteRule`.

## See Also

### Configuring Delete Behavior

`enum NSDeleteRule`

Constants that determine what happens when you delete a relationship’s owning
managed object.

Instance Property

# versionHash

The relationship’s unique identity.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

To calculate its version hash, the relationship combines its superclass’s
`versionHash` property with the values of `inverseRelationship`,
`destinationEntity`, `minCount`, and `maxCount`.

Instance Property

# inverseRelationship

The relationship that represents the inverse of the current relationship.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var inverseRelationship: NSRelationshipDescription? { get set }

## Discussion

The inverse relationship is the description of the current relationship from
the destination entity’s perspective. For example, the inverse of a
department’s relationship to an employee (a to-many relationship) is the
employees’ relationship to the department (a to-one relationship).

## See Also

### Configuring the Destination

`var destinationEntity: NSEntityDescription?`

The type of object the relationship contains.

`var isOrdered: Bool`

A Boolean value that determines whether the relationship preserves the order
of the referenced managed objects.

Instance Property

# destinationEntity

The type of object the relationship contains.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var destinationEntity: NSEntityDescription? { get set }

## See Also

### Configuring the Destination

`var inverseRelationship: NSRelationshipDescription?`

The relationship that represents the inverse of the current relationship.

`var isOrdered: Bool`

A Boolean value that determines whether the relationship preserves the order
of the referenced managed objects.

Instance Property

# isOrdered

A Boolean value that determines whether the relationship preserves the order
of the referenced managed objects.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isOrdered: Bool { get set }

## Discussion

The default value is `false`.

## See Also

### Configuring the Destination

`var inverseRelationship: NSRelationshipDescription?`

The relationship that represents the inverse of the current relationship.

`var destinationEntity: NSEntityDescription?`

The type of object the relationship contains.

Instance Property

# isToMany

Returns a Boolean value that indicates whether the relationship can contain
many managed objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isToMany: Bool { get }

## Discussion

If `maxCount` is equal to `1`, implying a to-one relationship, this property
returns `false`; otherwise, it returns `true`.

## See Also

### Configuring Cardinality

`var minCount: Int`

The minimum number of managed objects the relationship can reference.

`var maxCount: Int`

The maximum number of managed objects the relationship can reference.

Instance Property

# minCount

The minimum number of managed objects the relationship can reference.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var minCount: Int { get set }

## Discussion

If you declare a relationship attribute as optional when defining your
entities, the framework only enforces `minCount` and `maxCount` when that
attribute is not `nil`.

The default value is `0`.

## See Also

### Configuring Cardinality

`var isToMany: Bool`

Returns a Boolean value that indicates whether the relationship can contain
many managed objects.

`var maxCount: Int`

The maximum number of managed objects the relationship can reference.

Instance Property

# maxCount

The maximum number of managed objects the relationship can reference.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var maxCount: Int { get set }

## Discussion

If you declare a relationship attribute as optional when defining your
entities, the framework only enforces `minCount` and `maxCount` when that
attribute is not `nil`.

The default value is `0`.

## See Also

### Configuring Cardinality

`var isToMany: Bool`

Returns a Boolean value that indicates whether the relationship can contain
many managed objects.

`var minCount: Int`

The minimum number of managed objects the relationship can reference.

Instance Property

# deleteRule

The rule to apply when you delete the relationship’s owning managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var deleteRule: NSDeleteRule { get set }

## Discussion

The default value is `NSDeleteRule.nullifyDeleteRule`. For possible values,
see `NSDeleteRule`.

## See Also

### Configuring Delete Behavior

`enum NSDeleteRule`

Constants that determine what happens when you delete a relationship’s owning
managed object.

Instance Property

# versionHash

The relationship’s unique identity.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

To calculate its version hash, the relationship combines its superclass’s
`versionHash` property with the values of `inverseRelationship`,
`destinationEntity`, `minCount`, and `maxCount`.

