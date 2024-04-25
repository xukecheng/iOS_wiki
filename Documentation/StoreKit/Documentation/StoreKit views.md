Instance Method

# productViewStyle(_:)

Sets the style for in-app purchase product views within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func productViewStyle(_ style: some ProductViewStyle) -> some View

##  Parameters

`style`

    

The style to apply to the in-app purchase product views within the view.

## Discussion

This modifier styles any `ProductView` or `StoreView` instances within a view.

Instance Method

# subscriptionStorePickerItemBackground(_:)

Sets the background style for picker items of the subscription store view
instances within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStorePickerItemBackground(_ backgroundStyle: some ShapeStyle) -> some View

## See Also

### Configuring subscription store view controls

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> View`

Sets a view to use to decorate individual subscription options within a
subscription store view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> View`

Configures the subscription store views within a view to use a specified
button label.

`struct SubscriptionStoreButtonLabel`

The label of the subscribe button that a subscription store view uses.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
View`

Sets the control style for subscription store views within a view.

Instance Method

# subscriptionStoreControlStyle(_:)

Sets the control style for subscription store views within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStoreControlStyle(_ style: some SubscriptionStoreControlStyle) -> some View

## Discussion

Modify the control style of the in-app subscription store,
`SubscriptionStoreView`. This has no effect on `StoreView` and `ProductView`
instances.

## See Also

### Styling subscription store views

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> View`

Sets the background style for picker items of the subscription store view
instances within a view.

`protocol SubscriptionStoreControlStyle`

A type that specifies the appearance and interaction of controls in the
subscription store view instances within the view hierarchy.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> View`

Sets a view to use to decorate individual subscription options within a
subscription store view.

`struct SubscriptionStoreControlBackground`

Instance Method

# subscriptionStoreControlIcon(icon:)

Sets a view to use to decorate individual subscription options within a
subscription store view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func subscriptionStoreControlIcon(@ViewBuilder icon: @escaping (Product, Product.SubscriptionInfo) -> some View) -> some View

##  Parameters

`icon`

    

A closure that takes a `Product` and `Product.SubscriptionInfo` and returns a
view.

## Discussion

You can adjust this view to provide a different appearance for each
subscription option.

## See Also

### Configuring subscription store view controls

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> View`

Sets the background style for picker items of the subscription store view
instances within a view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> View`

Configures the subscription store views within a view to use a specified
button label.

`struct SubscriptionStoreButtonLabel`

The label of the subscribe button that a subscription store view uses.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
View`

Sets the control style for subscription store views within a view.

Structure

# ContainerBackgroundPlacement

The placement of a container background.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ContainerBackgroundPlacement

## Overview

This method controls where to place a background that you specify with the
`containerBackground(_:for:)` or `containerBackground(for:alignment:content:)`
modifier.

## Topics

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

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

