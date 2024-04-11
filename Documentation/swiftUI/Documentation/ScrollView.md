Initializer

# init(_:showsIndicators:content:)

Creates a new instance that’s scrollable in the direction of the given axis
and can show indicators while scrolling.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        _ axes: Axis.Set = .vertical,
        showsIndicators: Bool = true,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`axes`

    

The scroll view’s scrollable axis. The default axis is the vertical axis.

`showsIndicators`

    

A Boolean value that indicates whether the scroll view displays the scrollable
component of the content offset, in a way suitable for the platform. The
default value for this parameter is `true`.

`content`

    

The view builder that creates the scrollable view.

## See Also

### Creating a scroll view

`init(Axis.Set, content: () -> Content)`

Creates a new instance that’s scrollable in the direction of the given axis
and can show indicators while scrolling.

Available when `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a new instance that’s scrollable in the direction of the given axis
and can show indicators while scrolling.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ axes: Axis.Set = .vertical,
        @ViewBuilder content: () -> Content
    )

Available when `Content` conforms to `View`.

##  Parameters

`axes`

    

The scroll view’s scrollable axis. The default axis is the vertical axis.

`content`

    

The view builder that creates the scrollable view.

## See Also

### Creating a scroll view

`init(Axis.Set, showsIndicators: Bool, content: () -> Content)`

Creates a new instance that’s scrollable in the direction of the given axis
and can show indicators while scrolling.

Instance Property

# content

The scroll view’s content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var content: Content

## See Also

### Configuring a scroll view

`var axes: Axis.Set`

The scrollable axes of the scroll view.

`var showsIndicators: Bool`

A value that indicates whether the scroll view displays the scrollable
component of the content offset, in a way that’s suitable for the platform.

Instance Property

# axes

The scrollable axes of the scroll view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var axes: Axis.Set { get set }

## Discussion

The default value is `Axis.vertical`.

## See Also

### Configuring a scroll view

`var content: Content`

The scroll view’s content.

`var showsIndicators: Bool`

A value that indicates whether the scroll view displays the scrollable
component of the content offset, in a way that’s suitable for the platform.

Instance Property

# showsIndicators

A value that indicates whether the scroll view displays the scrollable
component of the content offset, in a way that’s suitable for the platform.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var showsIndicators: Bool { get set }

## Discussion

The default is `true`.

## See Also

### Configuring a scroll view

`var content: Content`

The scroll view’s content.

`var axes: Axis.Set`

The scrollable axes of the scroll view.

Instance Property

# body

The content and behavior of the scroll view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var body: some View { get }

