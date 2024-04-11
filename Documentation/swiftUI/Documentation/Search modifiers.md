Instance Method

# searchable(text:placement:prompt:)

Marks this view as searchable, which configures the display of a search field.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func searchable(
        text: Binding<String>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil
    ) -> some View
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:placement:prompt:)

Marks this view as searchable, which configures the display of a search field.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func searchable(
        text: Binding<String>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey
    ) -> some View
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:placement:prompt:)

Marks this view as searchable, which configures the display of a search field.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func searchable<S>(
        text: Binding<String>,
        placement: SearchFieldPlacement = .automatic,
        prompt: S
    ) -> some View where S : StringProtocol
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:isPresented:placement:prompt:)

Marks this view as searchable with programmatic presentation of the search
field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable(
        text: Binding<String>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey
    ) -> some View
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:isPresented:placement:prompt:)

Marks this view as searchable with programmatic presentation of the search
field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable(
        text: Binding<String>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil
    ) -> some View
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:isPresented:placement:prompt:)

Marks this view as searchable with programmatic presentation of the search
field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<S>(
        text: Binding<String>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: S
    ) -> some View where S : StringProtocol
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchPresentationToolbarBehavior(_:)

Configures the search toolbar presentation behavior for any searchable
modifiers within this view.

iOS 17.1+  iPadOS 17.1+  macOS 14.1+  Mac Catalyst 17.1+  tvOS 17.1+  watchOS
10.1+  visionOS 1.0+

    
    
    func searchPresentationToolbarBehavior(_ behavior: SearchPresentationToolbarBehavior) -> some View
    

## Discussion

By default on iOS, a toolbar may hide parts of its content when presenting
search to focus on searching. You can override this behavior by providing a
value of `avoidHidingContent` to this modifer.

## See Also

### Displaying toolbar content during search

`struct SearchPresentationToolbarBehavior`

A type that defines how the toolbar behaves when presenting search.

Instance Method

# searchable(text:tokens:placement:prompt:token:)

Marks this view as searchable with text and tokens.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func searchable<C, T, S>(
        text: Binding<String>,
        tokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: S,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:tokens:placement:prompt:token:)

Marks this view as searchable with text and tokens.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:tokens:placement:prompt:token:)

Marks this view as searchable with text and tokens.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:tokens:isPresented:placement:prompt:token:)

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:tokens:isPresented:placement:prompt:token:)

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:tokens:isPresented:placement:prompt:token:)

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C, T, S>(
        text: Binding<String>,
        tokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: S,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:editableTokens:isPresented:placement:prompt:token:)

Marks this view as searchable, which configures the display of a search field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C>(
        text: Binding<String>,
        editableTokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: some StringProtocol,
        @ViewBuilder token: @escaping (Binding<C.Element>) -> some View
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`editableTokens`

    

A collection of tokens to display and edit in the search field.

`isPresenting`

    

A `Binding` which controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:editableTokens:isPresented:placement:prompt:token:)

Marks this view as searchable, which configures the display of a search field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C>(
        text: Binding<String>,
        editableTokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil,
        @ViewBuilder token: @escaping (Binding<C.Element>) -> some View
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`editableTokens`

    

A collection of tokens to display and edit in the search field.

`isPresenting`

    

A `Binding` which controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:editableTokens:isPresented:placement:prompt:token:)

Marks this view as searchable, which configures the display of a search field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C>(
        text: Binding<String>,
        editableTokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey,
        @ViewBuilder token: @escaping (Binding<C.Element>) -> some View
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`editableTokens`

    

A collection of tokens to display and edit in the search field.

`isPresenting`

    

A `Binding` which controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:editableTokens:placement:prompt:token:)

Marks this view as searchable, which configures the display of a search field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C>(
        text: Binding<String>,
        editableTokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil,
        @ViewBuilder token: @escaping (Binding<C.Element>) -> some View
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`editableTokens`

    

A collection of tokens to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:editableTokens:placement:prompt:token:)

Marks this view as searchable, which configures the display of a search field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C>(
        text: Binding<String>,
        editableTokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey,
        @ViewBuilder token: @escaping (Binding<C.Element>) -> some View
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`editableTokens`

    

A collection of tokens to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchable(text:editableTokens:placement:prompt:token:)

Marks this view as searchable, which configures the display of a search field.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C>(
        text: Binding<String>,
        editableTokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: some StringProtocol,
        @ViewBuilder token: @escaping (Binding<C.Element>) -> some View
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`editableTokens`

    

A collection of tokens to display and edit in the search field.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

Performing a search operation

Update search results based on search text and optional tokens that you store.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: Text?) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable(text: Binding<String>, placement: SearchFieldPlacement,
prompt: LocalizedStringKey) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement,
prompt: S) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some
View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text and tokens.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Instance Method

# searchSuggestions(_:)

Configures the search suggestions for this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func searchSuggestions<S>(@ViewBuilder _ suggestions: () -> S) -> some View where S : View
    

##  Parameters

`suggestions`

    

A view builder that produces content that populates a list of suggestions.

## Discussion

You can suggest search terms during a search operation by providing a
collection of view to this modifier. The interface presents the suggestion
views as a list of choices when someone activates the search interface.
Associate a string with each suggestion view by adding the
`searchCompletion(_:)` modifier to the view. For example, you can suggest
fruit types by displaying their emoji, and provide the corresponding search
string as a search completion in each case:

When someone chooses a suggestion, SwiftUI replaces the text in the search
field with the search completion string. If you omit the search completion
modifier for a particular suggestion view, SwiftUI displays the suggestion,
but the suggestion view doesn’t react to taps or clicks.

Important

In tvOS, searchable modifiers only support suggestion views of type `Text`,
like in the above example. Other platforms can use any view for the
suggestions, including custom views.

You can update the suggestions that you provide as conditions change.

For example, you can specify an array of suggestions that you store in a
model:

If the model’s `suggestedSearches` begins as an empty array, the interface
doesn’t display any suggestions to start. You can then provide logic that
updates the array based on some condition. For example, you might update the
completions based on the current search text. Note that certain events or
actions, like when someone moves a macOS window, might dismiss the suggestion
view.

For more information about using search modifiers, see Adding a search
interface to your app.

## See Also

### Making search suggestions

Suggesting search terms

Provide suggestions to people searching for content in your app.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

Instance Method

# searchSuggestions(_:for:)

Configures how to display search suggestions within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func searchSuggestions(
        _ visibility: Visibility,
        for placements: SearchSuggestionsPlacement.Set
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of the search suggestions for the specified locations.

`placements`

    

The set of locations in which to set the visibility of search suggestions.

## Discussion

SwiftUI presents search suggestions differently depending on several factors,
like the platform, the position of the search field, and the size class. Use
this modifier when you want to only display suggestions in certain ways under
certain conditions. For example, you might choose to display suggestions in a
menu when possible, but directly filter your data source otherwise.

## See Also

### Making search suggestions

Suggesting search terms

Provide suggestions to people searching for content in your app.

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

Instance Method

# searchCompletion(_:)

Associates a search token with the value of this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func searchCompletion<T>(_ token: T) -> some View where T : Identifiable
    

##  Parameters

`token`

    

Data to use as the view’s completion.

## Discussion

Use this method to associate a search token with a view that is within a
search suggestion list context. The system uses this value when the view is
selected to replace the partial text being currently edited of the associated
search field.

## See Also

### Making search suggestions

Suggesting search terms

Provide suggestions to people searching for content in your app.

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

Instance Method

# searchCompletion(_:)

Associates a fully formed string with the value of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func searchCompletion(_ completion: String) -> some View
    

##  Parameters

`text`

    

A string to use as the view’s completion.

## Discussion

Use this method to associate a fully formed string with a view that is within
a search suggestion list context. The system uses this value when the view is
selected to replace the partial text being currently edited of the associated
search field.

On tvOS, the string that you provide to the this modifier is used when
displaying the associated suggestion and when replacing the partial text of
the search field.

## See Also

### Making search suggestions

Suggesting search terms

Provide suggestions to people searching for content in your app.

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

Instance Method

# searchable(text:tokens:suggestedTokens:placement:prompt:token:)

Marks this view as searchable with text, tokens, and suggestions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        suggestedTokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`suggestedTokens`

    

A collection of tokens to display as suggestions.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Making search suggestions

Suggesting search terms

Provide suggestions to people searching for content in your app.

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

Instance Method

# searchable(text:tokens:suggestedTokens:placement:prompt:token:)

Marks this view as searchable with text, tokens, and suggestions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        suggestedTokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`suggestedTokens`

    

A collection of tokens to display as suggestions.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Making search suggestions

Suggesting search terms

Provide suggestions to people searching for content in your app.

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

Instance Method

# searchable(text:tokens:suggestedTokens:placement:prompt:token:)

Marks this view as searchable with text, tokens, and suggestions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func searchable<C, T, S>(
        text: Binding<String>,
        tokens: Binding<C>,
        suggestedTokens: Binding<C>,
        placement: SearchFieldPlacement = .automatic,
        prompt: S,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`suggestedTokens`

    

A collection of tokens to display as suggestions.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Making search suggestions

Suggesting search terms

Provide suggestions to people searching for content in your app.

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchCompletion<T>(T) -> some View`

Associates a search token with the value of this view.

`func searchCompletion(String) -> some View`

Associates a fully formed string with the value of this view.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

Instance Method

# searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        suggestedTokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: LocalizedStringKey,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`suggestedTokens`

    

A collection of tokens to display as suggestions.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

The key for the localized prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C, T>(
        text: Binding<String>,
        tokens: Binding<C>,
        suggestedTokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: Text? = nil,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`suggestedTokens`

    

A collection of tokens to display as suggestions.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A `Text` view representing the prompt of the search field which provides users
with guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchable<C, T, S>(
        text: Binding<String>,
        tokens: Binding<C>,
        suggestedTokens: Binding<C>,
        isPresented: Binding<Bool>,
        placement: SearchFieldPlacement = .automatic,
        prompt: S,
        @ViewBuilder token: @escaping (C.Element) -> T
    ) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
    

##  Parameters

`text`

    

The text to display and edit in the search field.

`tokens`

    

A collection of tokens to display and edit in the search field.

`suggestedTokens`

    

A collection of tokens to display as suggestions.

`isPresenting`

    

A `Binding` that controls the presented state of search.

`placement`

    

The preferred placement of the search field within the containing view
hierarchy.

`prompt`

    

A string representing the prompt of the search field which provides users with
guidance on what to search for.

`token`

    

A view builder that creates a view given an element in tokens.

## Discussion

For more information about using searchable modifiers, see Adding a search
interface to your app. For information about presenting a search field
programmatically, see Managing search interface activation.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

`struct DismissSearchAction`

An action that can end a search interaction.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> some View`

Marks this view as searchable with programmatic presentation of the search
field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> some View`

Marks this view as searchable with text and tokens, as well as programmatic
presentation.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Method

# searchScopes(_:scopes:)

Configures the search scopes for this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.4+  visionOS
1.0+

    
    
    func searchScopes<V, S>(
        _ scope: Binding<V>,
        @ViewBuilder scopes: () -> S
    ) -> some View where V : Hashable, S : View
    

##  Parameters

`scope`

    

The active scope of the search field.

`scopes`

    

A view builder that represents the scoping options SwiftUI uses to populate a
`Picker`.

## Discussion

To enable people to narrow the scope of their searches, you can create a type
that represents the possible scopes, and then create a state variable to hold
the current selection. For example, you can scope the product search to just
fruits or just vegetables:

Provide a binding to the scope, as well as a view that represents each scope:

SwiftUI uses this binding and view to add a `Picker` with the search field. In
iOS, iPadOS, macOS, and tvOS, the picker appears below the search field when
search is active. To ensure that the picker operates correctly, match the type
of the scope binding with the type of each view’s tag. Then modify your search
to account for the current value of the `scope` state property.

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Limiting search scope

Scoping a search operation

Divide the search space into a few broad categories.

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> some View`

Configures the search scopes for this view with the specified activation
strategy.

`struct SearchScopeActivation`

The ways that searchable modifiers can show or hide search scopes.

Instance Method

# searchScopes(_:activation:_:)

Configures the search scopes for this view with the specified activation
strategy.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  visionOS
1.0+

    
    
    func searchScopes<V, S>(
        _ scope: Binding<V>,
        activation: SearchScopeActivation,
        @ViewBuilder _ scopes: () -> S
    ) -> some View where V : Hashable, S : View
    

##  Parameters

`scope`

    

The active scope of the search field.

`activation`

    

The activation style of the search field’s scopes.

`scopes`

    

A view builder that represents the scoping options SwiftUI uses to populate a
`Picker`.

## Discussion

To enable people to narrow the scope of their searches, you can create a type
that represents the possible scopes, and then create a state variable to hold
the current selection. For example, you can scope the product search to just
fruits or just vegetables:

Provide a binding to the scope, as well as a view that represents each scope:

SwiftUI uses this binding and view to add a `Picker` below the search field.
In iOS, macOS, and tvOS, the picker appears below the search field when search
is active. To ensure that the picker operates correctly, match the type of the
scope binding with the type of each view’s tag. Then condition your search on
the current value of the `scope` state property.

By default, the appearance of scopes varies by platform:

  * In iOS and iPadOS, search scopes appear when someone enters text into the search field and disappear when someone cancels the search.

  * In macOS, search scopes appear when SwiftUI presents search and disappear when someone cancels the search.

However, you can use the `activation` parameter with a value of `onTextEntry`
or `onSearchPresentation` to configure this behavior:

For more information about using searchable modifiers, see Adding a search
interface to your app.

## See Also

### Limiting search scope

Scoping a search operation

Divide the search space into a few broad categories.

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View`

Configures the search scopes for this view.

`struct SearchScopeActivation`

The ways that searchable modifiers can show or hide search scopes.

Instance Method

# searchDictationBehavior(_:)

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func searchDictationBehavior(_ dictationBehavior: TextInputDictationBehavior) -> some View
    

## See Also

### Dictating text

`struct TextInputDictationActivation`

`struct TextInputDictationBehavior`

