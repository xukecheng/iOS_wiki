Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a string variable as a
title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A>(
        _ title: S,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a text view for the
title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A>(
        _ title: Text,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

The title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:actions:)

Presents an alert when a given condition is true, using a localized string key
for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:)

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) ->
some View`

Presents an alert when an error is present.

Instance Method

# alert(isPresented:error:actions:)

Presents an alert when an error is present.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<E, A>(
        isPresented: Binding<Bool>,
        error: E?,
        @ViewBuilder actions: () -> A
    ) -> some View where E : LocalizedError, A : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`error`

    

An optional localized Error that is used to generate the alert’s title. The
system passes the contents to the modifier’s closures. You use this data to
populate the fields of an alert that you create that the system displays to
the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

## Discussion

In the example below, a form conditionally presents an alert depending upon
the value of an error. When the error value isn’t `nil`, the system presents
an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert

`func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a string variable as a
title.

`func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some
View`

Presents an alert when a given condition is true, using a text view for the
title.

`func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () ->
A) -> some View`

Presents an alert when a given condition is true, using a localized string key
for the title.

`func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
text view as a title.

`func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting:
T?, actions: (T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
localized string key for a title.

`func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions:
(T) -> A) -> some View`

Presents an alert using the given data to produce the alert’s content and a
string variable as a title.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true using a string
variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, M>(
        _ title: S,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:actions:message:)

Presents an alert with a message when a given condition is true using a text
view as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M>(
        _ title: Text,
        isPresented: Binding<Bool>,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

The title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A `ViewBuilder` returning the message for the alert.

## Discussion

In the example below, a login form conditionally presents an alert by setting
the `didFail` state variable. When the form sets the value to to `true`, the
system displays an alert with an “OK” action.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<A, M, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(_:isPresented:presenting:actions:message:)

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<S, A, M, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the alert.

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`data`

    

An optional source of truth for the alert. The system passes the contents to
the modifier’s closures. You use this data to populate the fields of an alert
that you create that the system displays to the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions given the currently available
data.

`message`

    

A `ViewBuilder` returning the message for the alert given the currently
available data.

## Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not
be `nil`. The data should not change after the presentation occurs. Any
changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content
from a data source. The example below shows a custom data source,
`SaveDetails`, that provides data to populate the alert:

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A,
message: (E) -> M) -> some View`

Presents an alert with a message when an error is present.

Instance Method

# alert(isPresented:error:actions:message:)

Presents an alert with a message when an error is present.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func alert<E, A, M>(
        isPresented: Binding<Bool>,
        error: E?,
        @ViewBuilder actions: (E) -> A,
        @ViewBuilder message: (E) -> M
    ) -> some View where E : LocalizedError, A : View, M : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the alert.
When the user presses or taps one of the alert’s actions, the system sets this
value to `false` and dismisses.

`error`

    

An optional localized Error that is used to generate the alert’s title. The
system passes the contents to the modifier’s closures. You use this data to
populate the fields of an alert that you create that the system displays to
the user.

`actions`

    

A `ViewBuilder` returning the alert’s actions.

`message`

    

A view builder returning the message for the alert given the current error.

## Discussion

In the example below, a form conditionally presents an alert depending upon
the value of an error. When the error value isn’t `nil`, the system presents
an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

All actions in an alert dismiss the alert after the action runs. The default
button is shown with greater prominence. You can influence the default button
by assigning it the `defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No
default cancel action is provided. If you want to show a cancel action, use a
button with a role of `cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are
`Text`. Passing any other type of view results in the content being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Presenting an alert with a message

`func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a string
variable as a title.

`func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: ()
-> A, message: () -> M) -> some View`

Presents an alert with a message when a given condition is true, using a
localized string key for a title.

`func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message:
() -> M) -> some View`

Presents an alert with a message when a given condition is true using a text
view as a title.

`func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>,
presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a localized string key for a title.

`func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a text view for a title.

`func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?,
actions: (T) -> A, message: (T) -> M) -> some View`

Presents an alert with a message using the given data to produce the alert’s
content and a string variable as a title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Getting confirmation for an action

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:)

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where A : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

Presents a confirmation dialog using data to produce the dialog’s content and
a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A
    ) -> some View where S : StringProtocol, A : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Getting confirmation for an action

`func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a string
variable as a title.

`func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility:
Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a text
view for the title.

`func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A) -> some View`

Presents a confirmation dialog when a given condition is true, using a
localized string key for the title.

`func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a text view for the title.

`func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View`

Presents a confirmation dialog using data to produce the dialog’s content and
a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, M>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        @ViewBuilder actions: () -> A,
        @ViewBuilder message: () -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`actions`

    

A view builder returning the dialog’s actions.

`message`

    

A view builder returning the message for the dialog.

## Discussion

In the example below, a button conditionally presents a confirmation dialog
depending upon the value of a bound Boolean variable. When the Boolean value
is set to `true`, the system displays a confirmation dialog with a cancel
action and a destructive action.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M, T>(
        _ title: Text,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`title`

    

the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<S, A, M, T>(
        _ title: S,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where S : StringProtocol, A : View, M : View
    

##  Parameters

`title`

    

A text string used as the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented:
Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A,
message: (T) -> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

Instance Method

#
confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a localized string key for the title.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func confirmationDialog<A, M, T>(
        _ titleKey: LocalizedStringKey,
        isPresented: Binding<Bool>,
        titleVisibility: Visibility = .automatic,
        presenting data: T?,
        @ViewBuilder actions: (T) -> A,
        @ViewBuilder message: (T) -> M
    ) -> some View where A : View, M : View
    

##  Parameters

`titleKey`

    

The key for the localized string that describes the title of the dialog.

`isPresented`

    

A binding to a Boolean value that determines whether to present the dialog.
When the user presses or taps the dialog’s default action button, the system
sets this value to `false`, dismissing the dialog.

`titleVisibility`

    

The visibility of the dialog’s title. The default value is
`Visibility.automatic`.

`data`

    

An optional source of truth for the confirmation dialog. The system passes the
contents to the modifier’s closures. You use this data to populate the fields
of a confirmation dialog that you create that the system displays to the user.

`actions`

    

A view builder returning the dialog’s actions given the currently available
data.

`message`

    

A view builder returning the message for the dialog given the currently
available data.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`data` must not be `nil`. `data` should not change after the presentation
occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog
with content from a data source. The example below shows a custom data source,
`FileDetails`, that provides data to populate the dialog:

This modifier creates a `Text` view for the title on your behalf, and treats
the localized key similar to `init(_:tableName:bundle:comment:)`. See `Text`
for more information about localizing strings.

All actions in a confirmation dialog will dismiss the dialog after the action
runs. The default button will be shown with greater prominence. You can
influence the default button by assigning it the `defaultAction` keyboard
shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button
with a role of `cancel`, that button takes the place of the default dismiss
action. You don’t have to dismiss the presentation with the cancel button’s
action.

Note

In regular size classes in iOS, the system renders confirmation dialogs as a
popover that the user dismisses by tapping anywhere outside the popover,
rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with
labels that are `Text`. Passing any other type of view results in the content
being omitted.

## See Also

### Showing a confirmation dialog with a message

`func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a string variable for the title.

`func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a localized string key for the title.

`func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View`

Presents a confirmation dialog with a message when a given condition is true,
using a text view for the title.

`func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

`func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>,
titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T)
-> M) -> some View`

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a string variable for the title.

Instance Method

# dialogIcon(_:)

Configures the icon used by dialogs within this view.

iOS 17.0+  iPadOS 17.0+  macOS 13.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+

    
    
    func dialogIcon(_ icon: Image?) -> some View
    

##  Parameters

`icon`

    

The custom icon to use for confirmation dialogs and alerts. Passing `nil` will
use the default app icon.

## Discussion

On macOS, this icon replaces the default icon of the app.

On watchOS, this icon will be shown in any dialogs presented.

This modifier has no effect on other platforms.

The following example configures a `confirmationDialog` with a custom image.

## See Also

### Configuring a dialog

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSeverity(_:)

macOS 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func dialogSeverity(_ severity: DialogSeverity) -> some View
    

##  Parameters

`severity`

    

The severity to use for confirmation dialogs and alerts.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View
    

##  Parameters

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle<S>(
        _ title: S,
        isSuppressed: Binding<Bool>
    ) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The title of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(
        _ label: Text,
        isSuppressed: Binding<Bool>
    ) -> some View
    

##  Parameters

`label`

    

The label of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# dialogSuppressionToggle(_:isSuppressed:)

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func dialogSuppressionToggle(
        _ titleKey: LocalizedStringKey,
        isSuppressed: Binding<Bool>
    ) -> some View
    

##  Parameters

`titleKey`

    

The title of the suppression toggle in the dialog. This parameter can be
elided to use the default suppression title.

`isSuppressed`

    

Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows
the user to request the alert not be displayed again. Typically whether a
dialog is suppressed is stored in `AppStorage` and used to decide whether to
present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression
toggle. The toggle’s state is stored in `AppStorage` and used to determine
whether or not to show the dialog when the “Delete Items” button is pressed.

## See Also

### Configuring a dialog

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

Instance Method

# sheet(isPresented:onDismiss:content:)

Presents a sheet when a binding to a Boolean value that you provide is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sheet<Content>(
        isPresented: Binding<Bool>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the sheet that
you create in the modifier’s `content` closure.

`onDismiss`

    

The closure to execute when dismissing the sheet.

`content`

    

A closure that returns the content of the sheet.

## Discussion

Use this method when you want to present a modal view to the user when a
Boolean value you provide is true. The example below displays a modal view of
the mockup for a software license agreement when the user toggles the
`isShowingSheet` variable by clicking or tapping on the “Show License
Agreement” button:

In vertically compact environments, such as iPhone in landscape orientation, a
sheet presentation automatically adapts to appear as a full-screen cover. Use
the `presentationCompactAdaptation(_:)` or
`presentationCompactAdaptation(horizontal:vertical:)` modifier to override
this behavior.

## See Also

### Showing a sheet, cover, or popover

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# sheet(item:onDismiss:content:)

Presents a sheet using the given item as a data source for the sheet’s
content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func sheet<Item, Content>(
        item: Binding<Item?>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the sheet. When `item` is
non-`nil`, the system passes the item’s content to the modifier’s closure. You
display this content in a sheet that you create that the system displays to
the user. If `item` changes, the system dismisses the sheet and replaces it
with a new one using the same process.

`onDismiss`

    

The closure to execute when dismissing the sheet.

`content`

    

A closure returning the content of the sheet.

## Discussion

Use this method when you need to present a modal view with content from a
custom data source. The example below shows a custom data source
`InventoryItem` that the `content` closure uses to populate the display the
action sheet shows to the user:

In vertically compact environments, such as iPhone in landscape orientation, a
sheet presentation automatically adapts to appear as a full-screen cover. Use
the `presentationCompactAdaptation(_:)` or
`presentationCompactAdaptation(horizontal:vertical:)` modifier to override
this behavior.

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# fullScreenCover(isPresented:onDismiss:content:)

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    func fullScreenCover<Content>(
        isPresented: Binding<Bool>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the sheet.

`onDismiss`

    

The closure to execute when dismissing the modal view.

`content`

    

A closure that returns the content of the modal view.

## Discussion

Use this method to show a modal view that covers as much of the screen as
possible. The example below displays a custom view when the user toggles the
value of the `isPresenting` binding:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# fullScreenCover(item:onDismiss:content:)

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS 7.0+
visionOS 1.0+

    
    
    func fullScreenCover<Item, Content>(
        item: Binding<Item?>,
        onDismiss: (() -> Void)? = nil,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the sheet. When `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You
display this content in a sheet that you create that the system displays to
the user. If `item` changes, the system dismisses the currently displayed
sheet and replaces it with a new one using the same process.

`onDismiss`

    

The closure to execute when dismissing the modal view.

`content`

    

A closure returning the content of the modal view.

## Discussion

Use this method to display a modal view that covers as much of the screen as
possible. In the example below a custom structure — `CoverData` — provides
data for the full-screen view to display in the `content` closure when the
user clicks or taps the “Present Full-Screen Cover With Data” button:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# popover(isPresented:attachmentAnchor:arrowEdge:content:)

Presents a popover when a given condition is true.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func popover<Content>(
        isPresented: Binding<Bool>,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        @ViewBuilder content: @escaping () -> Content
    ) -> some View where Content : View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that determines whether to present the popover
content that you return from the modifier’s `content` closure.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the popover. The
default is `bounds`.

`arrowEdge`

    

The edge of the `attachmentAnchor` that defines the location of the popover’s
arrow in macOS. The default is `Edge.top`. iOS ignores this parameter.

`content`

    

A closure returning the content of the popover.

## Discussion

Use this method to show a popover whose contents are a SwiftUI view that you
provide when a bound Boolean variable is `true`. In the example below, a
popover displays whenever the user toggles the `isShowingPopover` state
variable by pressing the “Show Popover” button:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: (Item) -> Content) -> some
View`

Presents a popover using the given item as a data source for the popover’s
content.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# popover(item:attachmentAnchor:arrowEdge:content:)

Presents a popover using the given item as a data source for the popover’s
content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  visionOS 1.0+

    
    
    func popover<Item, Content>(
        item: Binding<Item?>,
        attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds),
        arrowEdge: Edge = .top,
        @ViewBuilder content: @escaping (Item) -> Content
    ) -> some View where Item : Identifiable, Content : View
    

##  Parameters

`item`

    

A binding to an optional source of truth for the popover. When `item` is
non-`nil`, the system passes the contents to the modifier’s closure. You use
this content to populate the fields of a popover that you create that the
system displays to the user. If `item` changes, the system dismisses the
currently presented popover and replaces it with a new popover using the same
process.

`attachmentAnchor`

    

The positioning anchor that defines the attachment point of the popover. The
default is `bounds`.

`arrowEdge`

    

The edge of the `attachmentAnchor` that defines the location of the popover’s
arrow in macOS. The default is `Edge.top`. iOS ignores this parameter.

`content`

    

A closure returning the content of the popover.

## Discussion

Use this method when you need to present a popover with content from a custom
data source. The example below uses data in the `PopoverModel` structure to
populate the view in the `content` closure that the popover displays to the
user:

## See Also

### Showing a sheet, cover, or popover

`func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?,
content: () -> Content) -> some View`

Presents a sheet when a binding to a Boolean value that you provide is true.

`func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?,
content: (Item) -> Content) -> some View`

Presents a sheet using the given item as a data source for the sheet’s
content.

`func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() ->
Void)?, content: () -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible when
binding to a Boolean value you provide is true.

`func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() ->
Void)?, content: (Item) -> Content) -> some View`

Presents a modal view that covers as much of the screen as possible using the
binding you provide as a data source for the sheet’s content.

`func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor:
PopoverAttachmentAnchor, arrowEdge: Edge, content: () -> Content) -> some
View`

Presents a popover when a given condition is true.

`enum PopoverAttachmentAnchor`

An attachment anchor for a popover.

Instance Method

# interactiveDismissDisabled(_:)

Conditionally prevents interactive dismissal of presentations like popovers,
sheets, and inspectors.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func interactiveDismissDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that indicates whether to prevent nonprogrammatic dismissal of
the containing view hierarchy when presented in a sheet or popover.

## Discussion

Users can dismiss certain kinds of presentations using built-in gestures. In
particular, a user can dismiss a sheet by dragging it down, or a popover by
clicking or tapping outside of the presented view. Use the
`interactiveDismissDisabled(_:)` modifier to conditionally prevent this kind
of dismissal. You typically do this to prevent the user from dismissing a
presentation before providing needed data or completing a required action.

For instance, suppose you have a view that displays a licensing agreement that
the user must acknowledge before continuing:

If you present this view in a sheet, the user can dismiss it by either tapping
the button — which calls `dismiss` from its `action` closure — or by dragging
the sheet down. To ensure that the user accepts the terms by tapping the
button, disable interactive dismissal, conditioned on the `areTermsAccepted`
property:

You can apply the modifier to any view in the sheet’s view hierarchy,
including to the sheet’s top level view, as the example demonstrates, or to
any child view, like the `Form` or the Accept `Button`.

The modifier has no effect on programmatic dismissal, which you can invoke by
updating the `Binding` that controls the presentation, or by calling the
environment’s `dismiss` action. On macOS, disabling interactive dismissal in a
popover makes the popover nontransient.

## See Also

### Dismissing a presentation

`var isPresented: Bool`

A Boolean value that indicates whether the view associated with this
environment is currently presented.

`var dismiss: DismissAction`

An action that dismisses the current presentation.

`struct DismissAction`

An action that dismisses a presentation.

Instance Method

# presentationDetents(_:)

Sets the available detents for the enclosing sheet.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDetents(_ detents: Set<PresentationDetent>) -> some View
    

##  Parameters

`detents`

    

A set of supported detents for the sheet. If you provide more that one detent,
people can drag the sheet to resize it.

## Discussion

By default, sheets support the `large` detent.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationDetents(_:selection:)

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDetents(
        _ detents: Set<PresentationDetent>,
        selection: Binding<PresentationDetent>
    ) -> some View
    

##  Parameters

`detents`

    

A set of supported detents for the sheet. If you provide more that one detent,
people can drag the sheet to resize it.

`selection`

    

A `Binding` to the currently selected detent. Ensure that the value matches
one of the detents that you provide for the `detents` parameter.

## Discussion

By default, sheets support the `large` detent.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationDragIndicator(_:)

Sets the visibility of the drag indicator on top of a sheet.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func presentationDragIndicator(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the drag indicator.

## Discussion

You can show a drag indicator when it isn’t apparent that a sheet can resize
or when the sheet can’t dismiss interactively.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationBackground(_:)

Sets the presentation background of the enclosing sheet using a shape style.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackground<S>(_ style: S) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

The shape style to use as the presentation background.

## Discussion

The following example uses the `thick` material as the sheet background:

The `presentationBackground(_:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier in several key ways. A
presentation background:

  * Automatically fills the entire presentation.

  * Allows views behind the presentation to show through translucent styles.

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationBackground(alignment:content:)

Sets the presentation background of the enclosing sheet to a custom view.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackground<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`content`

    

The view to use as the background of the presentation.

## Discussion

The following example uses a yellow view as the sheet background:

The `presentationBackground(alignment:content:)` modifier differs from the
`background(alignment:content:)` modifier in several key ways. A presentation
background:

  * Automatically fills the entire presentation.

  * Allows views behind the presentation to show through translucent areas of the `content`.

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationBackgroundInteraction(_:)

Controls whether people can interact with the view behind a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View
    

##  Parameters

`interaction`

    

A specification of how people can interact with the view behind a
presentation.

## Discussion

On many platforms, SwiftUI automatically disables the view behind a sheet that
you present, so that people can’t interact with the backing view until they
dismiss the sheet. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind the
sheet when the sheet is at the smallest detent, but not at the other detents:

## See Also

### Styling a sheet and its background

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# presentationCompactAdaptation(horizontal:vertical:)

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCompactAdaptation(
        horizontal horizontalAdaptation: PresentationAdaptation,
        vertical verticalAdaptation: PresentationAdaptation
    ) -> some View
    

##  Parameters

`horizontalAdaptation`

    

The adaptation to use in a horizontally compact size class.

`verticalAdaptation`

    

The adaptation to use in a vertically compact size class. In a size class that
is both horizontally and vertically compact, SwiftUI uses the
`verticalAdaptation` value.

## Discussion

Some presentations adapt their appearance depending on the context. For
example, a popover presentation over a horizontally-compact view uses a sheet
appearance by default. Use this modifier to indicate a custom adaptation
preference.

If you want to specify the same adaptation for both dimensions, use the
`presentationCompactAdaptation(_:)` method instead.

## See Also

### Adapting a presentation to size classes

`func presentationCompactAdaptation(PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to compact size classes.

`struct PresentationAdaptation`

Strategies for adapting a presentation to a different size class.

Instance Method

# presentationCompactAdaptation(_:)

Specifies how to adapt a presentation to compact size classes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCompactAdaptation(_ adaptation: PresentationAdaptation) -> some View
    

##  Parameters

`adaptation`

    

The adaptation to use in either a horizontally or vertically compact size
class.

## Discussion

Some presentations adapt their appearance depending on the context. For
example, a sheet presentation over a vertically-compact view uses a full-
screen-cover appearance by default. Use this modifier to indicate a custom
adaptation preference. For example, the following code uses a presentation
adaptation value of `none` to request that the system not adapt the sheet in
compact size classes:

If you want to specify different adaptations for each dimension, use the
`presentationCompactAdaptation(horizontal:vertical:)` method instead.

## See Also

### Adapting a presentation to size classes

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

`struct PresentationAdaptation`

Strategies for adapting a presentation to a different size class.

Instance Method

# presentationContentInteraction(_:)

Configures the behavior of swipe gestures on a presentation.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationContentInteraction(_ behavior: PresentationContentInteraction) -> some View
    

##  Parameters

`behavior`

    

The requested behavior.

## Discussion

By default, when a person swipes up on a scroll view in a resizable
presentation, the presentation grows to the next detent. A scroll view
embedded in the presentation only scrolls after the presentation reaches its
largest size. Use this modifier to control which action takes precedence.

For example, you can request that swipe gestures scroll content first,
resizing the sheet only after hitting the end of the scroll view, by passing
the `scrolls` value to this modifier:

People can always resize your presentation using the drag indicator.

## See Also

### Configuring a sheet’s height

`func presentationDetents(Set<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet.

`func presentationDetents(Set<PresentationDetent>, selection:
Binding<PresentationDetent>) -> some View`

Sets the available detents for the enclosing sheet, giving you programmatic
control of the currently selected detent.

`func presentationDragIndicator(Visibility) -> some View`

Sets the visibility of the drag indicator on top of a sheet.

`struct PresentationDetent`

A type that represents a height where a sheet naturally rests.

`protocol CustomPresentationDetent`

The definition of a custom detent with a calculated height.

`struct PresentationContentInteraction`

A behavior that you can use to influence how a presentation responds to swipe
gestures.

Instance Method

# presentationCornerRadius(_:)

Requests that the presentation have a specific corner radius.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func presentationCornerRadius(_ cornerRadius: CGFloat?) -> some View
    

##  Parameters

`cornerRadius`

    

The corner radius, or `nil` to use the system default.

## Discussion

Use this modifier to change the corner radius of a presentation.

## See Also

### Styling a sheet and its background

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`struct PresentationBackgroundInteraction`

The kinds of interaction available to views behind a presentation.

Instance Method

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentType: UTType,
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View where D : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentType`

    

The content type to use for the exported file.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`document` must not be `nil`. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentType: UTType,
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View where D : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentType`

    

The content type to use for the exported file.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`document` must not be `nil`. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:documents:contentType:onCompletion:)

Presents a system interface for exporting a collection of reference type
documents to files on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentType: UTType,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`documents`

    

The collection of in-memory documents to export.

`contentType`

    

The content type to use for the exported file.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`documents` must not be empty. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:documents:contentType:onCompletion:)

Presents a system interface for exporting a collection of value type documents
to files on disk.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentType: UTType,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`documents`

    

The collection of in-memory documents to export.

`contentType`

    

The content type to use for the exported file.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, both `isPresented` must be `true` and
`documents` must not be empty. When the operation is finished, `isPresented`
will be set to `false` before `onCompletion` is called. If the user cancels
the operation, `isPresented` will be set to `false` and `onCompletion` will
not be called.

The `contentType` provided must be included within the document type’s
`writableContentTypes`, otherwise the first valid writable content type will
be used instead.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where D : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`document`

    

The in-memory document to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`FileDocument.writableContentTypes` are used.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<D>(
        isPresented: Binding<Bool>,
        document: D?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where D : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`document`

    

The in-memory document to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`ReferenceFileDocument.writableContentTypes` are used.

`defaultFilename`

    

If provided, the default name to use for the exported file, which will the
user will have an opportunity to edit prior to the export.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where C : Collection, C.Element : ReferenceFileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`documents`

    

The in-memory documents to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`ReferenceFileDocument.writableContentTypes` are used.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C>(
        isPresented: Binding<Bool>,
        documents: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = {}
    ) -> some View where C : Collection, C.Element : FileDocument
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`documents`

    

The in-memory documents to export.

`contentTypes`

    

The list of supported content types which can be exported. If not provided,
`FileDocument.writableContentTypes` are used.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCancellation` will be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

#
fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<T>(
        isPresented: Binding<Bool>,
        item: T?,
        contentTypes: [UTType] = [],
        defaultFilename: String? = nil,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void = { }
    ) -> some View where T : Transferable
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`item`

    

The item to be saved on disk.

`contentTypes`

    

The optional content types to use for the exported file. If empty, SwiftUI
uses the content types from the `transferRepresentation` property provided for
`Transferable` conformance.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.

`onCancellation`

    

A callback that will be invoked if the operation was cancelled.

## Discussion

In order for the interface to appear `isPresented` must be set to `true`. When
the operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)

Presents a system interface allowing the user to export a collection of items
to files on disk.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporter<C, T>(
        isPresented: Binding<Bool>,
        items: C,
        contentTypes: [UTType] = [],
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void = { }
    ) -> some View where C : Collection, T : Transferable, T == C.Element
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`items`

    

Collection of values to be saved on disk.

`contentTypes`

    

The content types to use for the exported file. If empty, SwiftUI uses the
content types from the `transferRepresentation` property provided for
`Transferable` conformance.

`allowsOtherContentTypes`

    

A Boolean value that indicates if the users are allowed to save the files with
a different file extension than specified by the `contentType` property.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed.

`onCancellation`

    

A callback that will be invoked if the operation was cancelled.

## Discussion

In order for the interface to appear `isPresented` must be set to `true`. When
the operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a label for the file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

The key to a localized string to display.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel(_ label: Text?) -> some View
    

##  Parameters

`label`

    

The optional text to use as the label for the file name field.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel<S>(S) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

Instance Method

# fileExporterFilenameLabel(_:)

On macOS, configures the `fileExporter` with a label for the file name field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileExporterFilenameLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The string to use as the label for the file name field.

## See Also

### Exporting to file

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a value
type, like a structure, to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType:
UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void) -> some View`

Presents a system interface for exporting a document that’s stored in a
reference type, like a class, to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of value type documents
to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType:
UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for exporting a collection of reference type
documents to files on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface for allowing the user to export a `FileDocument`
to a file on disk.

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to export a
`ReferenceFileDocument` to a file on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `ReferenceFileDocument` to files on disk.

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system dialog for allowing the user to export a collection of
documents that conform to `FileDocument` to files on disk.

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system interface allowing the user to export a `Transferable` item
to file on disk.

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> some View`

Presents a system interface allowing the user to export a collection of items
to files on disk.

`func fileExporterFilenameLabel(LocalizedStringKey) -> some View`

On macOS, configures the `fileExporter` with a label for the file name field.

`func fileExporterFilenameLabel(Text?) -> some View`

On macOS, configures the `fileExporter` with a text to use as a label for the
file name field.

Instance Method

#
fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)

Presents a system interface for allowing the user to import multiple files.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        allowsMultipleSelection: Bool,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`allowsMultipleSelection`

    

Whether the importer allows the user to select more than one file to import.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed. To
access the received URLs, call `startAccessingSecurityScopedResource`. When
the access is no longer required, call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to choose multiple PDF files for
the application to combine them later, might look like this:

Note

Changing `allowedContentTypes` or `allowsMultipleSelection` while the file
importer is presented will have no immediate effect, however will apply the
next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

Instance Method

# fileImporter(isPresented:allowedContentTypes:onCompletion:)

Presents a system interface for allowing the user to import an existing file.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed. To
access the received URLs, call `startAccessingSecurityScopedResource`. When
the access is no longer required, call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the interface to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, an application can have a button that allows the user to choose
the default directory with document templates loaded on every launch. Such a
button might look like this:

Note

Changing `allowedContentTypes` while the file importer is presented will have
no immediate effect, however will apply the next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

Instance Method

#
fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to import multiple files.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileImporter(
        isPresented: Binding<Bool>,
        allowedContentTypes: [UTType],
        allowsMultipleSelection: Bool,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`allowedContentTypes`

    

The list of supported content types which can be imported.

`allowsMultipleSelection`

    

Whether the importer allows the user to select more than one file to import.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the
operation is finished, `isPresented` will be set to `false` before
`onCompletion` is called. If the user cancels the operation, `isPresented`
will be set to `false` and `onCompletion` will not be called.

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to choose multiple PDF files for
the application to combine them later, might look like this:

Note

Changing `allowedContentTypes` or `allowsMultipleSelection` while the file
importer is presented will have no immediate effect, however will apply the
next time it is presented.

## See Also

### Importing from file

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void) -> some View`

Presents a system interface for allowing the user to import multiple files.

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
onCompletion: (Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to import an existing file.

Instance Method

# fileMover(isPresented:file:onCompletion:)

Presents a system interface for allowing the user to move an existing file to
a new location.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileMover(
        isPresented: Binding<Bool>,
        file: URL?,
        onCompletion: @escaping (Result<URL, any Error>) -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`file`

    

The `URL` of the file to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed. To access the received URLs, call
`startAccessingSecurityScopedResource`. When the access is no longer required,
call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

Note

This interface provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and
`file` must not be `nil`. When the operation is finished, `isPresented` will
be set to `false` before `onCompletion` is called. If the user cancels the
operation, `isPresented` will be set to `false` and `onCompletion` will not be
called.

## See Also

### Moving a file

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:files:onCompletion:)

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func fileMover<C>(
        isPresented: Binding<Bool>,
        files: C,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void
    ) -> some View where C : Collection, C.Element == URL
    

##  Parameters

`isPresented`

    

A binding to whether the interface should be shown.

`files`

    

A collection of `URL`s for the files to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has has succeeded or
failed. To access the received URLs, call
`startAccessingSecurityScopedResource`. When the access is no longer required,
call `stopAccessingSecurityScopedResource`.

`result`

    

A `Result` indicating whether the operation succeeded or failed.

## Discussion

Note

This interface provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and
`files` must not be empty. When the operation is finished, `isPresented` will
be set to `false` before `onCompletion` is called. If the user cancels the
operation, `isPresented` will be set to `false` and `onCompletion` will not be
called.

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:file:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to move an existing file to a
new location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileMover(
        isPresented: Binding<Bool>,
        file: URL?,
        onCompletion: @escaping (Result<URL, any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`file`

    

The URL of the file to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move a file might look like
this:

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

Instance Method

# fileMover(isPresented:files:onCompletion:onCancellation:)

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileMover<C>(
        isPresented: Binding<Bool>,
        files: C,
        onCompletion: @escaping (Result<[URL], any Error>) -> Void,
        onCancellation: @escaping () -> Void
    ) -> some View where C : Collection, C.Element == URL
    

##  Parameters

`isPresented`

    

A binding to whether the dialog should be shown.

`files`

    

A collection of URLs for the files to be moved.

`onCompletion`

    

A callback that will be invoked when the operation has succeeded or failed.
The `result` indicates whether the operation succeeded or failed. To access
the received URLs, call `startAccessingSecurityScopedResource`. When the
access is no longer required, call `stopAccessingSecurityScopedResource`.

`onCancellation`

    

A callback that will be invoked if the user cancels the operation.

## Discussion

Note

This dialog provides security-scoped URLs. Call the
`startAccessingSecurityScopedResource` method to access or bookmark the URLs,
and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move files might look like this:

## See Also

### Moving a file

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move an existing file to
a new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void) -> some View`

Presents a system interface for allowing the user to move a collection of
existing files to a new location.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

Instance Method

# fileDialogBrowserOptions(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogBrowserOptions(_ options: FileDialogBrowserOptions) -> some View
    

##  Parameters

`options`

    

The search options to apply to a given file dialog.

## See Also

### Configuring a file dialog

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The string to use as the label for the confirmation button.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel(_ label: Text?) -> some View
    

##  Parameters

`label`

    

The optional text to use as the label for the confirmation button.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogConfirmationLabel(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogConfirmationLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

The key to a localized string to display.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogCustomizationID(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogCustomizationID(_ id: String) -> some View
    

##  Parameters

`id`

    

An identifier of the configuration.

## Discussion

Among other parameters, it stores the current directory, view style (e.g.,
Icons, List, Columns), recent places, and expanded window size. It enables a
refined user experience; for example, when importing an image, the user might
switch to the Icons view, but the List view could be more convenient in
another context. The file dialog stores these settings and applies them every
time before presenting the panel. If not provided, on every launch, the file
dialog uses the default configuration.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogDefaultDirectory(_:)

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogDefaultDirectory(_ defaultDirectory: URL?) -> some View
    

##  Parameters

`defaultDirectory`

    

The directory to show when the system file dialog launches. If the given file
dialog has a `fileDialogCustomizationID` if stores the user-chosen directory
and subsequently opens with it, ignoring the default value provided in this
modifier.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogImportsUnresolvedAliases(_:)

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogImportsUnresolvedAliases(_ imports: Bool) -> some View
    

##  Parameters

`imports`

    

A Boolean value that indicates if the application receives unresolved or
resolved URLs when a user chooses aliases.

## Discussion

By default, file dialogs resolve aliases and provide the URL of the item
referred to by the chosen alias. This modifier allows control of this
behavior: pass `true` if the application doesn’t want file dialog to resolve
aliases.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage<S>(_ message: S) -> some View where S : StringProtocol
    

##  Parameters

`message`

    

The string to use as the file dialog message.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage(_ message: Text?) -> some View
    

##  Parameters

`message`

    

The optional text to use as the file dialog message.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogMessage(_:)

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogMessage(_ messageKey: LocalizedStringKey) -> some View
    

##  Parameters

`messageKey`

    

The key to a localized string to display.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# fileDialogURLEnabled(_:)

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func fileDialogURLEnabled(_ predicate: Predicate<URL>) -> some View
    

##  Parameters

`predicate`

    

The predicate that evaluates the URLs presented to the user to conditionally
disable them. The implementation is expected to have constant complexity and
should not access the files contents or metadata. A common use case is
inspecting the path or the file name.

## See Also

### Configuring a file dialog

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogCustomizationID(String) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
persist and restore the file dialog configuration.

`func fileDialogDefaultDirectory(URL?) -> some View`

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the
specified default directory.

`func fileDialogImportsUnresolvedAliases(Bool) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
behavior when a user chooses an alias.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`struct FileDialogBrowserOptions`

The way that file dialogs present the file system.

Instance Method

# inspector(isPresented:content:)

Inserts an inspector at the applied position in the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspector<V>(
        isPresented: Binding<Bool>,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`isPresented`

    

A binding to `Bool` controlling the presented state.

`content`

    

The inspector content.

## Discussion

Apply this modifier to declare an inspector with a context-dependent
presentation. For example, an inspector can present as a trailing column in a
horizontally regular size class, but adapt to a sheet in a horizontally
compact size class.

Note

Trailing column inspectors have their presentation state restored by the
framework.

See Also

`InspectorCommands` for including the default inspector commands and keyboard
shortcuts.

## See Also

### Presenting an inspector

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

Instance Method

# inspectorColumnWidth(_:)

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspectorColumnWidth(_ width: CGFloat) -> some View
    

##  Parameters

`width`

    

The preferred fixed width for the inspector if presented as a trailing column.

## Discussion

Apply this modifier on the content of a `inspector(isPresented:content:)` to
specify a fixed preferred width for the trailing column. Use
`inspectorColumnWidth(min:ideal:max:)` if you need to specify a flexible
width.

The following example shows an editor interface with an inspector, which when
presented as a trailing-column, has a fixed width of 225 points. The example
also uses `interactiveDismissDisabled(_:)` to prevent the inspector from being
collapsed by user action like dragging a divider.

Note

A fixed width does not prevent the user collapsing the inspector on macOS. See
`interactiveDismissDisabled(_:)`.

## See Also

### Presenting an inspector

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

Instance Method

# inspectorColumnWidth(min:ideal:max:)

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+

    
    
    func inspectorColumnWidth(
        min: CGFloat? = nil,
        ideal: CGFloat,
        max: CGFloat? = nil
    ) -> some View
    

##  Parameters

`min`

    

The minimum allowed width for the trailing column inspector

`ideal`

    

The initial width of the inspector in the absence of state restoration.
`ideal` influences the resulting width on macOS when a user double-clicks the
divider on the leading edge of the inspector. clicks a divider to readjust

`max`

    

The maximum allowed width for the trailing column inspector

## Discussion

Apply this modifier on the content of a `inspector(isPresented:content:)` to
specify a preferred flexible width for the column. Use
`inspectorColumnWidth(_:)` if you need to specify a fixed width.

The following example shows an editor interface with an inspector, which when
presented as a trailing-column, has a preferred width of 225 points, maximum
of 400, and a minimum of 150 at which point it will collapse, if allowed.

Only some platforms enable flexible inspector columns. If you specify a width
that the current presentation environment doesn’t support, SwiftUI may use a
different width for your column.

## See Also

### Presenting an inspector

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

Instance Method

# quickLookPreview(_:)

Presents a Quick Look preview of the contents of a single URL.

QuickLook  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+

    
    
    func quickLookPreview(_ item: Binding<URL?>) -> some View
    

##  Parameters

`item`

    

A `Binding` to a URL that should be previewed.

## Return Value

A view that presents the preview of the contents of the URL.

## Discussion

The Quick Look preview appears when you set the binding to a non-`nil` item.
When you set the item back to `nil`, Quick Look dismisses the preview.

Upon dismissal by the user, Quick Look automatically sets the item binding to
`nil`. Quick Look displays the preview when a non-`nil` item is set. Set
`item` to `nil` to dismiss the preview.

## See Also

### Previewing content

`func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some
View`

Presents a Quick Look preview of the URLs you provide.

Instance Method

# quickLookPreview(_:in:)

Presents a Quick Look preview of the URLs you provide.

QuickLook  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+

    
    
    func quickLookPreview<Items>(
        _ selection: Binding<Items.Element?>,
        in items: Items
    ) -> some View where Items : RandomAccessCollection, Items.Element == URL
    

##  Parameters

`selection`

    

A `Binding` to an element that’s part of the items collection. This is the URL
that you currently want to preview.

`items`

    

A collection of URLs to preview.

## Return Value

A view that presents the preview of the contents of the URL.

## Discussion

The Quick Look preview appears when you set the binding to a non-`nil` item.
When you set the item back to `nil`, Quick Look dismisses the preview. If the
value of the selection binding isn’t contained in the items collection, Quick
Look treats it the same as a `nil` selection.

Quick Look updates the value of the selection binding to match the URL of the
file the user is previewing. Upon dismissal by the user, Quick Look
automatically sets the item binding to `nil`.

## See Also

### Previewing content

`func quickLookPreview(Binding<URL?>) -> some View`

Presents a Quick Look preview of the contents of a single URL.

Instance Method

# familyActivityPicker(isPresented:selection:)

Presents an activity picker view as a sheet.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func familyActivityPicker(
        isPresented: Binding<Bool>,
        selection: Binding<FamilyActivitySelection>
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding that indicates whether the app presents the picker view.

`selection`

    

A binding that manages the user-selected categories, apps, and web domains.

## Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

## See Also

### Configuring Family Sharing

`struct FamilyActivityPicker`

A view in which users specify applications, web domains, and categories
without revealing their choices to the app.

`func familyActivityPicker(headerText: String?, footerText: String?,
isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) ->
some View`

Presents an activity picker view as a sheet.

Instance Method

# familyActivityPicker(headerText:footerText:isPresented:selection:)

Presents an activity picker view as a sheet.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func familyActivityPicker(
        headerText: String? = nil,
        footerText: String? = nil,
        isPresented: Binding<Bool>,
        selection: Binding<FamilyActivitySelection>
    ) -> some View
    

##  Parameters

`headerText`

    

An optional string that provides text for the header of the picker view.

`footerText`

    

An optional string that provides text for the footer of the picker view.

`isPresented`

    

A binding that indicates whether the app presents the picker view.

`selection`

    

A binding that manages the user-selected categories, apps, and web domains.

## Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

## See Also

### Configuring Family Sharing

`struct FamilyActivityPicker`

A view in which users specify applications, web domains, and categories
without revealing their choices to the app.

`func familyActivityPicker(isPresented: Binding<Bool>, selection:
Binding<FamilyActivitySelection>) -> some View`

Presents an activity picker view as a sheet.

Instance Method

# activitySystemActionForegroundColor(_:)

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    func activitySystemActionForegroundColor(_ color: Color?) -> some View
    

##  Parameters

`color`

    

The text color to use. Pass `nil` to use the system’s default color.

## See Also

### Configuring a Live Activity

`func activityBackgroundTint(Color?) -> some View`

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

`var isActivityFullscreen: Bool`

A Boolean value that indicates whether the Live Activity appears in a full-
screen presentation.

Instance Method

# activityBackgroundTint(_:)

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func activityBackgroundTint(_ color: Color?) -> some View
    

##  Parameters

`color`

    

The background tint color to apply. To use the system’s default background
material, pass `nil`.

## Discussion

When you set a custom background tint color, consider setting a custom text
color for the auxiliary button people use to end a Live Activity on the Lock
Screen. To set a custom text color, use the
`activitySystemActionForegroundColor(_:)` view modifier.

## See Also

### Configuring a Live Activity

`func activitySystemActionForegroundColor(Color?) -> some View`

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

`var isActivityFullscreen: Bool`

A Boolean value that indicates whether the Live Activity appears in a full-
screen presentation.

Instance Method

# musicSubscriptionOffer(isPresented:options:onLoadCompletion:)

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

MusicKit  SwiftUI  iOS 15.0+  iPadOS 15.0+  macOS 12.0+

    
    
    func musicSubscriptionOffer(
        isPresented: Binding<Bool>,
        options: MusicSubscriptionOffer.Options = .default,
        onLoadCompletion: @escaping ((any Error)?) -> Void = { _ in }
    ) -> some View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that you can set to `true` to show a sheet with
subscription offers for Apple Music.

`options`

    

Options to use for loading the subscription offer for Apple Music.

`onLoadCompletion`

    

The function to call upon completing the initial loading process for this
subscription offer. The subscription offer UI becomes visible when it calls
this function with the error argument as `nil`. If there is an error in the
loading process, the subscription offer calls this function with a non-`nil`
error, and it resets the `isPresented` binding to `false`.

## Discussion

The example below displays a simple button that the user can activate to begin
presenting subscription offers for Apple Music. The action handler of this
button initiates the presentation of those offers by setting the
`isShowingOffer` variable to `true`.

You can also configure the Apple Music subscription offer by creating an
instance of `MusicSubscriptionOffer.Options`, setting relevant properties on
it, and passing it to `.musicSubscriptionOffer(…)`. For example, to present
contextual offers that highlight a specific album, you can configure the
subscription offer like the following:

The initial value of `offerOptions` includes relevant tokens (affiliate and
campaign tokens) that allow you to receive compensation for referring new
Apple Music subscribers. For more information, see this presentation of the
Apple Services Performance Partners Program.

You may also set `isShowingOffer` to `false` to programmatically dismiss the
subscription offer (or to abort its loading process).

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# appStoreOverlay(isPresented:configuration:)

Presents a StoreKit overlay when a given condition is true.

StoreKit  SwiftUI  iOS 14.0+  iPadOS 14.0+  visionOS 1.0+

    
    
    func appStoreOverlay(
        isPresented: Binding<Bool>,
        configuration: @escaping () -> SKOverlay.Configuration
    ) -> some View
    

##  Parameters

`isPresented`

    

A Binding to a boolean value indicating whether the overlay should be
presented.

`configuration`

    

A closure providing the configuration of the overlay.

## Discussion

You use `appStoreOverlay` to display an overlay that recommends another app.
The overlay enables users to instantly view the other app’s page on the App
Store.

When `isPresented` is true, the system will run `configuration` to determine
how to configure the overlay. The overlay will automatically be presented over
the current scene.

See Also

SKOverlay.Configuration.

## See Also

### Interacting with the App Store and Apple Music

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# manageSubscriptionsSheet(isPresented:)

StoreKit  SwiftUI  iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View
    

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# refundRequestSheet(for:isPresented:onDismiss:)

Display the refund request sheet for the given transaction.

StoreKit  SwiftUI  iOS 15.0+  iPadOS 15.0+  macOS 14.0+  Mac Catalyst 15.0+
visionOS 1.0+

    
    
    @preconcurrency
    func refundRequestSheet(
        for transactionID: Transaction.ID,
        isPresented: Binding<Bool>,
        onDismiss: (@MainActor (Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())? = nil
    ) -> some View
    

##  Parameters

`transactionID`

    

The transaction ID to request a refund for.

`isPresented`

    

A binding to a Boolean value that determines whether the refund request sheet
is presented.

`onDismiss`

    

The closure to execute when dismissing the sheet, with the result of the
refund request provided as a parameter.

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion:
(Result<Void, any Error>) -> Void) -> some View`

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# offerCodeRedemption(isPresented:onCompletion:)

Presents a sheet that enables users to redeem subscription offer codes that
you configure in App Store Connect.

StoreKit  SwiftUI  iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func offerCodeRedemption(
        isPresented: Binding<Bool>,
        onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }
    ) -> some View
    

##  Parameters

`isPresented`

    

A Binding to a boolean value indicating whether the sheet should be presented.

`onCompletion`

    

A closure that returns the result of the presentation.

## Discussion

Important

The resulting transaction from redeeming an offer code is emitted in
`Transaction.updates`. Set up a transaction listener as soon as your app
launches to receive new transactions while the app is running.

## See Also

### Interacting with the App Store and Apple Music

`func appStoreOverlay(isPresented: Binding<Bool>, configuration: () ->
SKOverlay.Configuration) -> some View`

Presents a StoreKit overlay when a given condition is true.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View`

`func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>,
onDismiss: ((Result<Transaction.RefundRequestStatus,
Transaction.RefundRequestError>) -> ())?) -> some View`

Display the refund request sheet for the given transaction.

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

`func currentEntitlementTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some
View`

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

`func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?)
-> some View`

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

`func manageSubscriptionsSheet(isPresented: Binding<Bool>,
subscriptionGroupID: String) -> some View`

`func onInAppPurchaseCompletion(perform: ((Product,
Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View`

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

`func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View`

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

`func productIconBorder() -> some View`

Adds a standard border to an icon used by an `ProductView` .

`func productViewStyle(some ProductViewStyle) -> some View`

Sets the style for in-app store products within a view.

`func productDescription(Visibility) -> some View`

`func storeButton(Visibility, for: StoreButtonKind...) -> some View`

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

`func storeProductTask(for: Product.ID, priority: TaskPriority, action:
(Product.TaskState) async -> ()) -> some View`

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

`func storeProductsTask(for: some Collection<String> & Equatable & Sendable,
priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) ->
some View`

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

`func subscriptionStatusTask(for: String, priority: TaskPriority, action:
(EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some
View`

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

`func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View`

Configures in-app subscription store instances within a view to use a certain
button label.

`func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo)
-> some View) -> some View`

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

`func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) ->
some View`

Sets the control style for in-app subscription stores within a view.

`func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View`

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

`func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind,
destination: () -> some View) -> some View`

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyDestination(url: URL, for:
SubscriptionStorePolicyKind) -> some View`

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View`

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle)
-> some View`

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

`func subscriptionStoreSignInAction((() -> ())?) -> some View`

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

`func subscriptionStoreControlBackground(SubscriptionStoreControlBackground)
-> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionStoreControlBackground(some ShapeStyle) -> some View`

Set the control background style for `SubscriptionStoreView` instances within
the view.

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# photosPicker(isPresented:selection:matching:preferredItemEncoding:)

Presents a Photos picker that selects a `PhotosPickerItem`.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  watchOS 9.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<PhotosPickerItem?>,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

The item being shown and selected in the Photos picker.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of the selected item. Default is
`.automatic`. Setting it to `.automatic` means the best encoding determined by
the system will be used.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

#
photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<PhotosPickerItem?>,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic,
        photoLibrary: PHPhotoLibrary
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

The item being shown and selected in the Photos picker.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of the selected item. Default is
`.automatic`. Setting it to `.automatic` means the best encoding determined by
the system will be used.

`photoLibrary`

    

The photo library to choose from.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

#
photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  watchOS 9.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<[PhotosPickerItem]>,
        maxSelectionCount: Int? = nil,
        selectionBehavior: PhotosPickerSelectionBehavior = .default,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

All items being shown and selected in the Photos picker.

`maxSelectionCount`

    

The maximum number of items that can be selected. Default is `nil`. Setting it
to `nil` means maximum supported by the system.

`selectionBehavior`

    

The selection behavior of the Photos picker. Default is `.default`.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of selected items. Default is `.automatic`.
Setting it to `.automatic` means the best encoding determined by the system
will be used.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

#
photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+

    
    
    func photosPicker(
        isPresented: Binding<Bool>,
        selection: Binding<[PhotosPickerItem]>,
        maxSelectionCount: Int? = nil,
        selectionBehavior: PhotosPickerSelectionBehavior = .default,
        matching filter: PHPickerFilter? = nil,
        preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic,
        photoLibrary: PHPhotoLibrary
    ) -> some View
    

##  Parameters

`isPresented`

    

The binding to whether the Photos picker should be shown.

`selection`

    

All items being shown and selected in the Photos picker.

`maxSelectionCount`

    

The maximum number of items that can be selected. Default is `nil`. Setting it
to `nil` means maximum supported by the system.

`selectionBehavior`

    

The selection behavior of the Photos picker. Default is `.default`.

`filter`

    

Types of items that can be shown. Default is `nil`. Setting it to `nil` means
all supported types can be shown.

`preferredItemEncoding`

    

The encoding disambiguation policy of selected items. Default is `.automatic`.
Setting it to `.automatic` means the best encoding determined by the system
will be used.

`photoLibrary`

    

The photo library to choose from.

## Discussion

The user explicitly grants access only to items they choose, so photo library
access authorization is not needed.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

# photosPickerAccessoryVisibility(_:edges:)

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

PhotosUI  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func photosPickerAccessoryVisibility(
        _ visibility: Visibility,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`edges`

    

The accessory visibility to apply.

`edges`

    

One or more of the available edges.

## Return Value

A Photos picker with the specified accessory visibility.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

# photosPickerDisabledCapabilities(_:)

Disables capabilities of the Photos picker.

PhotosUI  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func photosPickerDisabledCapabilities(_ disabledCapabilities: PHPickerCapabilities) -> some View
    

##  Parameters

`disabledCapabilities`

    

One or more of the available capabilities.

## Return Value

A Photos picker with specified capabilities that are disabled.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerStyle(PhotosPickerStyle) -> some View`

Sets the mode of the Photos picker.

Instance Method

# photosPickerStyle(_:)

Sets the mode of the Photos picker.

PhotosUI  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func photosPickerStyle(_ style: PhotosPickerStyle) -> some View
    

##  Parameters

`mode`

    

One of the available modes.

## Return Value

A Photos picker that uses the specified mode.

## See Also

### Selecting photos

`struct PhotosPicker`

A view that displays a Photos picker for choosing assets from the photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy) -> some View`

Presents a Photos picker that selects a `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)
-> some View`

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo
library.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some
View`

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

`func photosPicker(isPresented: Binding<Bool>, selection:
Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior:
PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary) -> some View`

Presents a Photos picker that selects a collection of `PhotosPickerItem` from
a given photo library.

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some
View`

Sets the accessory visibility of the Photos picker. Accessories include
anything between the content and the edge, like the navigation bar or the
sidebar.

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View`

Disables capabilities of the Photos picker.

