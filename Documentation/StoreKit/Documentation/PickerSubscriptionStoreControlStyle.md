Type Property

# picker

A subscription store control style that displays subscription plans as a
picker control, with a single button to subscribe.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var picker: PickerSubscriptionStoreControlStyle { get }

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a picker subscription store.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func makeBody(configuration: PickerSubscriptionStoreControlStyle.Configuration) -> some View

##  Parameters

`configuration`

    

The properties of a picker subscription store control.

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`typealias PickerSubscriptionStoreControlStyle.Body`

A type that represents the body of a picker subscription store control style.

`init()`

Creates a picker subscription store control style.

Type Alias

# PickerSubscriptionStoreControlStyle.Body

A type that represents the body of a picker subscription store control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias PickerSubscriptionStoreControlStyle.Body = some View

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`func makeBody(configuration:
PickerSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of a picker subscription store.

`init()`

Creates a picker subscription store control style.

Initializer

# init()

Creates a picker subscription store control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init()

## See Also

### Creating the style

`func makeBody(configuration:
PickerSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of a picker subscription store.

`typealias PickerSubscriptionStoreControlStyle.Body`

A type that represents the body of a picker subscription store control style.

