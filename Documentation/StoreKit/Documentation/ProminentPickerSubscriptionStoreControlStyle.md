Type Property

# prominentPicker

A subscription store control style that displays subscription plans as a
prominent picker control, with a single button to subscribe.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
Xcode 15.0+

    
    
    static var prominentPicker: ProminentPickerSubscriptionStoreControlStyle { get }

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a prominent picker subscription
store.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
Xcode 15.0+

    
    
    func makeBody(configuration: ProminentPickerSubscriptionStoreControlStyle.Configuration) -> some View

##  Parameters

`configuration`

    

The properties of a prominent picker subscription store control.

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`typealias ProminentPickerSubscriptionStoreControlStyle.Body`

A type that represents the body of a prominent picker subscription store
control style.

`init()`

Creates a prominent picker subscription store control style.

Type Alias

# ProminentPickerSubscriptionStoreControlStyle.Body

A type that represents the body of a prominent picker subscription store
control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
Xcode 15.0+

    
    
    typealias ProminentPickerSubscriptionStoreControlStyle.Body = some View

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`func makeBody(configuration:
ProminentPickerSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of a prominent picker subscription
store.

`init()`

Creates a prominent picker subscription store control style.

Initializer

# init()

Creates a prominent picker subscription store control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
Xcode 15.0+

    
    
    init()

## See Also

### Creating the style

`func makeBody(configuration:
ProminentPickerSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of a prominent picker subscription
store.

`typealias ProminentPickerSubscriptionStoreControlStyle.Body`

A type that represents the body of a prominent picker subscription store
control style.

