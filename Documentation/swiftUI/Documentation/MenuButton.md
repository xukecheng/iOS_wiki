Initializer

# init(_:content:)

Creates a menu button with the specified localized title and content.

macOS 10.15–14.4  Deprecated

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

Use `Menu` instead.

## See Also

### Creating a menu button

`init<S>(S, content: () -> Content)`

Creates a menu button with the specified title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

`init(label: Label, content: () -> Content)`

Creates a menu button with the specified label and content.

Deprecated

Initializer

# init(_:content:)

Creates a menu button with the specified title and content.

macOS 10.15–14.4  Deprecated

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

Use `Menu` instead.

## See Also

### Creating a menu button

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu button with the specified localized title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

`init(label: Label, content: () -> Content)`

Creates a menu button with the specified label and content.

Deprecated

Initializer

# init(label:content:)

Creates a menu button with the specified label and content.

macOS 10.15–14.4  Deprecated

    
    
    init(
        label: Label,
        @ViewBuilder content: () -> Content
    )

Deprecated

Use `Menu` instead.

## See Also

### Creating a menu button

`init(LocalizedStringKey, content: () -> Content)`

Creates a menu button with the specified localized title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

`init<S>(S, content: () -> Content)`

Creates a menu button with the specified title and content.

Available when `Label` is `Text` and `Content` conforms to `View`.

Deprecated

Instance Method

# menuButtonStyle(_:)

Sets the style for menu buttons within this view.

macOS 10.15–14.4  Deprecated

    
    
    func menuButtonStyle<S>(_ style: S) -> some View where S : MenuButtonStyle
    

Deprecated

Use `menuStyle(_:)` instead.

## See Also

### Styling a menu button

`protocol MenuButtonStyle`

A custom specification for the appearance and interaction of a menu button.

Deprecated

Protocol

# MenuButtonStyle

A custom specification for the appearance and interaction of a menu button.

macOS 10.15–14.4  Deprecated

    
    
    protocol MenuButtonStyle

Deprecated

Use `MenuStyle` instead.

## Topics

### Supporting types

`struct BorderlessButtonMenuButtonStyle`

A menu button style which manifests as a borderless button with no visual
embelishments.

`struct BorderlessPullDownMenuButtonStyle`

A menu button style which manifests as a borderless pull-down button.

`struct DefaultMenuButtonStyle`

The default menu button style.

`struct PullDownMenuButtonStyle`

A menu button style which manifests as a pull-down button.

## Relationships

### Conforming Types

  * `BorderlessButtonMenuButtonStyle`
  * `BorderlessPullDownMenuButtonStyle`
  * `DefaultMenuButtonStyle`
  * `PullDownMenuButtonStyle`

## See Also

### Styling a menu button

`func menuButtonStyle<S>(S) -> some View`

Sets the style for menu buttons within this view.

Deprecated

