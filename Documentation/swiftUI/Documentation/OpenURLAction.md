Initializer

# init(handler:)

Creates an action that opens a URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(handler: @escaping (URL) -> OpenURLAction.Result)

##  Parameters

`handler`

    

The closure to run for the given URL. The closure takes a URL as input, and
returns a `OpenURLAction.Result` that indicates the outcome of the action.

## Discussion

Use this initializer to create a custom action for opening URLs. Provide a
handler that takes a URL and returns an `OpenURLAction.Result`. Place your
handler in the environment using the `environment(_:_:)` view modifier:

Any views that read the action from the environment, including the built-in
`Link` view and `Text` views with markdown links, or links in attributed
strings, use your action.

SwiftUI translates the value that your custom action’s handler returns into an
appropriate Boolean result for the action call. For example, a view that uses
the action declared above receives `true` when calling the action, because the
handler always returns `handled`.

## See Also

### Creating the action

`struct Result`

The result of a custom open URL action.

Structure

# OpenURLAction.Result

The result of a custom open URL action.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct Result

## Overview

If you declare a custom `OpenURLAction` in the `Environment`, return one of
the result values from its handler.

  * Use `handled` to indicate that the handler opened the URL.

  * Use `discarded` to indicate that the handler discarded the URL.

  * Use `systemAction` without an argument to ask SwiftUI to open the URL with the system handler.

  * Use `systemAction(_:)` with a URL argument to ask SwiftUI to open the specified URL with the system handler.

You can use the last option to transform URLs, while still relying on the
system to open the URL. For example, you could append a path component to
every URL:

## Topics

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

## See Also

### Creating the action

`init(handler: (URL) -> OpenURLAction.Result)`

Creates an action that opens a URL.

Instance Method

# callAsFunction(_:)

Opens a URL, following system conventions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func callAsFunction(_ url: URL)

##  Parameters

`url`

    

The URL to open.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`OpenURLAction` structure that you get from the `Environment`, using a URL as
an argument:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(URL, completion: (Bool) -> Void)`

Asynchronously opens a URL, following system conventions.

Instance Method

# callAsFunction(_:completion:)

Asynchronously opens a URL, following system conventions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS
1.0+

    
    
    func callAsFunction(
        _ url: URL,
        completion: @escaping (Bool) -> Void
    )

##  Parameters

`url`

    

The URL to open.

`completion`

    

A closure the method calls after determining if it can open the URL, but
possibly before fully opening the URL. The closure takes a Boolean value that
indicates whether the method can open the URL.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the
`OpenURLAction` structure that you get from the `Environment`, using a URL and
a completion handler as arguments:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.

## See Also

### Calling the action

`func callAsFunction(URL)`

Opens a URL, following system conventions.

