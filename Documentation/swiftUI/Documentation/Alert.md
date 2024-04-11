Initializer

# init(title:message:dismissButton:)

Creates an alert with one button.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        title: Text,
        message: Text? = nil,
        dismissButton: Alert.Button? = nil
    )

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the alert.

`message`

    

The message to display in the body of the alert.

`dismissButton`

    

The button that dismisses the alert.

## See Also

### Creating an alert

`init(title: Text, message: Text?, primaryButton: Alert.Button,
secondaryButton: Alert.Button)`

Creates an alert with two buttons.

Deprecated

`static func sideBySideButtons(title: Text, message: Text?, primaryButton:
Alert.Button, secondaryButton: Alert.Button) -> Alert`

Creates a side by side button alert.

Deprecated

Initializer

# init(title:message:primaryButton:secondaryButton:)

Creates an alert with two buttons.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        title: Text,
        message: Text? = nil,
        primaryButton: Alert.Button,
        secondaryButton: Alert.Button
    )

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the alert.

`message`

    

The message to display in the body of the alert.

`primaryButton`

    

The first button to show in the alert.

`secondaryButton`

    

The second button to show in the alert.

## Discussion

The system determines the visual ordering of the buttons.

## See Also

### Creating an alert

`init(title: Text, message: Text?, dismissButton: Alert.Button?)`

Creates an alert with one button.

Deprecated

`static func sideBySideButtons(title: Text, message: Text?, primaryButton:
Alert.Button, secondaryButton: Alert.Button) -> Alert`

Creates a side by side button alert.

Deprecated

Type Method

# sideBySideButtons(title:message:primaryButton:secondaryButton:)

Creates a side by side button alert.

watchOS 6.0–10.4  Deprecated

    
    
    static func sideBySideButtons(
        title: Text,
        message: Text? = nil,
        primaryButton: Alert.Button,
        secondaryButton: Alert.Button
    ) -> Alert

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the alert.

`message`

    

The message to display in the body of the alert.

`primaryButton`

    

The first button to show in the alert.

`secondaryButton`

    

The second button to show in the alert.

## Discussion

The system determines the visual ordering of the buttons.

## See Also

### Creating an alert

`init(title: Text, message: Text?, dismissButton: Alert.Button?)`

Creates an alert with one button.

Deprecated

`init(title: Text, message: Text?, primaryButton: Alert.Button,
secondaryButton: Alert.Button)`

Creates an alert with two buttons.

Deprecated

Structure

# Alert.Button

A button that represents an operation of an alert presentation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    struct Button

Deprecated

Use a `View` modifier like `alert(_:isPresented:presenting:actions:message:)`
instead.

## Topics

### Getting a button

`static func `default`(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with the default style.

`static func cancel((() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a system-provided
label.

`static func cancel(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button that indicates cancellation, with a custom label.

`static func destructive(Text, action: (() -> Void)?) -> Alert.Button`

Creates an alert button with a style that indicates a destructive action.

