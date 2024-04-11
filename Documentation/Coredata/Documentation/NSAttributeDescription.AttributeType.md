Type Property

# binaryData

An attribute that stores binary data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let binaryData: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# boolean

An attribute that stores a Boolean value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let boolean: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# composite

An attribute that derives its value by composing other attributes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static let composite: NSAttributeDescription.AttributeType

## Discussion

Composite attributes support all attribute types except the following:

  * `undefined`

  * `objectID`

  * `binaryData` (when `allowsExternalBinaryDataStorage` is `true`)

For more information, see `NSCompositeAttributeDescription`.

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# date

An attribute that stores a date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let date: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# decimal

An attribute that stores a decimal value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let decimal: NSAttributeDescription.AttributeType

## Discussion

Use instances of `NSDecimalNumber` when reading and writing attributes of this
type.

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# double

An attribute that stores a double value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let double: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# float

An attribute that stores a float value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let float: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# integer16

An attribute that stores a 16-bit signed integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let integer16: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# integer32

An attribute that stores a 32-bit signed integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let integer32: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# integer64

An attribute that stores a 64-bit signed integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let integer64: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# objectID

An attribute that stores a managed object’s ID.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let objectID: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# string

An attribute that stores a string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let string: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# transformable

An attribute that uses a value transformer to derive its value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let transformable: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# undefined

An attribute that doesn’t have an explicit type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let undefined: NSAttributeDescription.AttributeType

## Discussion

Use this attribute type with transient attributues only. Core Data manages the
attribute’s value and registers the necessary undo and redo actions.

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# uri

An attribute that stores a uniform resource identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let uri: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# uuid

An attribute that stores a universally unique identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let uuid: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

Initializer

# init(rawValue:)

Creates an attribute type using the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: NSAttributeType)

##  Parameters

`rawValue`

    

The raw attribute type. For possible values, see `NSAttributeType`.

## Relationships

### From Protocol

  * `RawRepresentable`

Instance Property

# rawValue

The attribute type’s cardinal value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var rawValue: NSAttributeType

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Getting an Attribute Type’s Raw Value

`typealias NSAttributeDescription.AttributeType.RawValue`

The type the conforming type uses to represent its values.

Type Alias

# NSAttributeDescription.AttributeType.RawValue

The type the conforming type uses to represent its values.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias NSAttributeDescription.AttributeType.RawValue = NSAttributeType

## See Also

### Getting an Attribute Type’s Raw Value

`var rawValue: NSAttributeType`

The attribute type’s cardinal value.

Instance Property

# hashValue

The attribute type’s computed hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Hashing an Attribute Type

`func hash(into: inout Hasher)`

Hashes the components of the attribute type using the provided hasher.

Instance Method

# hash(into:)

Hashes the components of the attribute type using the provided hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining components of this attribute type.

## See Also

### Hashing an Attribute Type

`var hashValue: Int`

The attribute type’s computed hash value.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: NSAttributeDescription.AttributeType, rhs: NSAttributeDescription.AttributeType) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

Type Property

# binaryData

An attribute that stores binary data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let binaryData: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# boolean

An attribute that stores a Boolean value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let boolean: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# composite

An attribute that derives its value by composing other attributes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static let composite: NSAttributeDescription.AttributeType

## Discussion

Composite attributes support all attribute types except the following:

  * `undefined`

  * `objectID`

  * `binaryData` (when `allowsExternalBinaryDataStorage` is `true`)

For more information, see `NSCompositeAttributeDescription`.

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# date

An attribute that stores a date.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let date: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# decimal

An attribute that stores a decimal value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let decimal: NSAttributeDescription.AttributeType

## Discussion

Use instances of `NSDecimalNumber` when reading and writing attributes of this
type.

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# double

An attribute that stores a double value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let double: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# float

An attribute that stores a float value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let float: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# integer16

An attribute that stores a 16-bit signed integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let integer16: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# integer32

An attribute that stores a 32-bit signed integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let integer32: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# integer64

An attribute that stores a 64-bit signed integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let integer64: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# objectID

An attribute that stores a managed object’s ID.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let objectID: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# string

An attribute that stores a string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let string: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# transformable

An attribute that uses a value transformer to derive its value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let transformable: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# undefined

An attribute that doesn’t have an explicit type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let undefined: NSAttributeDescription.AttributeType

## Discussion

Use this attribute type with transient attributues only. Core Data manages the
attribute’s value and registers the necessary undo and redo actions.

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# uri

An attribute that stores a uniform resource identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let uri: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uuid: NSAttributeDescription.AttributeType`

An attribute that stores a universally unique identifier.

Type Property

# uuid

An attribute that stores a universally unique identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static let uuid: NSAttributeDescription.AttributeType

## See Also

### Attribute Types

`static let binaryData: NSAttributeDescription.AttributeType`

An attribute that stores binary data.

`static let boolean: NSAttributeDescription.AttributeType`

An attribute that stores a Boolean value.

`static let composite: NSAttributeDescription.AttributeType`

An attribute that derives its value by composing other attributes.

`static let date: NSAttributeDescription.AttributeType`

An attribute that stores a date.

`static let decimal: NSAttributeDescription.AttributeType`

An attribute that stores a decimal value.

`static let double: NSAttributeDescription.AttributeType`

An attribute that stores a double value.

`static let float: NSAttributeDescription.AttributeType`

An attribute that stores a float value.

`static let integer16: NSAttributeDescription.AttributeType`

An attribute that stores a 16-bit signed integer value.

`static let integer32: NSAttributeDescription.AttributeType`

An attribute that stores a 32-bit signed integer value.

`static let integer64: NSAttributeDescription.AttributeType`

An attribute that stores a 64-bit signed integer value.

`static let objectID: NSAttributeDescription.AttributeType`

An attribute that stores a managed object’s ID.

`static let string: NSAttributeDescription.AttributeType`

An attribute that stores a string.

`static let transformable: NSAttributeDescription.AttributeType`

An attribute that uses a value transformer to derive its value.

`static let undefined: NSAttributeDescription.AttributeType`

An attribute that doesn’t have an explicit type.

`static let uri: NSAttributeDescription.AttributeType`

An attribute that stores a uniform resource identifier.

Initializer

# init(rawValue:)

Creates an attribute type using the specified raw value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    init(rawValue: NSAttributeType)

##  Parameters

`rawValue`

    

The raw attribute type. For possible values, see `NSAttributeType`.

## Relationships

### From Protocol

  * `RawRepresentable`

Instance Property

# rawValue

The attribute type’s cardinal value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var rawValue: NSAttributeType

## Relationships

### From Protocol

  * `RawRepresentable`

## See Also

### Getting an Attribute Type’s Raw Value

`typealias NSAttributeDescription.AttributeType.RawValue`

The type the conforming type uses to represent its values.

Type Alias

# NSAttributeDescription.AttributeType.RawValue

The type the conforming type uses to represent its values.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    typealias NSAttributeDescription.AttributeType.RawValue = NSAttributeType

## See Also

### Getting an Attribute Type’s Raw Value

`var rawValue: NSAttributeType`

The attribute type’s cardinal value.

Instance Property

# hashValue

The attribute type’s computed hash value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var hashValue: Int { get }

## See Also

### Hashing an Attribute Type

`func hash(into: inout Hasher)`

Hashes the components of the attribute type using the provided hasher.

Instance Method

# hash(into:)

Hashes the components of the attribute type using the provided hasher.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    func hash(into hasher: inout Hasher)

##  Parameters

`hasher`

    

The hasher to use when combining components of this attribute type.

## See Also

### Hashing an Attribute Type

`var hashValue: Int`

The attribute type’s computed hash value.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    static func != (lhs: NSAttributeDescription.AttributeType, rhs: NSAttributeDescription.AttributeType) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

