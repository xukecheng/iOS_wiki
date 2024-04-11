Type Method

# default(_:action:)

Creates an alert button with the default style.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func `default`(
        _ label: Text,
        action: (() -> Void)? = {}
    ) -> Alert.Button

##  Parameters

`label`

    

The text to display on the button.

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button with the default style.

## See Also

### Getting a button

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.

Type Method

# cancel(_:)

Creates an alert button that indicates cancellation, with a system-provided
label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func cancel(_ action: (() -> Void)? = {}) -> Alert.Button

##  Parameters

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button that indicates cancellation.

## Discussion

The system automatically chooses locale-appropriate text for the button’s
label.

## See Also

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.

Type Method

# cancel(_:action:)

Creates an alert button that indicates cancellation, with a custom label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func cancel(
        _ label: Text,
        action: (() -> Void)? = {}
    ) -> Alert.Button

##  Parameters

`label`

    

The text to display on the button.

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button that indicates cancellation.

## See Also

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.

Type Method

# destructive(_:action:)

Creates an alert button with a style that indicates a destructive action.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    static func destructive(
        _ label: Text,
        action: (() -> Void)? = {}
    ) -> Alert.Button

##  Parameters

`label`

    

The text to display on the button.

`action`

    

A closure to execute when the user taps or presses the button.

## Return Value

An alert button that indicates a destructive action.

## See Also

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.

