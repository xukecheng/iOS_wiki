Initializer

# init(content:publisher:action:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        content: Content,
        publisher: PublisherType,
        action: @escaping (PublisherType.Output) -> Void
    )

Instance Property

# publisher

The `Publisher` that is being subscribed.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var publisher: PublisherType

## See Also

### Managing the subscription

`var action: (PublisherType.Output) -> Void`

The `Action` executed when `publisher` emits an event.

`var content: Content`

The content view.

Instance Property

# action

The `Action` executed when `publisher` emits an event.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var action: (PublisherType.Output) -> Void

## See Also

### Managing the subscription

`var publisher: PublisherType`

The `Publisher` that is being subscribed.

`var content: Content`

The content view.

Instance Property

# content

The content view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var content: Content

## See Also

### Managing the subscription

`var publisher: PublisherType`

The `Publisher` that is being subscribed.

`var action: (PublisherType.Output) -> Void`

The `Action` executed when `publisher` emits an event.

