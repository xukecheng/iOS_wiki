Type Property

# automatic

A subscription store control style that resolves its appearance automatically,
based on the current context.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    static var automatic: AutomaticSubscriptionStoreControlStyle { get }

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of an automatic subscription store
control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    func makeBody(configuration: AutomaticSubscriptionStoreControlStyle.Configuration) -> some View

##  Parameters

`configuration`

    

The properties of an automatic subscription store control.

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`typealias AutomaticSubscriptionStoreControlStyle.Body`

A type that represents the body of an automatic subscription store control
style.

`init()`

Creates an automatic subscription store control style.

Type Alias

# AutomaticSubscriptionStoreControlStyle.Body

A type that represents the body of an automatic subscription store control
style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    typealias AutomaticSubscriptionStoreControlStyle.Body = some View

## Relationships

### From Protocol

  * `SubscriptionStoreControlStyle`

## See Also

### Creating the style

`func makeBody(configuration:
AutomaticSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of an automatic subscription store
control style.

`init()`

Creates an automatic subscription store control style.

Initializer

# init()

Creates an automatic subscription store control style.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+
tvOS 17.0+  watchOS 10.0+  visionOS 1.0+  Xcode 15.0+

    
    
    init()

## See Also

### Creating the style

`func makeBody(configuration:
AutomaticSubscriptionStoreControlStyle.Configuration) -> View`

Creates a view that represents the body of an automatic subscription store
control style.

`typealias AutomaticSubscriptionStoreControlStyle.Body`

A type that represents the body of an automatic subscription store control
style.

