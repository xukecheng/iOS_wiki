Instance Property

# attributeValueClassName

The class name that represents the attribute’s value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var attributeValueClassName: String? { get set }

## See Also

### Managing the type

`var type: NSAttributeDescription.AttributeType`

The attribute’s type.

`struct NSAttributeDescription.AttributeType`

The types of attributes that Core Data supports.

Instance Property

# type

The attribute’s type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var type: NSAttributeDescription.AttributeType { get set }

## Discussion

Don’t change an attribute’s type after you add its containing managed object
model to a persistent store coordinator; otherwise, Core Data throws an
exception.

## See Also

### Managing the type

`var attributeValueClassName: String?`

The class name that represents the attribute’s value.

`struct NSAttributeDescription.AttributeType`

The types of attributes that Core Data supports.

Instance Property

# allowsCloudEncryption

A Boolean value that determines whether to encrypt the attribute’s value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var allowsCloudEncryption: Bool { get set }

## Discussion

Set this property to `true` to store the attribute’s value in an encrypted
form in iCloud. Only use this property with new attributes. Core Data doesn’t
support encrypting attributes that already exist in your CloudKit schema, or
attributes that represent relationships between entities.

You can also set this property using the Allow Cloud Encryption attribute in
the Attributes inspector of the Core Data model editor.

Important

Attributes can’t change their encryption state after you promote them to your
production CloudKit schema. If you choose to encrypt an attribute, it always
remains that way.

## See Also

### Configuring the behavior

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var defaultValue: Any?`

The default value of the attribute.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# allowsExternalBinaryDataStorage

A Boolean value that indicates whether the attribute allows external binary
storage.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var allowsExternalBinaryDataStorage: Bool { get set }

## Discussion

`true` if the attribute allows external binary storage, otherwise `false`. If
this value is `true`, the corresponding attribute may be stored in a file
external to the persistent store itself.

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var defaultValue: Any?`

The default value of the attribute.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# defaultValue

The default value of the attribute.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var defaultValue: Any? { get set }

## Discussion

Default values are retained by a managed object model, not copied. This means
that attribute values do not have to implement the `NSCopying` protocol,
however it also means that you should not modify any objects after they have
been set as default values.

### Special Considerations

Setting the default value raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# preservesValueInHistoryOnDeletion

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var preservesValueInHistoryOnDeletion: Bool { get set }

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var defaultValue: Any?`

The default value of the attribute.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# valueTransformerName

The name of the transformer to use for the attribute value.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var valueTransformerName: String? { get set }

## Discussion

The attribute must be of type `NSTransformedAttributeType`.

The transformer must output an `NSData` object from `transformedValue(_:)` and
must allow reverse transformations.

If this value is `nil`, Core Data uses a default a transformer that uses
`NSCoding` to archive and unarchive the attribute value.

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var defaultValue: Any?`

The default value of the attribute.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

Instance Property

# versionHash

The version hash for the attribute.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

The version hash is used to uniquely identify an attribute based on its
configuration. This value includes the `versionHash` information from
`NSPropertyDescription` and the attribute type.

## See Also

### Related Documentation

`var versionHash: Data`

The version hash for the receiver.

Instance Property

# attributeValueClassName

The class name that represents the attribute’s value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var attributeValueClassName: String? { get set }

## See Also

### Managing the type

`var type: NSAttributeDescription.AttributeType`

The attribute’s type.

`struct NSAttributeDescription.AttributeType`

The types of attributes that Core Data supports.

Instance Property

# type

The attribute’s type.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+  Xcode 13.0+

    
    
    var type: NSAttributeDescription.AttributeType { get set }

## Discussion

Don’t change an attribute’s type after you add its containing managed object
model to a persistent store coordinator; otherwise, Core Data throws an
exception.

## See Also

### Managing the type

`var attributeValueClassName: String?`

The class name that represents the attribute’s value.

`struct NSAttributeDescription.AttributeType`

The types of attributes that Core Data supports.

Instance Property

# allowsCloudEncryption

A Boolean value that determines whether to encrypt the attribute’s value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var allowsCloudEncryption: Bool { get set }

## Discussion

Set this property to `true` to store the attribute’s value in an encrypted
form in iCloud. Only use this property with new attributes. Core Data doesn’t
support encrypting attributes that already exist in your CloudKit schema, or
attributes that represent relationships between entities.

You can also set this property using the Allow Cloud Encryption attribute in
the Attributes inspector of the Core Data model editor.

Important

Attributes can’t change their encryption state after you promote them to your
production CloudKit schema. If you choose to encrypt an attribute, it always
remains that way.

## See Also

### Configuring the behavior

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var defaultValue: Any?`

The default value of the attribute.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# allowsExternalBinaryDataStorage

A Boolean value that indicates whether the attribute allows external binary
storage.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var allowsExternalBinaryDataStorage: Bool { get set }

## Discussion

`true` if the attribute allows external binary storage, otherwise `false`. If
this value is `true`, the corresponding attribute may be stored in a file
external to the persistent store itself.

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var defaultValue: Any?`

The default value of the attribute.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# defaultValue

The default value of the attribute.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var defaultValue: Any? { get set }

## Discussion

Default values are retained by a managed object model, not copied. This means
that attribute values do not have to implement the `NSCopying` protocol,
however it also means that you should not modify any objects after they have
been set as default values.

### Special Considerations

Setting the default value raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# preservesValueInHistoryOnDeletion

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.1+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var preservesValueInHistoryOnDeletion: Bool { get set }

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var defaultValue: Any?`

The default value of the attribute.

`var valueTransformerName: String?`

The name of the transformer to use for the attribute value.

Instance Property

# valueTransformerName

The name of the transformer to use for the attribute value.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var valueTransformerName: String? { get set }

## Discussion

The attribute must be of type `NSTransformedAttributeType`.

The transformer must output an `NSData` object from `transformedValue(_:)` and
must allow reverse transformations.

If this value is `nil`, Core Data uses a default a transformer that uses
`NSCoding` to archive and unarchive the attribute value.

## See Also

### Configuring the behavior

`var allowsCloudEncryption: Bool`

A Boolean value that determines whether to encrypt the attribute’s value.

`var allowsExternalBinaryDataStorage: Bool`

A Boolean value that indicates whether the attribute allows external binary
storage.

`var defaultValue: Any?`

The default value of the attribute.

`var preservesValueInHistoryOnDeletion: Bool`

A Boolean value that indicates whether the attribute records its value in the
persistent history transaction for a managed object’s deletion.

Instance Property

# versionHash

The version hash for the attribute.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

The version hash is used to uniquely identify an attribute based on its
configuration. This value includes the `versionHash` information from
`NSPropertyDescription` and the attribute type.

## See Also

### Related Documentation

`var versionHash: Data`

The version hash for the receiver.

