Type Property

# automatic

The automatic window resizability.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var automatic: WindowResizability { get set }

## Discussion

When you use automatic resizability, SwiftUI applies a resizing strategy
that’s appropriate for the scene type:

  * Windows from `WindowGroup`, `Window`, and `DocumentGroup` scene declarations use the `contentMinSize` strategy.

  * A window from a `Settings` scene declaration uses the `contentSize` strategy.

Automatic resizability is the default if you don’t specify another value using
the `windowResizability(_:)` scene modifier.

## See Also

### Getting the resizability

`static var contentMinSize: WindowResizability`

A window resizability that’s partially derived from the window’s content.

`static var contentSize: WindowResizability`

A window resizability that’s derived from the window’s content.

Type Property

# contentMinSize

A window resizability that’s partially derived from the window’s content.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var contentMinSize: WindowResizability { get set }

## Discussion

Windows that use this resizability have:

  * A minimum size that matches the minimum size of the window’s content.

  * No maximum size.

## See Also

### Getting the resizability

`static var automatic: WindowResizability`

The automatic window resizability.

`static var contentSize: WindowResizability`

A window resizability that’s derived from the window’s content.

Type Property

# contentSize

A window resizability that’s derived from the window’s content.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var contentSize: WindowResizability { get set }

## Discussion

Windows that use this resizability have:

  * A minimum size that matches the minimum size of the window’s content.

  * A maximum size that matches the maximum size of the window’s content.

## See Also

### Getting the resizability

`static var automatic: WindowResizability`

The automatic window resizability.

`static var contentMinSize: WindowResizability`

A window resizability that’s partially derived from the window’s content.

