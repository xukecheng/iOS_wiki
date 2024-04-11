Enumeration Case

# NSAttributeType.binaryDataAttributeType

An attribute that stores binary data.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case binaryDataAttributeType = 1000

## See Also

### Attribute types

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.booleanAttributeType

An attribute that stores a Boolean value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case booleanAttributeType = 800

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.compositeAttributeType

An attribute that derives its value by composing other attributes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case compositeAttributeType = 2100

## Discussion

Composite attributes support all attribute types except the following:

  * `NSAttributeType.undefinedAttributeType`

  * `NSAttributeType.objectIDAttributeType`

  * `NSAttributeType.binaryDataAttributeType` (when `allowsExternalBinaryDataStorage` is `true`)

For more information, see `NSCompositeAttributeDescription`.

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.dateAttributeType

An attribute that stores a date.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case dateAttributeType = 900

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.decimalAttributeType

An attribute that stores a decimal value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case decimalAttributeType = 400

## Discussion

Use instances of `NSDecimalNumber` when reading and writing attributes of this
type.

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.doubleAttributeType

An attribute that stores a double value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case doubleAttributeType = 500

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.floatAttributeType

An attribute that stores a float value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case floatAttributeType = 600

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.integer16AttributeType

An attribute that stores a 16-bit signed integer value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case integer16AttributeType = 100

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.integer32AttributeType

An attribute that stores a 32-bit signed integer value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case integer32AttributeType = 200

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.integer64AttributeType

An attribute that stores a 64-bit signed integer value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case integer64AttributeType = 300

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.objectIDAttributeType

An attribute that stores a managed object’s ID.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case objectIDAttributeType = 2000

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.stringAttributeType

An attribute that stores a string.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case stringAttributeType = 700

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.transformableAttributeType

An attribute that uses a value transformer to derive its value.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case transformableAttributeType = 1800

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.undefinedAttributeType

An attribute that doesn’t have an explicit type.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case undefinedAttributeType = 0

## Discussion

Use this attribute type with transient attributues only. Core Data manages the
attribute’s value and registers the necessary undo and redo actions.

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.URIAttributeType

An attribute that stores a uniform resource identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    case URIAttributeType = 1200

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case UUIDAttributeType`

An attribute that stores a universally unique identifier.

Enumeration Case

# NSAttributeType.UUIDAttributeType

An attribute that stores a universally unique identifier.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.1+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    case UUIDAttributeType = 1100

## See Also

### Attribute types

`case binaryDataAttributeType`

An attribute that stores binary data.

`case booleanAttributeType`

An attribute that stores a Boolean value.

`case compositeAttributeType`

An attribute that derives its value by composing other attributes.

`case dateAttributeType`

An attribute that stores a date.

`case decimalAttributeType`

An attribute that stores a decimal value.

`case doubleAttributeType`

An attribute that stores a double value.

`case floatAttributeType`

An attribute that stores a float value.

`case integer16AttributeType`

An attribute that stores a 16-bit signed integer value.

`case integer32AttributeType`

An attribute that stores a 32-bit signed integer value.

`case integer64AttributeType`

An attribute that stores a 64-bit signed integer value.

`case objectIDAttributeType`

An attribute that stores a managed object’s ID.

`case stringAttributeType`

An attribute that stores a string.

`case transformableAttributeType`

An attribute that uses a value transformer to derive its value.

`case undefinedAttributeType`

An attribute that doesn’t have an explicit type.

`case URIAttributeType`

An attribute that stores a uniform resource identifier.

