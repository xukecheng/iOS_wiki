Initializer

# init(objectID:)

Returns a cache node for the given managed object ID.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(objectID moid: NSManagedObjectID)

##  Parameters

`moid`

    

A managed object ID.

## Return Value

A cache node for the given managed object ID, or `nil` if the node could not
be initialized.

## See Also

### Related Documentation

Core Data Programming Guide

Instance Property

# objectID

The managed object ID of the node.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var objectID: NSManagedObjectID { get }

## See Also

### Managing Node Data

`var propertyCache: NSMutableDictionary?`

The property cache dictionary of the node.

`func value(forKey: String) -> Any?`

Returns the value for a given key.

`func setValue(Any?, forKey: String)`

Sets the value for the given key.

Instance Property

# propertyCache

The property cache dictionary of the node.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var propertyCache: NSMutableDictionary? { get set }

## Discussion

This dictionary is used by `value(forKey:)` and `setValue(_:forKey:)` for
property values. This property is `nil` unless it has been explicitly set or
non-`nil` values have been set for keys using `setValue(_:forKey:)`.

## See Also

### Managing Node Data

`var objectID: NSManagedObjectID`

The managed object ID of the node.

`func value(forKey: String) -> Any?`

Returns the value for a given key.

`func setValue(Any?, forKey: String)`

Sets the value for the given key.

Instance Method

# value(forKey:)

Returns the value for a given key.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func value(forKey key: String) -> Any?

##  Parameters

`key`

    

The name of a property.

## Return Value

The value for the property named `key`. For an attribute, the return value is
an instance of an attribute type supported by Core Data (see
`NSAttributeDescription`); for a to-one relationship, the return value must be
another cache node instance; for a to-many relationship, the return value must
be an collection of the related cache nodes.

## Discussion

The default implementation forwards the request to the `propertyCache`
dictionary if `key` matches a property name of the entity for the cache node.
If `key` does not represent a property, the standard `value(forKey:)`
implementation is used.

## See Also

### Managing Node Data

`var objectID: NSManagedObjectID`

The managed object ID of the node.

`var propertyCache: NSMutableDictionary?`

The property cache dictionary of the node.

`func setValue(Any?, forKey: String)`

Sets the value for the given key.

Instance Method

# setValue(_:forKey:)

Sets the value for the given key.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setValue(
        _ value: Any?,
        forKey key: String
    )

##  Parameters

`value`

    

The value for the property identified by `key`.

`key`

    

The name of a property.

## Discussion

The default implementation forwards the request to the `propertyCache`
dictionary if `key` matches a property name of the entity for this cache node.
If `key` does not represent a property, the standard `setValue(_:forKey:)`
implementation is used.

## See Also

### Managing Node Data

`var objectID: NSManagedObjectID`

The managed object ID of the node.

`var propertyCache: NSMutableDictionary?`

The property cache dictionary of the node.

`func value(forKey: String) -> Any?`

Returns the value for a given key.

