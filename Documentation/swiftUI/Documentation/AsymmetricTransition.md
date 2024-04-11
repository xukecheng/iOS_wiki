Initializer

# init(insertion:removal:)

Creates a composite `Transition` that uses a different transition for
insertion versus removal.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        insertion: Insertion,
        removal: Removal
    )

Instance Property

# insertion

The `Transition` defining the insertion phase of `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var insertion: Insertion

## See Also

### Getting transition properties

`var removal: Removal`

The `Transition` defining the removal phase of `self`.

Instance Property

# removal

The `Transition` defining the removal phase of `self`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var removal: Removal

## See Also

### Getting transition properties

`var insertion: Insertion`

The `Transition` defining the insertion phase of `self`.

