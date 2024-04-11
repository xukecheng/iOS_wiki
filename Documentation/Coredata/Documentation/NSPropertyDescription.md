Instance Property

# entity

The entity description of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var entity: NSEntityDescription { get }

## See Also

### Accessing Features of a Property

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

### Related Documentation

Core Data Programming Guide

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

Instance Property

# isIndexed

A Boolean value that indicates whether the receiver should be indexed for
searching.

iOS 3.0–11.0  Deprecated  iPadOS 3.0–11.0  Deprecated  macOS 10.5–10.13
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–11.0  Deprecated
watchOS 2.0–4.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    var isIndexed: Bool { get set }

## Discussion

`true` if the receiver should be indexed for searching, otherwise `false`.
Object stores can optionally use this information upon store creation for
operations such as defining indexes.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# isOptional

A Boolean value that indicates whether the receiver is optional.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isOptional: Bool { get set }

## Discussion

`true` if the receiver is optional, otherwise `false`. The optionality flag
specifies whether a property’s value can be `nil` before an object can be
saved to a persistent store.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# isTransient

A Boolean value that indicates whether the receiver is transient.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isTransient: Bool { get set }

## Discussion

`true` if the receiver is transient, otherwise `false`. The transient flag
specifies whether or not a property’s value is ignored when an object is saved
to a persistent store. Transient properties are not saved to the persistent
store, but are still managed for undo, redo, validation, and so on.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# name

The name of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var name: String { get set }

## Discussion

A property name cannot be the same as any no-parameter method name of
`NSObject` or `NSManagedObject`. Since there are hundreds of methods on
`NSObject` which may conflict with property names, you should avoid very
general words (like "font”, and “color”) and words or phrases that overlap
with Cocoa paradigms (such as “isEditing” and “objectSpecifier”).

### Special Considerations

Setting the name raises an exception if the receiver’s model has been used by
an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# userInfo

The user info dictionary of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var userInfo: [AnyHashable : Any]? { get set }

## Discussion

Setting the user info raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

Instance Property

# validationPredicates

The validation predicates of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var validationPredicates: [NSPredicate] { get }

## See Also

### Supporting Validation

`var validationWarnings: [Any]`

The error strings associated with the receiver’s validation predicates.

`func setValidationPredicates([NSPredicate]?, withValidationWarnings:
[String]?)`

Sets the validation predicates and warnings of the receiver.

Instance Property

# validationWarnings

The error strings associated with the receiver’s validation predicates.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var validationWarnings: [Any] { get }

## See Also

### Supporting Validation

`var validationPredicates: [NSPredicate]`

The validation predicates of the receiver.

`func setValidationPredicates([NSPredicate]?, withValidationWarnings:
[String]?)`

Sets the validation predicates and warnings of the receiver.

Instance Method

# setValidationPredicates(_:withValidationWarnings:)

Sets the validation predicates and warnings of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setValidationPredicates(
        _ validationPredicates: [NSPredicate]?,
        withValidationWarnings validationWarnings: [String]?
    )

##  Parameters

`validationPredicates`

    

An array containing the validation predicates for the receiver.

`validationWarnings`

    

An array containing the validation warnings for the receiver.

## Discussion

The `validationPredicates` and `validationWarnings` arrays should contain the
same number of elements, and corresponding elements should appear at the same
index in each array.

Instead of implementing individual validation methods, you can use this method
to provide a list of predicates that are evaluated against the managed objects
and a list of corresponding error messages (which can be localized).

### Special Considerations

This method raises an exception if the receiver’s model has been used by an
object graph manager.

## See Also

### Supporting Validation

`var validationPredicates: [NSPredicate]`

The validation predicates of the receiver.

`var validationWarnings: [Any]`

The error strings associated with the receiver’s validation predicates.

Instance Property

# versionHash

The version hash for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

The version hash is used to uniquely identify a property based on its
configuration. The version hash uses only values which affect the persistence
of data and the user-defined `versionHashModifier` value. (The values which
affect persistence are the name of the property, and the flags for
`isOptional`, `isTransient`, and `isReadOnly`.) This value is stored as part
of the version information in the metadata for stores, as well as a definition
of a property involved in an `NSPropertyMapping` object.

## See Also

### Supporting Versioning

`var versionHashModifier: String?`

The version hash modifier for the receiver.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

Instance Property

# versionHashModifier

The version hash modifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHashModifier: String? { get set }

## Discussion

This value is included in the version hash for the property. You use it to
mark or denote a property as being a different “version” than another even if
all of the values which affect persistence are equal. (Such a difference is
important in cases where the attributes of a property are unchanged but the
format or content of its data are changed.)

## See Also

### Supporting Versioning

`var versionHash: Data`

The version hash for the receiver.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

Instance Property

# renamingIdentifier

The renaming identifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var renamingIdentifier: String? { get set }

## Discussion

This is used to resolve naming conflicts between models. When creating an
entity mapping between entities in two managed object models, a source entity
property and a destination entity property that share the same identifier
indicate that a property mapping should be configured to migrate from the
source to the destination. If unset, the identifier will return the property's
name.

## See Also

### Supporting Versioning

`var versionHash: Data`

The version hash for the receiver.

`var versionHashModifier: String?`

The version hash modifier for the receiver.

Instance Property

# isIndexedBySpotlight

A Boolean value that indicates whether Core Data adds the property’s value to
the Core Spotlight index.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isIndexedBySpotlight: Bool { get set }

## Discussion

Important

If you set this property to `true` for a property description that describes a
relationship, you must override `attributeSet(for:)` in your Core Spotlight
delegate and return the necessary set of attributes. Core Data doesn’t
automatically infer indexable information for relationships.

You can also set this property using the Index in Spotlight attribute in the
Attributes inspector of the Core Data model editor.

## See Also

### Specifying Spotlight Support

`var isStoredInExternalRecord: Bool`

A Boolean value that indicates whether to write the property’s data in an
external record file that corresponds to the managed object.

Deprecated

Instance Property

# isStoredInExternalRecord

A Boolean value that indicates whether to write the property’s data in an
external record file that corresponds to the managed object.

iOS 3.0–11.0  Deprecated  iPadOS 3.0–11.0  Deprecated  macOS 10.6–10.13
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–11.0  Deprecated
watchOS 2.0–4.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    var isStoredInExternalRecord: Bool { get set }

## Discussion

`true` if the property data should be written out in an external record file
corresponding to the managed object, otherwise `false`. For additional
information, see Core Data Spotlight Integration Programming Guide.

### Special Considerations

This property has no effect on iOS.

## See Also

### Specifying Spotlight Support

`var isIndexedBySpotlight: Bool`

A Boolean value that indicates whether Core Data adds the property’s value to
the Core Spotlight index.

Instance Property

# entity

The entity description of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var entity: NSEntityDescription { get }

## See Also

### Accessing Features of a Property

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

### Related Documentation

Core Data Programming Guide

`var properties: [NSPropertyDescription]`

An array containing the properties of the receiver.

Instance Property

# isIndexed

A Boolean value that indicates whether the receiver should be indexed for
searching.

iOS 3.0–11.0  Deprecated  iPadOS 3.0–11.0  Deprecated  macOS 10.5–10.13
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–11.0  Deprecated
watchOS 2.0–4.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    var isIndexed: Bool { get set }

## Discussion

`true` if the receiver should be indexed for searching, otherwise `false`.
Object stores can optionally use this information upon store creation for
operations such as defining indexes.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# isOptional

A Boolean value that indicates whether the receiver is optional.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isOptional: Bool { get set }

## Discussion

`true` if the receiver is optional, otherwise `false`. The optionality flag
specifies whether a property’s value can be `nil` before an object can be
saved to a persistent store.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# isTransient

A Boolean value that indicates whether the receiver is transient.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isTransient: Bool { get set }

## Discussion

`true` if the receiver is transient, otherwise `false`. The transient flag
specifies whether or not a property’s value is ignored when an object is saved
to a persistent store. Transient properties are not saved to the persistent
store, but are still managed for undo, redo, validation, and so on.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var name: String`

The name of the receiver.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# name

The name of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var name: String { get set }

## Discussion

A property name cannot be the same as any no-parameter method name of
`NSObject` or `NSManagedObject`. Since there are hundreds of methods on
`NSObject` which may conflict with property names, you should avoid very
general words (like "font”, and “color”) and words or phrases that overlap
with Cocoa paradigms (such as “isEditing” and “objectSpecifier”).

### Special Considerations

Setting the name raises an exception if the receiver’s model has been used by
an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var userInfo: [AnyHashable : Any]?`

The user info dictionary of the receiver.

Instance Property

# userInfo

The user info dictionary of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var userInfo: [AnyHashable : Any]? { get set }

## Discussion

Setting the user info raises an exception if the receiver’s model has been
used by an object graph manager.

## See Also

### Accessing Features of a Property

`var entity: NSEntityDescription`

The entity description of the receiver.

`var isIndexed: Bool`

A Boolean value that indicates whether the receiver should be indexed for
searching.

Deprecated

`var isOptional: Bool`

A Boolean value that indicates whether the receiver is optional.

`var isTransient: Bool`

A Boolean value that indicates whether the receiver is transient.

`var name: String`

The name of the receiver.

Instance Property

# validationPredicates

The validation predicates of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var validationPredicates: [NSPredicate] { get }

## See Also

### Supporting Validation

`var validationWarnings: [Any]`

The error strings associated with the receiver’s validation predicates.

`func setValidationPredicates([NSPredicate]?, withValidationWarnings:
[String]?)`

Sets the validation predicates and warnings of the receiver.

Instance Property

# validationWarnings

The error strings associated with the receiver’s validation predicates.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var validationWarnings: [Any] { get }

## See Also

### Supporting Validation

`var validationPredicates: [NSPredicate]`

The validation predicates of the receiver.

`func setValidationPredicates([NSPredicate]?, withValidationWarnings:
[String]?)`

Sets the validation predicates and warnings of the receiver.

Instance Method

# setValidationPredicates(_:withValidationWarnings:)

Sets the validation predicates and warnings of the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setValidationPredicates(
        _ validationPredicates: [NSPredicate]?,
        withValidationWarnings validationWarnings: [String]?
    )

##  Parameters

`validationPredicates`

    

An array containing the validation predicates for the receiver.

`validationWarnings`

    

An array containing the validation warnings for the receiver.

## Discussion

The `validationPredicates` and `validationWarnings` arrays should contain the
same number of elements, and corresponding elements should appear at the same
index in each array.

Instead of implementing individual validation methods, you can use this method
to provide a list of predicates that are evaluated against the managed objects
and a list of corresponding error messages (which can be localized).

### Special Considerations

This method raises an exception if the receiver’s model has been used by an
object graph manager.

## See Also

### Supporting Validation

`var validationPredicates: [NSPredicate]`

The validation predicates of the receiver.

`var validationWarnings: [Any]`

The error strings associated with the receiver’s validation predicates.

Instance Property

# versionHash

The version hash for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHash: Data { get }

## Discussion

The version hash is used to uniquely identify a property based on its
configuration. The version hash uses only values which affect the persistence
of data and the user-defined `versionHashModifier` value. (The values which
affect persistence are the name of the property, and the flags for
`isOptional`, `isTransient`, and `isReadOnly`.) This value is stored as part
of the version information in the metadata for stores, as well as a definition
of a property involved in an `NSPropertyMapping` object.

## See Also

### Supporting Versioning

`var versionHashModifier: String?`

The version hash modifier for the receiver.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

Instance Property

# versionHashModifier

The version hash modifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var versionHashModifier: String? { get set }

## Discussion

This value is included in the version hash for the property. You use it to
mark or denote a property as being a different “version” than another even if
all of the values which affect persistence are equal. (Such a difference is
important in cases where the attributes of a property are unchanged but the
format or content of its data are changed.)

## See Also

### Supporting Versioning

`var versionHash: Data`

The version hash for the receiver.

`var renamingIdentifier: String?`

The renaming identifier for the receiver.

Instance Property

# renamingIdentifier

The renaming identifier for the receiver.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var renamingIdentifier: String? { get set }

## Discussion

This is used to resolve naming conflicts between models. When creating an
entity mapping between entities in two managed object models, a source entity
property and a destination entity property that share the same identifier
indicate that a property mapping should be configured to migrate from the
source to the destination. If unset, the identifier will return the property's
name.

## See Also

### Supporting Versioning

`var versionHash: Data`

The version hash for the receiver.

`var versionHashModifier: String?`

The version hash modifier for the receiver.

Instance Property

# isIndexedBySpotlight

A Boolean value that indicates whether Core Data adds the property’s value to
the Core Spotlight index.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isIndexedBySpotlight: Bool { get set }

## Discussion

Important

If you set this property to `true` for a property description that describes a
relationship, you must override `attributeSet(for:)` in your Core Spotlight
delegate and return the necessary set of attributes. Core Data doesn’t
automatically infer indexable information for relationships.

You can also set this property using the Index in Spotlight attribute in the
Attributes inspector of the Core Data model editor.

## See Also

### Specifying Spotlight Support

`var isStoredInExternalRecord: Bool`

A Boolean value that indicates whether to write the property’s data in an
external record file that corresponds to the managed object.

Deprecated

Instance Property

# isStoredInExternalRecord

A Boolean value that indicates whether to write the property’s data in an
external record file that corresponds to the managed object.

iOS 3.0–11.0  Deprecated  iPadOS 3.0–11.0  Deprecated  macOS 10.6–10.13
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–11.0  Deprecated
watchOS 2.0–4.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    var isStoredInExternalRecord: Bool { get set }

## Discussion

`true` if the property data should be written out in an external record file
corresponding to the managed object, otherwise `false`. For additional
information, see Core Data Spotlight Integration Programming Guide.

### Special Considerations

This property has no effect on iOS.

## See Also

### Specifying Spotlight Support

`var isIndexedBySpotlight: Bool`

A Boolean value that indicates whether Core Data adds the property’s value to
the Core Spotlight index.

