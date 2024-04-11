Type Property

# discarded

The handler discarded the URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let discarded: OpenURLAction.Result

## Discussion

The action invokes its completion handler with `false` when your handler
returns this value.

## See Also

### Getting the results

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

Type Property

# handled

The handler opened the URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let handled: OpenURLAction.Result

## Discussion

The action invokes its completion handler with `true` when your handler
returns this value.

## See Also

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

Type Property

# systemAction

The handler asks the system to open the original URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let systemAction: OpenURLAction.Result

## Discussion

The action invokes its completion handler with a value that depends on the
outcome of the system’s attempt to open the URL.

## See Also

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static func systemAction(URL) -> OpenURLAction.Result`

The handler asks the system to open the modified URL.

Type Method

# systemAction(_:)

The handler asks the system to open the modified URL.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static func systemAction(_ url: URL) -> OpenURLAction.Result

##  Parameters

`url`

    

The URL that the handler asks the system to open.

## Discussion

The action invokes its completion handler with a value that depends on the
outcome of the system’s attempt to open the URL.

## See Also

### Getting the results

`static let discarded: OpenURLAction.Result`

The handler discarded the URL.

`static let handled: OpenURLAction.Result`

The handler opened the URL.

`static let systemAction: OpenURLAction.Result`

The handler asks the system to open the original URL.

