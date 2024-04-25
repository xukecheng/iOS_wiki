Type Property

# buttons

A subscription store control style that displays a subscribe button for each
subscription plan.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var buttons: ButtonsSubscriptionStoreControlStyle { get }

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button subscription store.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func makeBody(configuration: ButtonsSubscriptionStoreControlStyle.Configuration) -> some View

##  Parameters

`configuration`

    

The properties of a button subscription store control.

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`typealias ButtonsSubscriptionStoreControlStyle.Body`

A type that represents the body of a button subscription store control style.

`init()`

Creates a button subscription store control style.

Type Alias

# ButtonsSubscriptionStoreControlStyle.Body

A type that represents the body of a button subscription store control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias ButtonsSubscriptionStoreControlStyle.Body = some View

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`func makeBody(configuration:
ButtonsSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of a button subscription store.

`init()`

Creates a button subscription store control style.

Initializer

# init()

Creates a button subscription store control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init()

## See Also

### Creating the style

`func makeBody(configuration:
ButtonsSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of a button subscription store.

`typealias ButtonsSubscriptionStoreControlStyle.Body`

A type that represents the body of a button subscription store control style.

