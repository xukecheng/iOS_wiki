Type Property

# intrinsicContentSize

The hosting controller’s view automatically invalidate its intrinsic content
size when its ideal size changes.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    static let intrinsicContentSize: UIHostingControllerSizingOptions

## Discussion

Use this option when the hosting controller’s view is being laid out with Auto
Layout.

Note

This option comes with a performance cost because it asks for the ideal size
of the content using the `unspecified` size proposal.

## See Also

### Getting sizing options

`static let preferredContentSize: UIHostingControllerSizingOptions`

The hosting controller tracks its content’s ideal size in its preferred
content size.

Type Property

# preferredContentSize

The hosting controller tracks its content’s ideal size in its preferred
content size.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    static let preferredContentSize: UIHostingControllerSizingOptions

## Discussion

Use this option when using a hosting controller with a container view
controller that requires up-to-date knowledge of the hosting controller’s
ideal size.

Note

This option comes with a performance cost because it asks for the ideal size
of the content using the `unspecified` size proposal.

## See Also

### Getting sizing options

`static let intrinsicContentSize: UIHostingControllerSizingOptions`

The hosting controller’s view automatically invalidate its intrinsic content
size when its ideal size changes.

Initializer

# init(rawValue:)

Creates a new option set from a raw value.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init(rawValue: Int)

## See Also

### Creating a sizing option

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 6.0+
visionOS 1.0+

    
    
    let rawValue: Int

## See Also

### Creating a sizing option

`init(rawValue: Int)`

Creates a new option set from a raw value.

