Initializer

# init(objectID:withValues:version:)

Returns an object initialized with the given values.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        objectID: NSManagedObjectID,
        withValues values: [String : Any],
        version: UInt64
    )

##  Parameters

`objectID`

    

A managed object ID.

`values`

    

A dictionary containing the values persisted in an external store with keys
corresponding to the names of the property description in the
`NSEntityDescription` object described by `objectID`:

  * For attributes: an immutable value (an instance of a value class such as `NSNumber`, `NSString`, `NSData`). Missing attribute keys will assume a nil value.

  * For to-one relationships: the managed object ID of the related object or an instance of `NSNull` for nil relationship values. A missing key will be resolved lazily through calling `newValueForRelationship:forObjectWithID:withContext:error:` on the `NSPersistentStore` object. Lazy resolution for to-one relationships is discouraged.

  * For to-many relationships: an instance of `NSArray` or `NSSet` containing the managed object IDs of the related objects. Empty to-many relationships must be represented by an empty non-nil collection. A missing key will be resolved lazily through calling `newValueForRelationship:forObjectWithID:withContext:error:` on the `NSPersistentStore` object. Lazy resolution for to-many relationships is encouraged.

Unknown or unmodeled keys are stripped out.

`version`

    

The revision number of this state. This value is used for conflict detection
and merging.

## Return Value

An object initialized with the given values.

## See Also

### Related Documentation

Incremental Store Programming Guide

Instance Property

# objectID

The object ID that identifies the data stored by the receiver.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var objectID: NSManagedObjectID { get }

## See Also

### Managing Node Data

`func update(withValues: [String : Any], version: UInt64)`

Update the values and version to reflect new data being saved to or loaded
from the external store.

`func value(for: NSPropertyDescription) -> Any?`

Returns the value for the given property.

`var version: UInt64`

The version of data in the receiver.

Instance Method

# update(withValues:version:)

Update the values and version to reflect new data being saved to or loaded
from the external store.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func update(
        withValues values: [String : Any],
        version: UInt64
    )

##  Parameters

`values`

    

A dictionary containing updated values, in the same format as that described
in `init(objectID:withValues:version:)`.

`version`

    

The version number for the transaction.

## Discussion

Update the values and version to reflect new data being saved to or loaded
from the external store. // The values dictionary is in the same format as the
initializer

## See Also

### Managing Node Data

`var objectID: NSManagedObjectID`

The object ID that identifies the data stored by the receiver.

`func value(for: NSPropertyDescription) -> Any?`

Returns the value for the given property.

`var version: UInt64`

The version of data in the receiver.

Instance Method

# value(for:)

Returns the value for the given property.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func value(for prop: NSPropertyDescription) -> Any?

##  Parameters

`prop`

    

A property description for one of the properties in the receiver.

## Return Value

The value for the property specified by `prop`. May return an instance of
`NSNull` for to-one relationships.

## Discussion

If a relationship is `nil`, you should create a new value by invoking
`newValueForRelationship:forObjectWithID:withContext:error:` on the
`NSPersistentStore` object.

## See Also

### Managing Node Data

`var objectID: NSManagedObjectID`

The object ID that identifies the data stored by the receiver.

`func update(withValues: [String : Any], version: UInt64)`

Update the values and version to reflect new data being saved to or loaded
from the external store.

`var version: UInt64`

The version of data in the receiver.

Instance Property

# version

The version of data in the receiver.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var version: UInt64 { get }

## Discussion

The version number is used by the persistent store coordinator to detect and
handle merge conflicts. The version number should be stored with the record.
The version number should (implicitly) start at zero (where zero indicates an
unsaved object in memory) and be incremented by exactly one every time you
save. In addition, you increment the version number when you or the Core Data
framework have marked the associated managed object for optimistic locking.

## See Also

### Managing Node Data

`var objectID: NSManagedObjectID`

The object ID that identifies the data stored by the receiver.

`func update(withValues: [String : Any], version: UInt64)`

Update the values and version to reflect new data being saved to or loaded
from the external store.

`func value(for: NSPropertyDescription) -> Any?`

Returns the value for the given property.

