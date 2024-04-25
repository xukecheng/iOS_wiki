Type Property

# automatic

A subscription store control style that resolves its appearance automatically,
based on the current context.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var automatic: AutomaticSubscriptionStoreControlStyle { get }

Available when `Self` is `AutomaticSubscriptionStoreControlStyle`.

## Discussion

You can also use `subscriptionStoreControlStyle(_:)`with `automatic` as the
parameter to construct this style.

## See Also

### Getting built-in subscription store view styles

`static var buttons: ButtonsSubscriptionStoreControlStyle`

A subscription store control style that displays a subscribe button for each
subscription plan.

Available when `Self` is `ButtonsSubscriptionStoreControlStyle`.

`static var picker: PickerSubscriptionStoreControlStyle`

A subscription store control style that displays subscription plans as a
picker control, with a single button to subscribe.

Available when `Self` is `PickerSubscriptionStoreControlStyle`.

`static var prominentPicker: ProminentPickerSubscriptionStoreControlStyle`

A subscription store control style that displays subscription plans as a
prominent picker control, with a single button to subscribe.

Available when `Self` is `ProminentPickerSubscriptionStoreControlStyle`.

Type Property

# buttons

A subscription store control style that displays a subscribe button for each
subscription plan.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var buttons: ButtonsSubscriptionStoreControlStyle { get }

Available when `Self` is `ButtonsSubscriptionStoreControlStyle`.

## Discussion

You can also use `subscriptionStoreControlStyle(_:)`with `buttons` as the
parameter to construct this style.

## See Also

### Getting built-in subscription store view styles

`static var automatic: AutomaticSubscriptionStoreControlStyle`

A subscription store control style that resolves its appearance automatically,
based on the current context.

Available when `Self` is `AutomaticSubscriptionStoreControlStyle`.

`static var picker: PickerSubscriptionStoreControlStyle`

A subscription store control style that displays subscription plans as a
picker control, with a single button to subscribe.

Available when `Self` is `PickerSubscriptionStoreControlStyle`.

`static var prominentPicker: ProminentPickerSubscriptionStoreControlStyle`

A subscription store control style that displays subscription plans as a
prominent picker control, with a single button to subscribe.

Available when `Self` is `ProminentPickerSubscriptionStoreControlStyle`.

Type Property

# picker

A subscription store control style that displays subscription plans as a
picker control, with a single button to subscribe.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var picker: PickerSubscriptionStoreControlStyle { get }

Available when `Self` is `PickerSubscriptionStoreControlStyle`.

## Discussion

You can also use `subscriptionStoreControlStyle(_:)`with `picker` as the
parameter to construct this style.

## See Also

### Getting built-in subscription store view styles

`static var automatic: AutomaticSubscriptionStoreControlStyle`

A subscription store control style that resolves its appearance automatically,
based on the current context.

Available when `Self` is `AutomaticSubscriptionStoreControlStyle`.

`static var buttons: ButtonsSubscriptionStoreControlStyle`

A subscription store control style that displays a subscribe button for each
subscription plan.

Available when `Self` is `ButtonsSubscriptionStoreControlStyle`.

`static var prominentPicker: ProminentPickerSubscriptionStoreControlStyle`

A subscription store control style that displays subscription plans as a
prominent picker control, with a single button to subscribe.

Available when `Self` is `ProminentPickerSubscriptionStoreControlStyle`.

Type Property

# prominentPicker

A subscription store control style that displays subscription plans as a
prominent picker control, with a single button to subscribe.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
Xcode 15.0+

    
    
    static var prominentPicker: ProminentPickerSubscriptionStoreControlStyle { get }

Available when `Self` is `ProminentPickerSubscriptionStoreControlStyle`.

## Discussion

You can also use `subscriptionStoreControlStyle(_:)`with `prominentPicker` as
the parameter to construct this style.

## See Also

### Getting built-in subscription store view styles

`static var automatic: AutomaticSubscriptionStoreControlStyle`

A subscription store control style that resolves its appearance automatically,
based on the current context.

Available when `Self` is `AutomaticSubscriptionStoreControlStyle`.

`static var buttons: ButtonsSubscriptionStoreControlStyle`

A subscription store control style that displays a subscribe button for each
subscription plan.

Available when `Self` is `ButtonsSubscriptionStoreControlStyle`.

`static var picker: PickerSubscriptionStoreControlStyle`

A subscription store control style that displays subscription plans as a
picker control, with a single button to subscribe.

Available when `Self` is `PickerSubscriptionStoreControlStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a subscription store control.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of a subscription store control.

## See Also

### Creating custom subscription store views

`typealias SubscriptionStoreControlStyle.Configuration`

A type that represents the properties of a subscription store control.

`struct SubscriptionStoreControlStyleConfiguration`

The properties of a subscription store view control.

`associatedtype Body`

A view that represents the body of a subscription store control.

**Required**

Type Alias

# SubscriptionStoreControlStyle.Configuration

A type that represents the properties of a subscription store control.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias SubscriptionStoreControlStyle.Configuration = SubscriptionStoreControlStyleConfiguration

## See Also

### Creating custom subscription store views

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a subscription store control.

**Required**

` struct SubscriptionStoreControlStyleConfiguration`

The properties of a subscription store view control.

`associatedtype Body`

A view that represents the body of a subscription store control.

**Required**

Structure

# SubscriptionStoreControlStyleConfiguration

The properties of a subscription store view control.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    struct SubscriptionStoreControlStyleConfiguration

## See Also

### Creating custom subscription store views

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a subscription store control.

**Required**

` typealias SubscriptionStoreControlStyle.Configuration`

A type that represents the properties of a subscription store control.

`associatedtype Body`

A view that represents the body of a subscription store control.

**Required**

# Body

A view that represents the body of a subscription store control.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom subscription store views

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a subscription store control.

**Required**

` typealias SubscriptionStoreControlStyle.Configuration`

A type that represents the properties of a subscription store control.

`struct SubscriptionStoreControlStyleConfiguration`

The properties of a subscription store view control.

