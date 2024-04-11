Type Property

# appRefresh

A task that updates your app’s state in the background.

watchOS 9.0+

    
    
    static var appRefresh: BackgroundTask<String?, Void> { get }

## See Also

### Refreshing the app

`static func appRefresh(String) -> BackgroundTask<Void, Void>`

A task that updates your app’s state in the background for a matching
identifier.

Type Method

# appRefresh(_:)

A task that updates your app’s state in the background for a matching
identifier.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static func appRefresh(_ identifier: String) -> BackgroundTask<Void, Void>

##  Parameters

`matching`

    

The identifier to match.

## Return Value

A background task that you can handle with your app or extension.

## See Also

### Refreshing the app

`static var appRefresh: BackgroundTask<String?, Void>`

A task that updates your app’s state in the background.

Type Property

# snapshot

A background task used to update your app’s user interface in preparation for
a snapshot.

watchOS 9.0+

    
    
    static var snapshot: BackgroundTask<SnapshotData, SnapshotResponse> { get }

Type Property

# bluetoothAlert

A background task used to receive critical alerts from paired bluetooth
accessories.

watchOS 9.0+

    
    
    static var bluetoothAlert: BackgroundTask<Void, Void> { get }

## See Also

### Receiving connectivity updates

`static var watchConnectivity: BackgroundTask<Void, Void>`

A background task used to receive background updates from the Watch
Connectivity framework.

Type Property

# watchConnectivity

A background task used to receive background updates from the Watch
Connectivity framework.

watchOS 9.0+

    
    
    static var watchConnectivity: BackgroundTask<Void, Void> { get }

## See Also

### Receiving connectivity updates

`static var bluetoothAlert: BackgroundTask<Void, Void>`

A background task used to receive critical alerts from paired bluetooth
accessories.

Type Property

# urlSession

A task that responds to background URL sessions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var urlSession: BackgroundTask<String, Void> { get }

## See Also

### Responding to URL sessions

`static func urlSession(String) -> BackgroundTask<Void, Void>`

A task that responds to background URL sessions matching the given identifier.

`static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String,
Void>`

A task that responds to background URL sessions matching the given predicate.

Type Method

# urlSession(_:)

A task that responds to background URL sessions matching the given identifier.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func urlSession(_ identifier: String) -> BackgroundTask<Void, Void>

##  Parameters

`identifier`

    

The identifier to match.

## Return Value

A background task that you can handle with your app or extension.

## See Also

### Responding to URL sessions

`static var urlSession: BackgroundTask<String, Void>`

A task that responds to background URL sessions.

`static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String,
Void>`

A task that responds to background URL sessions matching the given predicate.

Type Method

# urlSession(matching:)

A task that responds to background URL sessions matching the given predicate.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func urlSession(matching: @escaping (String) -> Bool) -> BackgroundTask<String, Void>

##  Parameters

`matching`

    

The predicate to match.

## Return Value

A background task that you can handle with your app or extension.

## See Also

### Responding to URL sessions

`static var urlSession: BackgroundTask<String, Void>`

A task that responds to background URL sessions.

`static func urlSession(String) -> BackgroundTask<Void, Void>`

A task that responds to background URL sessions matching the given identifier.

Type Property

# intentDidRun

A background task used to update your app after a SiriKit intent runs.

watchOS 9.0+

    
    
    static var intentDidRun: BackgroundTask<Void, Void> { get }

## See Also

### Updating intents and shortcuts

`static var relevantShortcut: BackgroundTask<Void, Void>`

A background task used to periodically donate relevant Siri shortcuts.

Type Property

# relevantShortcut

A background task used to periodically donate relevant Siri shortcuts.

watchOS 9.0+

    
    
    static var relevantShortcut: BackgroundTask<Void, Void> { get }

## See Also

### Updating intents and shortcuts

`static var intentDidRun: BackgroundTask<Void, Void>`

A background task used to update your app after a SiriKit intent runs.

