Instance Property

# top

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var top: CGFloat

## See Also

### Getting edge insets

`var bottom: CGFloat`

`var leading: CGFloat`

`var trailing: CGFloat`

Instance Property

# bottom

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var bottom: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

`var leading: CGFloat`

`var trailing: CGFloat`

Instance Property

# leading

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var leading: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

`var bottom: CGFloat`

`var trailing: CGFloat`

Instance Property

# trailing

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var trailing: CGFloat

## See Also

### Getting edge insets

`var top: CGFloat`

`var bottom: CGFloat`

`var leading: CGFloat`

Initializer

# init()

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init()

## See Also

### Creating an edge inset

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)`

`init(EdgeInsets3D)`

Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and
`back` values.

`init(NSDirectionalEdgeInsets)`

Create edge insets from the equivalent NSDirectionalEdgeInsets.

Initializer

# init(top:leading:bottom:trailing:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        top: CGFloat,
        leading: CGFloat,
        bottom: CGFloat,
        trailing: CGFloat
    )

## See Also

### Creating an edge inset

`init()`

`init(EdgeInsets3D)`

Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and
`back` values.

`init(NSDirectionalEdgeInsets)`

Create edge insets from the equivalent NSDirectionalEdgeInsets.

Initializer

# init(_:)

Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and
`back` values.

visionOS 1.0+

    
    
    init(_ i: EdgeInsets3D)

## See Also

### Creating an edge inset

`init()`

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)`

`init(NSDirectionalEdgeInsets)`

Create edge insets from the equivalent NSDirectionalEdgeInsets.

Initializer

# init(_:)

Create edge insets from the equivalent NSDirectionalEdgeInsets.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS
1.0+

    
    
    init(_ nsEdgeInsets: NSDirectionalEdgeInsets)

## See Also

### Creating an edge inset

`init()`

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)`

`init(EdgeInsets3D)`

Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and
`back` values.

