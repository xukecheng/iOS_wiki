Type Property

# navigation

A background placement inside a `NavigationStack` or `NavigationSplitView`

watchOS 10.0+

    
    
    static let navigation: ContainerBackgroundPlacement

## See Also

### Getting placements

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

Type Property

# tabView

A background placement inside a `TabView`.

watchOS 10.0+

    
    
    static let tabView: ContainerBackgroundPlacement

## See Also

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

Type Property

# widget

The container background placement for a widget.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.0+
visionOS 1.0+

    
    
    static let widget: ContainerBackgroundPlacement

## Discussion

Pass the container background placement to the `containerBackground(_:for:)`
function to configure the background of your widgets.

## See Also

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

Type Property

# subscriptionStore

A background placement inside a `SubscriptionStoreView`.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+

    
    
    static var subscriptionStore: ContainerBackgroundPlacement { get }

## See Also

### Getting StoreKit placements

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

Type Property

# subscriptionStoreFullHeight

A background placement that spans the full height of a
`SubscriptionStoreView`.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+

    
    
    static var subscriptionStoreFullHeight: ContainerBackgroundPlacement { get }

## See Also

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

Type Property

# subscriptionStoreHeader

A background placement inside the marketing content of a
`SubscriptionStoreView`

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    static var subscriptionStoreHeader: ContainerBackgroundPlacement { get }

## See Also

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.

