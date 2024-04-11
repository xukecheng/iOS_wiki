Initializer

# init(_:prompt:onSubmit:)

Creates a TextFieldLink which when pressed will request text input from the
user.

watchOS 9.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        prompt: Text? = nil,
        onSubmit: @escaping (String) -> Void
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

A key for the TextFieldLink’s localized title, that describes the purpose of
requesting text input.

`prompt`

    

Text which describes the reason for requesting text input.

`onSubmit`

    

An action to perform when text input has been accepted and dismissed

## See Also

### Creating a text field link

`init<S>(S, prompt: Text?, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` is `Text`.

`init(prompt: Text?, label: () -> Label, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` conforms to `View`.

Initializer

# init(_:prompt:onSubmit:)

Creates a TextFieldLink which when pressed will request text input from the
user.

watchOS 9.0+

    
    
    init<S>(
        _ title: S,
        prompt: Text? = nil,
        onSubmit: @escaping (String) -> Void
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

A key for the TextFieldLink’s localized title, that describes the purpose of
requesting text input.

`prompt`

    

Text which describes the reason for requesting text input.

`onSubmit`

    

An action to perform when text input has been accepted and dismissed

## See Also

### Creating a text field link

`init(LocalizedStringKey, prompt: Text?, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` is `Text`.

`init(prompt: Text?, label: () -> Label, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` conforms to `View`.

Initializer

# init(prompt:label:onSubmit:)

Creates a TextFieldLink which when pressed will request text input from the
user.

watchOS 9.0+

    
    
    init(
        prompt: Text? = nil,
        @ViewBuilder label: () -> Label,
        onSubmit: @escaping (String) -> Void
    )

Available when `Label` conforms to `View`.

##  Parameters

`label`

    

A view that describes the action of requesting text input.

`prompt`

    

Text which describes the reason for requesting text input.

`onSubmit`

    

An action to perform when text input has been accepted and dismissed

## See Also

### Creating a text field link

`init(LocalizedStringKey, prompt: Text?, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` is `Text`.

`init<S>(S, prompt: Text?, onSubmit: (String) -> Void)`

Creates a TextFieldLink which when pressed will request text input from the
user.

Available when `Label` is `Text`.

