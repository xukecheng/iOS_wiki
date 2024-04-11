Instance Property

# id

The value that all entities in the section share for a specified key path.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    let id: SectionIdentifier

## Discussion

Specify the key path that the entities share this value with by setting the
`SectionedFetchRequest` instance’s `sectionIdentifier` parameter during
initialization, or by modifying the corresponding `SectionedFetchResults`
instance’s `sectionIdentifier` property.

Instance Property

# startIndex

The index of the first entity in the section.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var startIndex: Int { get }

## See Also

### Getting indices

`var endIndex: Int`

The index that’s one greater than that of the last entity in the section.

Instance Property

# endIndex

The index that’s one greater than that of the last entity in the section.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var endIndex: Int { get }

## See Also

### Getting indices

`var startIndex: Int`

The index of the first entity in the section.

Instance Subscript

# subscript(_:)

Gets the entity at the specified index within the section.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    subscript(position: Int) -> Result { get }

