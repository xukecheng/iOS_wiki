Article

# Adding a search interface to your app

Present an interface that people can use to search for content in your app.

## Overview

Add a search interface to your app by applying one of the searchable view
modifiers — like `searchable(text:placement:prompt:)` — to a
`NavigationSplitView` or `NavigationStack`, or to a view inside one of these.
A search field then appears in the toolbar. The precise placement and
appearance of the search field depends on the platform, where you put the
modifier in code, and its configuration.

The searchable modifier that creates the field takes a `Binding` to a string
that represents the search field’s text. You provide the storage for the
string — and optionally for an array of discrete search tokens — that you use
to conduct the search. To learn about managing the search field’s data, see
Performing a search operation.

### Place the search field automatically

You can automatically place the search field by adding the
`searchable(text:placement:prompt:)` modifier to a navigation element like a
navigation split view:

With this configuration, the search field appears on the trailing edge of the
toolbar in macOS. In iOS and iPadOS, the first or second column displays the
search field in a double or triple column navigation view, respectively. The
above three-column example puts the search field at the top of the middle
column on iPad.

  * macOS 
  * iOS 

### Control the placement structurally

To add a search field to a specific column in iOS and iPadOS, add the
searchable modifier to a view in that column. For example, to indicate that
the search covers departments in the previous example, you could place the
search field in the first column by adding the modifier to that column’s
`DepartmentList` view instead of to the navigation split view:

### Control the placement programmatically

You can alternatively use the `placement` input parameter to suggest a
`SearchFieldPlacement` value for the search interface. For example, you can
achieve the same results as the previous example in macOS using the `sidebar`
placement:

If SwiftUI can’t satisfy the placement request, like when you ask for sidebar
placement in a searchable modifier that isn’t applied to a navigation split
view, SwiftUI relies instead on its automatic placement rules.

### Set a prompt for the search field

By default, the search field contains Search as the placeholder text, to
prompt people on how to use the field. You can customize the prompt by setting
either a string, a `Text` view, or a `LocalizedStringKey` for the searchable
modifier’s `prompt` input parameter. For example, you might use this to
clarify that the search field in the Department column searches among both
departments and the products in each department:

## See Also

### Searching your app’s data model

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

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`struct SearchFieldPlacement`

The placement of a search field in a view hierarchy.

Article

# Performing a search operation

Update search results based on search text and optional tokens that you store.

## Overview

To conduct a search in your app’s data model, create storage for the query
text and present it with a searchable view modifier. Because you manage the
storage, you can detect when it changes and update the search operation in
response. By updating search results as people type, you ensure that your
app’s search interface is responsive.

You can also optionally provide storage for tokens, which are discrete search
terms that your app recognizes. Tokens provide a way to combine multiple
search terms, and make it easier for you to indicate that a search term is
common or expected in your app.

For information on how to control the placement of the search field in your
app’s interface, see Adding a search interface to your app.

### Provide storage for a string

The searchable modifiers take a `Binding` to a string value for the `text`
input. The string serves as the storage for the search query field that
SwiftUI displays. You can create this storage inside a view using a `State`
property, and initialize it to an empty string:

To make it easier to share the search query among different views, you can
create a published value inside an observable object that’s part of your app’s
model:

In either case, pass a `Binding` to this string into the searchable view
modifier by adding the dollar sign (`$`) prefix to the value:

### Provide storage for tokens

In addition to a search string, the search field can also display tokens when
you use one of the searchable modifiers that has a `tokens` parameter, like
`searchable(text:tokens:placement:prompt:token:)`.

You create tokens by defining a group of values that conform to the
`Identifiable` protocol, then instantiate the collection of values. For
example you can create an enumeration of fruit tokens:

Then add a new published property to your model to store a collection of
tokens:

To display tokens, provide a `Binding` to the `tokens` array as the searchable
modifier’s `tokens` input parameter, and describe how to draw each token using
the `token` closure. From the closure, return the `View` that represents the
token given as an input. For example, you can use a `Text` view to represent
each token:

You can represent the token with a `Text` view, as the above example
demonstrates. In iOS and iPadOS, you can use a `Label` instead. Ensure the
view clearly represents the corresponding search query, and if you use a
label, that the tokens fit the search query field’s height. Tokens appear at
the beginning of the search field before any plain text. The following shows
how the search field looks when the `tokens` array contains the `apple` and
`banana` tokens:

### Support tokens that have a mutable component

You can enable people to mutate part of the data that represents a token by
using a `Picker` in the `token` closure. For example, suppose you have fruit
token data that contains both a kind and a hydration property:

With your new model, specify a `Binding` to the token in the `token` closure
by adding a dollar sign (`$`). Use the binding to create a picker for the
`hydration` property and a label that uses the `kind` property:

### Add tokens to the search

Provide a way for people to add tokens to the search field. You can do this in
different ways. For example, you can:

  * Suggest tokens to add to the array by using one of the searchable view modifiers that have a `suggestedTokens` input parameter, like `searchable(text:tokens:suggestedTokens:placement:prompt:token:)`. People select suggestions from a list that appears below the search field. For more information about offering suggestions for tokens, as well as for search text, see Suggesting search terms.

  * Monitor the search string as people edit it. When you detect a substring that matches one of the tokens, convert the text into a token by removing the relevant characters from the string and add the corresponding token to the `tokens` array.

  * Wait until you see a dividing character in the search string, like a comma or a space, and then attempt to tokenize the preceding characters.

  * Wait until someone submits the search, and then attempt to tokenize the entire search string. For more information about submitting a search, see Managing search interface activation.

### Conduct the search

When you detect changes in the search query, your app can begin a search. How
you perform the search operation depends on how your app stores and presents
data. One approach is to filter the elements that appear in a `List` based on
whether a field in the list’s items matches the search query. For example, you
can create a method that returns only the items in an array of products with
names that match the search text or one of the tokens currently in the search
field:

Consider the complexity of the search and the cost of changing the search
terms. If the cost is high, like when updates require network access, or for
complex filter logic, consider prefetching and caching data or reducing the
frequency of updates. Alternatively, you can wait until someone submits the
query before conducting the search. For information about detecting query
submission, see Managing search interface activation.

If the search space can be broken into broad categories, you can help people
narrow the search more quickly by providing a scope. See Scoping a search
operation.

## See Also

### Searching your app’s data model

Adding a search interface to your app

Present an interface that people can use to search for content in your app.

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

Structure

# SearchFieldPlacement

The placement of a search field in a view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct SearchFieldPlacement

## Overview

You can give a preferred placement to any of the searchable modifiers, like
`searchable(text:placement:prompt:)`:

Depending on the containing view hierachy, SwiftUI might not be able to
fulfill your request.

## Topics

### Getting a search field placement

`static let automatic: SearchFieldPlacement`

SwiftUI places the search field automatically.

`static let navigationBarDrawer: SearchFieldPlacement`

The search field appears in the navigation bar.

`static func navigationBarDrawer(displayMode:
SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement`

The search field appears in the navigation bar using the specified display
mode.

`static let sidebar: SearchFieldPlacement`

The search field appears in the sidebar of a navigation view.

`static let toolbar: SearchFieldPlacement`

The search field appears in the toolbar.

### Supporting types

`struct NavigationBarDrawerDisplayMode`

A mode that determines when to display a search field that appears in a
navigation bar.

## Relationships

### Conforms To

  * `Sendable`

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

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

Article

# Suggesting search terms

Provide suggestions to people searching for content in your app.

## Overview

You can suggest query text during a search operation by providing a collection
of search suggestion views. Because suggestion views are not limited to plain
text, you must also provide the search string that each suggestion view
represents. You can also provide suggestions for tokens, if your search
interface includes them. SwiftUI presents the suggestions in a list below the
search field.

For both text and tokens, you manage the list of suggestions, so you have
complete flexibility to decide what to suggest. For example, you can:

  * Offer a static list of suggestions.

  * Remember previous searches and offer the most recent or most common ones.

  * Update the list of suggestions in real time based on the current search text.

  * Employ some combination of these and other strategies, possibly changing over time.

### Suggest search text

Suggest search text by providing a collection of views to the
`searchSuggestions(_:)` view modifier. This modifier applies to the
`searchable(text:placement:prompt:)` modifier that appears before it.

When someone activates the search interface, it presents the suggestion views
as a list of choices below the query string. Associate a string with each
suggestion view by adding the `searchCompletion(_:)` modifier to the view
inside the search suggestions closure. For example, you can include emoji with
fruit types that you suggest as possible products to search for, and provide
the corresponding search string as a search completion in each case:

When someone chooses a suggestion, SwiftUI replaces the text in the search
field with the search completion string. In the above example, choosing “🍐
Pear” puts the text “pear” in the search query.

If you omit the search completion modifier for a particular suggestion view,
SwiftUI displays the view, but the view doesn’t react to taps or clicks.
However, you can group the views with `Section` containers that have headers,
enabling you to distinguish different kinds of suggestions, like recent
searches and common search terms.

Important

In tvOS, searchable modifiers only support suggestion views of type `Text`,
like in the above example. Other platforms can use arbitrary views for the
suggestions, including custom views.

Certain events or actions, like when someone moves a macOS window, might
dismiss the suggestion list.

### Suggest tokens

You can also suggest tokens for the search field. In this case, associate a
suggestion view with a token using the version of the `searchCompletion(_:)`
modifier that takes tokens as input:

You can use any type that conforms to the `Identifiable` protocol as a token.
For more information about using tokens in the search query, see Performing a
search operation.

### Simplify token suggestions

As a convenience when you have a collection of suggestions that exactly
matches the list of tokens, you can create a collection of possible tokens to
suggest. For example, you can add a published `suggestions` property to your
model that contains all the possible tokens:

Then you can provide this array to one of the searchable modifiers that takes
a `suggestedTokens` input parameter, like
`searchable(text:tokens:suggestedTokens:placement:prompt:token:)`. SwiftUI
uses this to generate the suggestions automatically:

In this version of the searchable modifier, SwiftUI uses one view builder to
describe the appearance of the tokens in both the search field and the
suggestions container.

### Update suggestions dynamically

You can update the suggestions that you provide as conditions change. For
example, you can specify an array of `suggestedSearches` that you store in
your app’s model:

If `suggestedSearches` begins as an empty array, the interface doesn’t display
any suggestions to start. You can then update the array as conditions change,
like when you want to include previous searches.

## See Also

### Making search suggestions

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

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

`struct SearchSuggestionsPlacement`

The ways that SwiftUI displays search suggestions.

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

Structure

# SearchSuggestionsPlacement

The ways that SwiftUI displays search suggestions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct SearchSuggestionsPlacement

## Overview

You can influence which modes SwiftUI displays search suggestions for by using
the `searchSuggestions(_:for:)` modifier:

In the above example, SwiftUI only displays search suggestions in a
suggestions menu. You might want to do this when you want to render search
suggestions in a container, like inline with your own set of search results.

You can get the current search suggestion placement by querying the
`searchSuggestionsPlacement` environment value in your search suggestions.

## Topics

### Getting placements

`static var automatic: SearchSuggestionsPlacement`

Search suggestions render automatically based on the surrounding context.

`static var content: SearchSuggestionsPlacement`

Search suggestions render in the main content of the app.

`static var menu: SearchSuggestionsPlacement`

Search suggestions render inside of a menu attached to the search field.

### Supporting types

`struct Set`

An efficient set of search suggestion display modes.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

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

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S,
token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions.

Article

# Scoping a search operation

Divide the search space into a few broad categories.

## Overview

If the data you want to search falls into a few categories, you can define
different scopes to help people narrow their search. When you define a scope,
SwiftUI presents a picker that people can use to choose one of them. You then
use the current scope selection as one of the inputs to the search operation.

### Define the possible scopes

Start by creating a type that conforms to the `Hashable` protocol to represent
the possible scopes. For example, you can use an enumeration to scope a
product search to just fruits or just vegetables:

Then create a property to store the current scope, either as a state variable
in a view, or a published property in your model:

### Apply the scope

To use the scope information, bind the current scope to the
`searchScopes(_:scopes:)` modifier. You also indicate a set of views that
correspond to the different scopes. Like the `searchSuggestions(_:)` modifier,
the scopes modifier operates on the searchable modifier that’s closer to the
modified view, so it needs to follow the searchable modifier:

SwiftUI uses the binding and views to add a `Picker` to the search field. By
default, the picker appears below the search field in macOS when search is
active, or in iOS when someone starts entering text into the search field:

  * macOS 
  * iOS 

You can change when the picker appears by using the
`searchScopes(_:activation:_:)` modifier instead, and supplying one of the
`SearchScopeActivation` values, like `onTextEntry` or `onSearchPresentation`.

To ensure that the picker operates correctly, match the type of the scope
binding with the type of each view’s tag. In the above example, both the
`scope` input and the tags for each view have the type `ProductScope`.

### Use the scope in your search

Modify your search to account for the current value of the `scope` property,
if you offer it, along with the text and tokens in the query. For example, you
might include the scope as one element of a predicate that you define for a
Core Data fetch request. For more information about conducting a search, see
Performing a search operation.

## See Also

### Limiting search scope

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View`

Configures the search scopes for this view.

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> some View`

Configures the search scopes for this view with the specified activation
strategy.

`struct SearchScopeActivation`

The ways that searchable modifiers can show or hide search scopes.

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

Structure

# SearchScopeActivation

The ways that searchable modifiers can show or hide search scopes.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    struct SearchScopeActivation

## Topics

### Getting search scope activiation types

`static var automatic: SearchScopeActivation`

The automatic activation of the scope bar.

`static var onSearchPresentation: SearchScopeActivation`

An activation where the system shows search scopes after presenting search and
hides search scopes after search cancellation.

`static var onTextEntry: SearchScopeActivation`

An activation where the system shows search scopes when typing begins in the
search field and hides search scopes after search cancellation.

## See Also

### Limiting search scope

Scoping a search operation

Divide the search space into a few broad categories.

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View`

Configures the search scopes for this view.

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> some View`

Configures the search scopes for this view with the specified activation
strategy.

Article

# Managing search interface activation

Programmatically detect and dismiss a search field.

## Overview

People activate a search field in your app by tapping or clicking it, after
which they can enter search terms. In many cases, your app only needs to react
to the corresponding changes in the search text values, which the interface
updates through the binding that you provide, as described in Performing a
search operation.

However, SwiftUI also provides controls that enable you to programmatically
manage the search interface. In particular, you can:

  * Activate or deactivate the interface using a binding that you provide to the searchable modifier.

  * Detect whether the interface is active by reading an environment value.

  * Dismiss the interface by calling an action stored in the environment.

  * Wait for a search submission event before starting to search.

### Control activation through a binding

You can control search interface activation programmatically by providing the
searchable modifier’s `isPresented` parameter with a `Binding` to a Boolean
value. For example, to present a sheet that appears with the search interface
already active, create a binding that starts as true:

On iOS and macOS, SwiftUI focuses the search field when presenting search and
unfocuses the search field when dismissing search. The search field can also
lose focus while the search interface remains presented. For example, if your
search interface contains a list of text fields, someone might move focus to
one of the text fields without dismissing the interface.

### Detect search activation

If you need to know when the search interface is active, you can query the
environment’s `isSearching` property using the `Environment` property wrapper.
The following example shows a view that updates the text it displays based on
the state of the property:

When someone first taps or clicks in a search field, the `isSearching`
property becomes `true`. When they cancel or submit the search operation, the
property becomes `false`. It also becomes `false` if you programmatically
dismiss the interface, as the next section describes.

Be sure to read the property from inside a view that’s wrapped, either
directly or indirectly, by one of the `searchable(text:placement:prompt:)`
view modifiers, like `SearchedView` in the above example. You won’t detect any
change in the property value if you read it from outside of that context, like
if you put it in the `SearchingExample` view.

### Dismiss the search interface

You can programmatically deactivate the interface using the environment’s
`dismissSearch` action. For example, consider a view with a `Button` that
presents more information about the first matching item from a collection:

The button becomes visible only after someone enters search text that produces
a match. The button’s action shows a sheet that provides more information
about the item, including an Add button for adding the item to a stored list
of items:

People can dismiss the sheet by dragging it down, effectively canceling the
operation, leaving the in-progress search interaction intact. Alternatively,
They can tap the Add button to store the item. Because people are likely done
with both the detail view and the search interaction at this point, the
button’s closure uses the `dismiss` property to dismiss the sheet, and the
`dismissSearch` property to reset the search field.

As with the `isSearching` property, be sure to only read `dismissSearch` from
within the hierarchy of a searchable view modifier. Calling the action has no
effect if you read it from the environment outside of that context. The above
example reads the action from `SearchedView`, and passes that into the sheet,
because the sheet has its own environment. The action also has no effect if
the search interface isn’t active.

### React to search submission

To specify an action that SwiftUI invokes when someone submits the search
query (by pressing the Return key), add the `onSubmit(of:_:)` modifier:

Depending your app’s structure, you can use search submission in different
ways. For example, you can take that opportunity to look for substrings among
the search query string that you can convert into tokens. Alternatively, for a
search operation that’s very slow, perhaps because it requires a network
access, you can wait for a submission event before performing a search.

## See Also

### Detecting, activating, and dismissing search

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

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Property

# isSearching

A Boolean value that indicates when the user is searching.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isSearching: Bool { get }

## Discussion

You can read this value like any of the other `EnvironmentValues`, by creating
a property with the `Environment` property wrapper:

Get the value to find out when the user interacts with a search field that’s
produced by one of the searchable modifiers, like
`searchable(text:placement:prompt:)`:

When the user first taps or clicks in a search field, the `isSearching`
property becomes `true`. When the user cancels the search operation, the
property becomes `false`. To programmatically set the value to `false` and
dismiss the search operation, use `dismissSearch`.

Important

Access the value from inside the searched view, as the example above
demonstrates, rather than from the searched view’s parent. SwiftUI sets the
value in the environment of the view that you apply the searchable modifier
to, and doesn’t propagate the value up the view hierarchy.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

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

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Instance Property

# dismissSearch

An action that ends the current search interaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var dismissSearch: DismissSearchAction { get }

## Discussion

Use this environment value to get the `DismissSearchAction` instance for the
current `Environment`. Then call the instance to dismiss the current search
interaction. You call the instance directly because it defines a
`callAsFunction()` method that Swift calls when you call the instance.

When you dismiss search, SwiftUI:

  * Sets `isSearching` to `false`.

  * Clears any text from the search field.

  * Removes focus from the search field.

Note

Calling this instance has no effect if the user isn’t interacting with a
search field.

Use this action to dismiss a search operation based on another user
interaction. For example, consider a searchable view with a `Button` that
presents more information about the first matching item from a collection:

The button becomes visible only after the user enters search text that
produces a match. When the user taps the button, SwiftUI shows a sheet that
provides more information about the item, including an Add button for adding
the item to a stored list of items:

People can dismiss the sheet by dragging it down, effectively canceling the
operation, leaving the in-progress search interaction intact. Alternatively,
people can tap the Add button to store the item. Because the person using your
app is likely to be done with both the detail view and the search interaction
at this point, the button’s closure also uses the `dismiss` property to
dismiss the sheet, and the `dismissSearch` property to reset the search field.

Important

Access the action from inside the searched view, as the example above
demonstrates, rather than from the searched view’s parent, or another
hierarchy, like that of a sheet. SwiftUI sets the value in the environment of
the view that you apply the searchable modifier to, and doesn’t propagate the
value up the view hierarchy.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

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

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View`

Marks this view as searchable with text, tokens, and suggestions, as well as
programmatic presentation.

Structure

# DismissSearchAction

An action that can end a search interaction.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct DismissSearchAction

## Overview

Use the `dismissSearch` environment value to get the instance of this
structure for a given `Environment`. Then call the instance to dismiss the
current search interaction. You call the instance directly because it defines
a `callAsFunction()` method that Swift calls when you call the instance.

When you dismiss search, SwiftUI:

  * Sets `isSearching` to `false`.

  * Clears any text from the search field.

  * Removes focus from the search field.

Note

Calling this instance has no effect if the user isn’t interacting with a
search field.

Use this action to dismiss a search operation based on another user
interaction. For example, consider a searchable view with a `Button` that
presents more information about the first matching item from a collection:

The button becomes visible only after the user enters search text that
produces a match. When the user taps the button, SwiftUI shows a sheet that
provides more information about the item, including an Add button for adding
the item to a stored list of items:

People can dismiss the sheet by dragging it down, effectively canceling the
operation, leaving the in-progress search interaction intact. Alternatively,
people can tap the Add button to store the item. Because the person using your
app is likely to be done with both the detail view and the search interaction
at this point, the button’s closure also uses the `dismiss` property to
dismiss the sheet, and the `dismissSearch` property to reset the search field.

Important

Access the action from inside the searched view, as the example above
demonstrates, rather than from the searched view’s parent, or another
hierarchy, like that of a sheet. SwiftUI sets the value in the environment of
the view that you apply the searchable modifier to, and doesn’t propagate the
value up the view hierarchy.

## Topics

### Calling the action

`func callAsFunction()`

Dismisses the current search operation, if any.

## See Also

### Detecting, activating, and dismissing search

Managing search interface activation

Programmatically detect and dismiss a search field.

`var isSearching: Bool`

A Boolean value that indicates when the user is searching.

`var dismissSearch: DismissSearchAction`

An action that ends the current search interaction.

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

Structure

# SearchPresentationToolbarBehavior

A type that defines how the toolbar behaves when presenting search.

iOS 17.1+  iPadOS 17.1+  macOS 14.1+  Mac Catalyst 17.1+  tvOS 17.1+  watchOS
10.1+  visionOS 1.0+

    
    
    struct SearchPresentationToolbarBehavior

## Overview

Use this type in combination with the `searchPresentationToolbarBehavior(_:)`

## Topics

### Getting toolbar behaviors

`static var automatic: SearchPresentationToolbarBehavior`

The automatic behavior.

`static var avoidHidingContent: SearchPresentationToolbarBehavior`

The avoid hiding content behavior.

## See Also

### Displaying toolbar content during search

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
some View`

Configures the search toolbar presentation behavior for any searchable
modifiers within this view.

Instance Method

# findNavigator(isPresented:)

Programmatically presents the find and replace interface for text editor
views.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func findNavigator(isPresented: Binding<Bool>) -> some View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that controls the presentation of the find and
replace interface.

## Return Value

A view that presents the find and replace interface when `isPresented` is
`true`.

## Discussion

Add this modifier to a `TextEditor`, or to a view hierarchy that contains at
least one text editor, to control the presentation of the find and replace
interface. When you set the `isPresented` binding to `true`, the system shows
the interface, and when you set it to `false`, the system hides the interface.
The following example shows and hides the interface based on the state of a
toolbar button:

The find and replace interface allows people to search for instances of a
specified string in the text editor, and optionally to replace instances of
the search string with another string. They can also show and hide the
interface using built-in controls, like menus and keyboard shortcuts. SwiftUI
updates `isPresented` to reflect the users’s actions.

If the text editor view isn’t currently in focus, the system still presents
the find and replace interface when you set `isPresented` to `true`. If the
view hierarchy contains multiple editors, the one that shows the find and
replace interface is nondeterministic.

You can disable the find and replace interface for a text editor by applying
the `findDisabled(_:)` modifier to the editor. If you do that, setting this
modifier’s `isPresented` binding to `true` has no effect, but only if the
disabling modifier appears closer to the text editor, like this:

## See Also

### Searching for text in a view with find and replace

`func findDisabled(Bool) -> some View`

Prevents find and replace operations in a text editor.

`func replaceDisabled(Bool) -> some View`

Prevents replace operations in a text editor.

Instance Method

# findDisabled(_:)

Prevents find and replace operations in a text editor.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func findDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that indicates whether to disable the find and replace
interface for a text editor.

## Return Value

A view that disables the find and replace interface.

## Discussion

Add this modifier to ensure that people can’t activate the find and replace
interface for a `TextEditor`:

When you disable the find operation, you also implicitly disable the replace
operation. If you want to only disable replace, use `replaceDisabled(_:)`
instead.

Using this modifer also prevents programmatic find and replace interface
presentation using the `findNavigator(isPresented:)` method. Be sure to place
the disabling modifier closer to the text editor for this to work:

If you apply this modifer at multiple levels of a view hierarchy, the call
closest to the text editor takes precedence. For example, people can activate
find and replace for the first text editor in the following example, but not
the second:

## See Also

### Searching for text in a view with find and replace

`func findNavigator(isPresented: Binding<Bool>) -> some View`

Programmatically presents the find and replace interface for text editor
views.

`func replaceDisabled(Bool) -> some View`

Prevents replace operations in a text editor.

Instance Method

# replaceDisabled(_:)

Prevents replace operations in a text editor.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func replaceDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that indicates whether text replacement in the find and
replace interface is disabled.

## Return Value

A view that disables the replace feature of a find and replace interface.

## Discussion

Add this modifier to ensure that people can’t activate the replace feature of
a find and replace interface for a `TextEditor`:

If you want to disable both find and replace, use the `findDisabled(_:)`
modifier instead.

Using this modifer also disables the replace feature of a find and replace
interface that you present programmatically using the
`findNavigator(isPresented:)` method. Be sure to place the disabling modifier
closer to the text editor for this to work:

If you apply this modifer at multiple levels of a view hierarchy, the call
closest to the text editor takes precedence. For example, people can activate
find and replace for the first text editor in the following example, but only
find for the second:

## See Also

### Searching for text in a view with find and replace

`func findNavigator(isPresented: Binding<Bool>) -> some View`

Programmatically presents the find and replace interface for text editor
views.

`func findDisabled(Bool) -> some View`

Prevents find and replace operations in a text editor.

