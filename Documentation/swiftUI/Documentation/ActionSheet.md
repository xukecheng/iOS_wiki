Initializer

# init(title:message:buttons:)

Creates an action sheet with the provided buttons.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    init(
        title: Text,
        message: Text? = nil,
        buttons: [ActionSheet.Button] = [.cancel()]
    )

Deprecated

Use a `View` modifier like
`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`
instead.

##  Parameters

`title`

    

The title of the action sheet.

`message`

    

The message to display in the body of the action sheet.

`buttons`

    

The buttons to show in the action sheet.

Type Alias

# ActionSheet.Button

A button representing an operation of an action sheet presentation.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  Mac Catalyst
13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated  watchOS 6.0–10.4
Deprecated  visionOS 1.0+

    
    
    typealias Button = Alert.Button

Deprecated

Use a `View` modifier like
`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`
instead.

## Discussion

The `ActionSheet` button is type-aliased to the `Alert` button type, which
provides default, cancel, and destructive styles.

