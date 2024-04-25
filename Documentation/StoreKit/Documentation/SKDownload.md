Instance Property

# expectedContentLength

The length of the downloadable content, in bytes.

iOS 13.0–16.0  Deprecated  iPadOS 13.0–16.0  Deprecated  macOS 10.15–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 13.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var expectedContentLength: Int64 { get }

## See Also

### Getting Content Information

`var contentIdentifier: String`

A string that uniquely identifies the downloadable content.

Deprecated

`var contentVersion: String`

A string that identifies which version of the content is available for
download.

Deprecated

`var transaction: SKPaymentTransaction`

The transaction associated with the downloadable file.

Deprecated

`var contentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

Instance Property

# contentIdentifier

A string that uniquely identifies the downloadable content.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var contentIdentifier: String { get }

## Discussion

Each piece of downloadable content associated with a product has its own
unique identifier. The content identifier is specified in App Store Connect
when you add the content.

## See Also

### Getting Content Information

`var expectedContentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

`var contentVersion: String`

A string that identifies which version of the content is available for
download.

Deprecated

`var transaction: SKPaymentTransaction`

The transaction associated with the downloadable file.

Deprecated

`var contentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

### Related Documentation

In-App Purchase Programming Guide

Instance Property

# contentVersion

A string that identifies which version of the content is available for
download.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var contentVersion: String { get }

## Discussion

The version string must be formatted as a series of integers separated by
periods.

## See Also

### Getting Content Information

`var expectedContentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

`var contentIdentifier: String`

A string that uniquely identifies the downloadable content.

Deprecated

`var transaction: SKPaymentTransaction`

The transaction associated with the downloadable file.

Deprecated

`var contentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

Instance Property

# transaction

The transaction associated with the downloadable file.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.11–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var transaction: SKPaymentTransaction { get }

## Discussion

A download object is always associated with a payment transaction. The
download object may only be queued after payment is processed and before the
transaction is finished.

## See Also

### Getting Content Information

`var expectedContentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

`var contentIdentifier: String`

A string that uniquely identifies the downloadable content.

Deprecated

`var contentVersion: String`

A string that identifies which version of the content is available for
download.

Deprecated

`var contentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

Instance Property

# contentLength

The length of the downloadable content, in bytes.

iOS 6.0–13.0  Deprecated  iPadOS 6.0–13.0  Deprecated  macOS 10.8–10.15
Deprecated  Mac Catalyst 13.0–13.0  Deprecated  tvOS 9.0–13.0  Deprecated

**iOS, iPadOS, Mac Catalyst, tvOS**

    
    
     var contentLength: Int64 { get }

**macOS**

    
    
     @NSCopying
    var contentLength: NSNumber { get }

Deprecated

Use `expectedContentLength` instead.

## See Also

### Getting Content Information

`var expectedContentLength: Int64`

The length of the downloadable content, in bytes.

Deprecated

`var contentIdentifier: String`

A string that uniquely identifies the downloadable content.

Deprecated

`var contentVersion: String`

A string that identifies which version of the content is available for
download.

Deprecated

`var transaction: SKPaymentTransaction`

The transaction associated with the downloadable file.

Deprecated

Instance Property

# state

The current state of the download object.

iOS 12.0–16.0  Deprecated  iPadOS 12.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 12.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var state: SKDownloadState { get }

## Discussion

After you queue a download object, the payment queue object calls your
transaction observer when the state of the download object changes. Your
transaction observer should read the `state` property and use it to determine
how to proceed. For more information on the different states, see
`SKDownloadState`.

## See Also

### Getting State Information

`var progress: Float`

A value that indicates how much of the file has been downloaded.

Deprecated

`var timeRemaining: TimeInterval`

An estimated time, in seconds, to finish downloading the content.

Deprecated

`var SKDownloadTimeRemainingUnknown: TimeInterval`

Indicates that the system cannot determine how much time is needed to finish
downloading the content.

Deprecated

`enum SKDownloadState`

The states that a download operation can be in.

Deprecated

`var downloadState: SKDownloadState`

The current state of the download object.

Deprecated

Instance Property

# progress

A value that indicates how much of the file has been downloaded.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var progress: Float { get }

## Discussion

The value of this property is a floating point number between `0.0` and `1.0`,
inclusive, where `0.0` means no data has been download and `1.0` means all the
data has been downloaded. Typically, your app uses the value of this property
to update a user interface element, such as a progress bar, that displays how
much of the file has been downloaded.

Do not use the value of this property to determine whether the download has
completed. Instead, use the `downloadState` property.

## See Also

### Getting State Information

`var state: SKDownloadState`

The current state of the download object.

Deprecated

`var timeRemaining: TimeInterval`

An estimated time, in seconds, to finish downloading the content.

Deprecated

`var SKDownloadTimeRemainingUnknown: TimeInterval`

Indicates that the system cannot determine how much time is needed to finish
downloading the content.

Deprecated

`enum SKDownloadState`

The states that a download operation can be in.

Deprecated

`var downloadState: SKDownloadState`

The current state of the download object.

Deprecated

Instance Property

# timeRemaining

An estimated time, in seconds, to finish downloading the content.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var timeRemaining: TimeInterval { get }

## Discussion

The system attempts to estimate how long it will take to finish downloading
the file. If it cannot create a good estimate, the value of this property is
set to `SKDownloadTimeRemainingUnknown`.

## See Also

### Getting State Information

`var state: SKDownloadState`

The current state of the download object.

Deprecated

`var progress: Float`

A value that indicates how much of the file has been downloaded.

Deprecated

`var SKDownloadTimeRemainingUnknown: TimeInterval`

Indicates that the system cannot determine how much time is needed to finish
downloading the content.

Deprecated

`enum SKDownloadState`

The states that a download operation can be in.

Deprecated

`var downloadState: SKDownloadState`

The current state of the download object.

Deprecated

Global Variable

# SKDownloadTimeRemainingUnknown

Indicates that the system cannot determine how much time is needed to finish
downloading the content.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.14–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var SKDownloadTimeRemainingUnknown: TimeInterval

## See Also

### Getting State Information

`var state: SKDownloadState`

The current state of the download object.

Deprecated

`var progress: Float`

A value that indicates how much of the file has been downloaded.

Deprecated

`var timeRemaining: TimeInterval`

An estimated time, in seconds, to finish downloading the content.

Deprecated

`enum SKDownloadState`

The states that a download operation can be in.

Deprecated

`var downloadState: SKDownloadState`

The current state of the download object.

Deprecated

Instance Property

# downloadState

The current state of the download object.

iOS 6.0–12.0  Deprecated  iPadOS 6.0–12.0  Deprecated  Mac Catalyst 13.1–13.1
Deprecated  tvOS 9.0–12.0  Deprecated

    
    
    var downloadState: SKDownloadState { get }

## Discussion

After you queue a download object, the payment queue object calls your
transaction observer when the state of the download object changes. Your
transaction observer should read the `downloadState` property and use it to
determine how to proceed. For more information on the different states, see
`SKDownloadState`.

## See Also

### Getting State Information

`var state: SKDownloadState`

The current state of the download object.

Deprecated

`var progress: Float`

A value that indicates how much of the file has been downloaded.

Deprecated

`var timeRemaining: TimeInterval`

An estimated time, in seconds, to finish downloading the content.

Deprecated

`var SKDownloadTimeRemainingUnknown: TimeInterval`

Indicates that the system cannot determine how much time is needed to finish
downloading the content.

Deprecated

`enum SKDownloadState`

The states that a download operation can be in.

Deprecated

Instance Property

# error

The error that prevented the content from being downloaded.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var error: (any Error)? { get }

## Discussion

The value of this property is valid only when the `downloadState` property is
set to `SKDownloadState.failed`.

## See Also

### Accessing a Completed Download

`var contentURL: URL?`

The local location of the downloaded file.

Deprecated

Instance Property

# contentURL

The local location of the downloaded file.

iOS 6.0–16.0  Deprecated  iPadOS 6.0–16.0  Deprecated  macOS 10.8–13.0
Deprecated  Mac Catalyst 13.1–16.0  Deprecated  tvOS 9.0–16.0  Deprecated
watchOS 6.2–9.0  Deprecated

    
    
    var contentURL: URL? { get }

## Discussion

The value of this property is valid only when the `downloadState` property is
set to `SKDownloadState.finished`. The URL becomes invalid after the
transaction object associated with the download is finalized.

## See Also

### Accessing a Completed Download

`var error: (any Error)?`

The error that prevented the content from being downloaded.

Deprecated

Type Method

# contentURL(forProductID:)

Returns the local location for the previously downloaded flie.

macOS 10.8–13.0  Deprecated  Mac Catalyst 13.0–16.0  Deprecated

    
    
    class func contentURL(forProductID productID: String) -> URL?

##  Parameters

`productID`

    

The product identifier.

## Return Value

The local location for the previously downloaded flie.

## Discussion

Use this method to locate the content on subsequent launches of your app.

## See Also

### Managing Downloaded Content

`class func deleteContent(forProductID: String)`

Deletes the previously downloaded file.

Deprecated

Type Method

# deleteContent(forProductID:)

Deletes the previously downloaded file.

macOS 10.8–13.0  Deprecated  Mac Catalyst 13.0–16.0  Deprecated

    
    
    class func deleteContent(forProductID productID: String)

##  Parameters

`productID`

    

The product identifier.

## See Also

### Managing Downloaded Content

`class func contentURL(forProductID: String) -> URL?`

Returns the local location for the previously downloaded flie.

Deprecated

