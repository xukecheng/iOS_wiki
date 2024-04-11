Type Property

# search

Defines triggers originating from search fields constructed from searchable
modifiers.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let search: SubmitTriggers

## Discussion

In the example below, only the search field or search completions placed by
the searchable modifier will trigger the view model to submit its current
search query.

## See Also

### Getting submit triggers

`static let text: SubmitTriggers`

Defines triggers originating from text input controls like `TextField` and
`SecureField`.

Type Property

# text

Defines triggers originating from text input controls like `TextField` and
`SecureField`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let text: SubmitTriggers

## See Also

### Getting submit triggers

`static let search: SubmitTriggers`

Defines triggers originating from search fields constructed from searchable
modifiers.

Initializer

# init(rawValue:)

Creates a set of submit triggers.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(rawValue: SubmitTriggers.RawValue)

