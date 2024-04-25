Type Property

# messages

The asynchronous sequence that sends a message when the App Store creates it.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static var messages: Message.Messages { get }

## Discussion

If your app doesn’t implement this message listener, StoreKit retrieves any
messages from the App Store each time your app launches, and presents them by
default.

For more information about listening for and displaying messages, see
`Message`.

## See Also

### Getting messages and message reasons

`let reason: Message.Reason`

The reason that the App Store sends the message.

`struct Message.Messages`

An asynchronous sequence of messages from the App Store.

`struct Message.Reason`

Reasons for the App Store messages.

Instance Property

# reason

The reason that the App Store sends the message.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    let reason: Message.Reason

## See Also

### Getting messages and message reasons

`static var messages: Message.Messages`

The asynchronous sequence that sends a message when the App Store creates it.

`struct Message.Messages`

An asynchronous sequence of messages from the App Store.

`struct Message.Reason`

Reasons for the App Store messages.

Instance Method

# display(in:)

Requests the system to display the App Store message in the window scene.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    @MainActor
    func display(in scene: UIWindowScene) throws

##  Parameters

`scene`

    

The `UIWindowScene` that StoreKit uses to display the App Store message.

## Discussion

The system displays the message if the message is applicable; for example, if
the user has previously seen the same App Store message, the system may
determine whether to display the message again.

Note

If your app uses SwiftUI views, use `DisplayMessageAction` instead of
`display(in:)`.

For more information about using `display(in:)`, see `Message`.

Operator

# !=(_:_:)

Returns a Boolean value indicating whether two values are not equal.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func != (lhs: Message, rhs: Message) -> Bool

##  Parameters

`lhs`

    

A value to compare.

`rhs`

    

Another value to compare.

## Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b`
implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any
type that conforms to `Equatable`.

## See Also

### Comparing and hashing messages

`static func == (Message, Message) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Operator

# ==(_:_:)

Returns a Boolean value that indicates whether two values are equal.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    static func == (lhs: Message, rhs: Message) -> Bool

## See Also

### Comparing and hashing messages

`static func != (Message, Message) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

`var hashValue: Int`

The hash value.

Instance Method

# hash(into:)

Hashes the essential components of the value by feeding them into the given
hasher.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    func hash(into hasher: inout Hasher)

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing messages

`static func != (Message, Message) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Message, Message) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`var hashValue: Int`

The hash value.

Instance Property

# hashValue

The hash value.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+  Xcode 14.0+

    
    
    var hashValue: Int { get }

## Relationships

### From Protocol

  * `Hashable`

## See Also

### Comparing and hashing messages

`static func != (Message, Message) -> Bool`

Returns a Boolean value indicating whether two values are not equal.

`static func == (Message, Message) -> Bool`

Returns a Boolean value that indicates whether two values are equal.

`func hash(into: inout Hasher)`

Hashes the essential components of the value by feeding them into the given
hasher.

