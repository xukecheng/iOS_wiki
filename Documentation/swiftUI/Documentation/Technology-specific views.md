Structure

# LocalAuthenticationView

A SwiftUI view that displays an authentication interface.

LocalAuthentication  SwiftUI  macOS 13.0+  visionOS 1.0+  iPadOS 8.0+

    
    
    struct LocalAuthenticationView<Label> where Label : View

## Overview

Use a `LocalAuthenticationView` to display a view that prompts users to
authenticate with the app. The view visually represents the state of an
`LAPolicy` evaluation from the Local Authentication framework.

The following shows a `LocalAuthenticationView` in a Mac app with an implicit
`LAContext` instance:

If your app’s authorization flow reuses an existing `LAContext`, pass it as
part of initializing a `LocalAuthenticationView` and call its
`evaluatePolicy(_:localizedReason:reply:)` method after the view appears.

## Topics

### Authenticating with an implicit context

`init(reason: Text, context: LAContext?, result: ((Result<Void, any Error>) ->
Void), label: () -> Label)`

Creates a local authentication view.

`init<S>(S, reason: Text, context: LAContext?, result: ((Result<Void, any
Error>) -> Void))`

Creates a local authentication view with a title.

`init(LocalizedStringKey, reason: Text, context: LAContext?, result:
((Result<Void, any Error>) -> Void))`

Creates a local authentication view with a localizable title.

`init(Text, reason: Text, context: LAContext?, result: ((Result<Void, any
Error>) -> Void))`

Creates a local authentication view with a title text view.

### Authenticating with a context you supply

`init<S>(S, context: LAContext)`

Creates a local authentication view with a required context.

`init(context: LAContext, label: () -> Label)`

Creates a local authentication view with a label and required context.

`init(LocalizedStringKey, context: LAContext)`

Creates a local authentication view with a localizable title and required
context.

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<Self, AccessibilityAttachmentModifier>`

Explicitly set whether this accessibility element is a direct touch area.
Direct touch areas passthrough touch events to the app rather than being
handled through an assistive technology, such as VoiceOver. The modifier
accepts an optional `AccessibilityDirectTouchOptions` option set to customize
the functionality of the direct touch area.

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Adds an accessibility zoom action to the view. Actions allow assistive
technologies, such as VoiceOver, to interact with the view by invoking the
action.

`func allowedDynamicRange(Image.DynamicRange?) -> some View`

Returns a new view configured with the specified allowed dynamic range.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) ->
some View`

Applies the given animation to all animatable values within the `body`
closure.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View`

Sets whether buttons in this view should repeatedly trigger their actions on
prolonged interactions.

`func colorEffect(Shader, isEnabled: Bool) -> some View`

Returns a new view that applies `shader` to `self` as a filter effect on the
color of each pixel.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> some View`

Adds an item-based context menu to a view.

`func coordinateSpace(NamedCoordinateSpace) -> some View`

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

`func defaultScrollAnchor(UnitPoint?) -> some View`

Associates an anchor to control which part of the scroll view’s content should
be rendered by default.

`func dialogIcon(Image?) -> some View`

Configures the icon used by dialogs within this view.

`func dialogSeverity(DialogSeverity) -> some View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
custom suppression message on macOS. Unused on other platforms.

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View`

Enables user suppression of dialogs and alerts presented within `self`, with a
default suppression message on macOS. Unused on other platforms.

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
some View`

Returns a new view that applies `shader` to `self` as a geometric distortion
effect on the location of each pixel.

`func draggable<V, T>(() -> T, preview: () -> V) -> some View`

Activates this view as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> some View`

Defines the destination of a drag and drop operation that handles the dropped
content with a closure that you specify.

`func environment<T>(T?) -> some View`

Places an observable object in the view’s environment.

`func exportableToServices<T>(() -> [T]) -> some View`

Exports items for consumption by shortcuts, quick actions, and services.

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> some View`

Exports read-write items for consumption by shortcuts, quick actions, and
services.

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View`

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to
provide a refined URL search experience: include or exclude hidden files,
allow searching by tag, etc.

`func fileDialogConfirmationLabel(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom confirmation button label.

`func fileDialogConfirmationLabel(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with custom text as a confirmation button label.

`func fileDialogConfirmationLabel<S>(S) -> some View`

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

`func fileDialogMessage(LocalizedStringKey) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogMessage(Text?) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user, similar to a title.

`func fileDialogMessage<S>(S) -> some View`

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover`
with a custom message that is presented to the user, similar to a title.

`func fileDialogURLEnabled(Predicate<URL>) -> some View`

On macOS, configures the the `fileImporter` or `fileMover` to conditionally
disable presented URLs.

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

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to import multiple files.

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move an existing file to a
new location.

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View`

Presents a system dialog for allowing the user to move a collection of
existing files to a new location.

`func focusEffectDisabled(Bool) -> some View`

Adds a condition that controls whether this view can display focus effects,
such as a default focus ring or hover effect.

`func focusable(Bool, interactions: FocusInteractions) -> some View`

Specifies if the view is focusable, and if so, what focus-driven interactions
it supports.

`func focusedObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the focused view hierarchy.

`func focusedObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose state
depends on the focused view hierarchy.

`func focusedSceneObject<T>(T) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneObject<T>(T?) -> some View`

Creates a new view that exposes the provided object to other views whose whose
state depends on the active scene.

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some
View`

Creates a new view that exposes the provided value to other views whose state
depends on the active scene.

`func focusedValue<T>(T?) -> some View`

Sets the focused value for the given object type.

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
some View`

Creates a new view that exposes the provided value to other views whose state
depends on the focused view hierarchy.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`func geometryGroup() -> some View`

Isolates the geometry (e.g. position and size) of the view from its parent
view.

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some
View`

Enables importing items from services, such as Continuity Camera on macOS.

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View`

Inserts an inspector at the applied position in the view hierarchy.

`func inspectorColumnWidth(CGFloat) -> some View`

Sets a fixed, preferred width for the inspector containing this view when
presented as a trailing column.

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
some View`

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

`func invalidatableContent(Bool) -> some View`

Mark the receiver as their content might be invalidated.

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some
Keyframes) -> some View`

Loops the given keyframes continuously, updating the view using the modifiers
you apply in `body`.

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<Self>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> some View`

Plays the given keyframes when the given trigger value changes, updating the
view using the modifiers you apply in `body`.

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some
View`

Returns a new view that applies `shader` to `self` as a filter on the raster
layer created from `self`.

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View`

Tells a menu whether to dismiss after performing an action.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func navigationBarBackButtonHidden(Bool) -> some View`

Hides the navigation bar back button for the view.

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> some View`

Associates a destination view with a binding that can be used to push the view
onto a `NavigationStack`.

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> some View`

Associates a destination view with a bound value for use within a navigation
stack or navigation split view

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onChange<V>(of: V, initial: Bool, () -> Void) -> some View`

Adds a modifier for this view that fires an action when a specific value
changes.

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses a key on a hardware keyboard while the
view has focus.

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> some View`

Performs an action if the user presses one or more keys on a hardware keyboard
while the view has focus.

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> some View`

Performs an action if the user presses any key on a hardware keyboard while
the view has focus.

`func paletteSelectionEffect(PaletteSelectionEffect) -> some View`

Specifies the selection effect to apply to a palette item.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change continuously.

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) ->
Animation?) -> some View`

Animates effects that you apply to a view over a sequence of phases that
change based on a trigger.

`func presentationBackground<S>(S) -> some View`

Sets the presentation background of the enclosing sheet using a shape style.

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
some View`

Sets the presentation background of the enclosing sheet to a custom view.

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
some View`

Controls whether people can interact with the view behind a presentation.

`func presentationCompactAdaptation(PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to compact size classes.

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> some View`

Specifies how to adapt a presentation to horizontally and vertically compact
size classes.

`func presentationContentInteraction(PresentationContentInteraction) -> some
View`

Configures the behavior of swipe gestures on a presentation.

`func presentationCornerRadius(CGFloat?) -> some View`

Requests that the presentation have a specific corner radius.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View`

Configures the bounce behavior of scrollable views along the specified axis.

`func scrollClipDisabled(Bool) -> some View`

Sets whether a scroll view clips its content to its bounds.

`func scrollContentBackground(Visibility) -> some View`

Specifies the visibility of the background for scrollable views within this
view.

`func scrollIndicatorsFlash(onAppear: Bool) -> some View`

Flashes the scroll indicators of a scrollable view when it appears.

`func scrollIndicatorsFlash(trigger: some Equatable) -> some View`

Flashes the scroll indicators of scrollable views when a value changes.

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
some View`

Associates a binding to be updated when a scroll view within this view
scrolls.

`func scrollTargetBehavior(some ScrollTargetBehavior) -> some View`

Sets the scroll behavior of views scrollable in the provided axes.

`func scrollTargetLayout(isEnabled: Bool) -> some View`

Configures the outermost layout as a scroll target layout.

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View`

Applies the given transition, animating between the phases of the transition
as this view appears and disappears within the visible region of the
containing scroll view, or other container specified using the
`coordinateSpace` parameter.

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
some View`

Configures the search toolbar presentation behavior for any searchable
modifiers within this view.

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> some View`

Configures the search scopes for this view with the specified activation
strategy.

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View`

Configures the search scopes for this view.

`func searchSuggestions<S>(() -> S) -> some View`

Configures the search suggestions for this view.

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
some View`

Configures how to display search suggestions within this view.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> some View`

Marks this view as searchable, which configures the display of a search field.

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

`func selectionDisabled(Bool) -> some View`

Adds a condition that controls whether users can select this view.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes.

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> some View`

Plays the specified `feedback` when the provided `trigger` value changes and
the `condition` closure returns `true`.

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View`

Plays feedback when returned from the `feedback` closure after the provided
`trigger` value changes.

`func springLoadingBehavior(SpringLoadingBehavior) -> some View`

Sets the spring loading behavior this view.

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some
View`

Returns a new view with a symbol effect added to it.

`func symbolEffectsRemoved(Bool) -> some View`

Returns a new view with its inherited symbol image effects either removed or
left unchanged.

`func tableColumnHeaders(Visibility) -> some View`

Controls the visibility of a `Table`’s column header views.

`func textEditorStyle(some TextEditorStyle) -> some View`

Sets the style for text editors within this view.

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func toolbar(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the visibility of a bar managed by SwiftUI.

`func toolbar(removing: ToolbarDefaultItemKind?) -> some View`

Remove a toolbar item present by default

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View`

Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View`

Specifies the preferred color scheme of a bar managed by SwiftUI.

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View`

Configures the toolbar title display mode for this view.

`func toolbarTitleMenu<C>(content: () -> C) -> some View`

Configure the title menu of a toolbar.

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<Self>) -> V) -> some View`

Applies the given transaction mutation function to all animations used within
the `body` closure.

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> some
View`

Applies the given transaction mutation function to all animations used within
the view.

`func typeSelectEquivalent(LocalizedStringKey) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent(Text?) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typeSelectEquivalent<S>(S) -> some View`

Sets an explicit type select equivalent text in a collection, such as a list
or table.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
some View`

Applies effects to this view, while providing access to layout information
through a geometry proxy.

### Instance Properties

`var body: some View`

The content and behavior of the view.

### Type Aliases

`typealias Body`

The type of view representing the body of this view.

### Default Implementations

API Reference

View Implementations

## Relationships

### Conforms To

  * `View`

Structure

# SignInWithAppleButton

The view that creates the Sign in with Apple button for display.

Authentication Services  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac
Catalyst 14.2+  tvOS 14.0+  watchOS 7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    struct SignInWithAppleButton

## Topics

### Creating a button

`init(SignInWithAppleButton.Label, onRequest: (ASAuthorizationAppleIDRequest)
-> Void, onCompletion: ((Result<ASAuthorization, any Error>) -> Void))`

Creates a Sign in with Apple button.

`struct SignInWithAppleButton.Label`

The label that appears on the button.

`struct SignInWithAppleButton.Style`

The structure that defines styles that you use to control the button’s
appearance.

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<SignInWithAppleButton, AccessibilityAttachmentModifier>`

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<SignInWithAppleButton, AccessibilityAttachmentModifier>`

`func allowedDynamicRange(Image.DynamicRange?) -> View`

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> View`

`func animation<V>(Animation?, body:
(PlaceholderContentView<SignInWithAppleButton>) -> V) -> View`

`func badgeProminence(BadgeProminence) -> View`

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> View`

`func colorEffect(Shader, isEnabled: Bool) -> View`

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> View`

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> View`

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> View`

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> View`

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
View`

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> View`

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> View`

`func coordinateSpace(NamedCoordinateSpace) -> View`

`func copyable<T>(() -> [T]) -> View`

`func cuttable<T>(for: T.Type, action: () -> [T]) -> View`

`func defaultHoverEffect(HoverEffect?) -> View`

`func defaultScrollAnchor(UnitPoint?) -> View`

`func dialogIcon(Image?) -> View`

`func dialogSeverity(DialogSeverity) -> View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> View`

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> View`

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
View`

`func draggable<V, T>(() -> T, preview: () -> V) -> View`

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> View`

`func environment<T>(T?) -> View`

`func exportableToServices<T>(() -> [T]) -> View`

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> View`

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> View`

`func fileDialogConfirmationLabel(LocalizedStringKey) -> View`

`func fileDialogConfirmationLabel(Text?) -> View`

`func fileDialogConfirmationLabel<S>(S) -> View`

`func fileDialogCustomizationID(String) -> View`

`func fileDialogDefaultDirectory(URL?) -> View`

`func fileDialogImportsUnresolvedAliases(Bool) -> View`

`func fileDialogMessage(LocalizedStringKey) -> View`

`func fileDialogMessage(Text?) -> View`

`func fileDialogMessage<S>(S) -> View`

`func fileDialogURLEnabled(Predicate<URL>) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporterFilenameLabel(LocalizedStringKey) -> View`

`func fileExporterFilenameLabel(Text?) -> View`

`func fileExporterFilenameLabel<S>(S) -> View`

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> View`

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> View`

`func focusEffectDisabled(Bool) -> View`

`func focusable(Bool, interactions: FocusInteractions) -> View`

`func focusedObject<T>(T) -> View`

`func focusedObject<T>(T?) -> View`

`func focusedSceneObject<T>(T) -> View`

`func focusedSceneObject<T>(T?) -> View`

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> View`

`func focusedValue<T>(T?) -> View`

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
View`

`func fontDesign(Font.Design?) -> View`

`func fontWidth(Font.Width?) -> View`

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> View`

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> View`

`func geometryGroup() -> View`

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> View`

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> View`

`func hoverEffect(HoverEffect, isEnabled: Bool) -> View`

`func hoverEffectDisabled(Bool) -> View`

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> View`

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> View`

`func inspectorColumnWidth(CGFloat) -> View`

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
View`

`func invalidatableContent(Bool) -> View`

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<SignInWithAppleButton>, Value) -> some View,
keyframes: (Value) -> some Keyframes) -> View`

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<SignInWithAppleButton>, Value) -> some View,
keyframes: (Value) -> some Keyframes) -> View`

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> View`

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> View`

`func listRowHoverEffect(HoverEffect?) -> View`

`func listRowHoverEffectDisabled(Bool) -> View`

`func listRowSpacing(CGFloat?) -> View`

`func listSectionSpacing(CGFloat) -> View`

`func listSectionSpacing(ListSectionSpacing) -> View`

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> View`

`func monospaced(Bool) -> View`

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> View`

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> View`

`func offset(z: CGFloat) -> View`

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> View`

`func onChange<V>(of: V, initial: Bool, () -> Void) -> View`

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> View`

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> View`

`func padding3D(CGFloat) -> View`

`func padding3D(EdgeInsets3D) -> View`

`func padding3D(Edge3D.Set, CGFloat?) -> View`

`func paletteSelectionEffect(PaletteSelectionEffect) -> View`

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> View`

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> View`

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<SignInWithAppleButton>, Phase) -> some View,
animation: (Phase) -> Animation?) -> View`

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<SignInWithAppleButton>, Phase) -> some View,
animation: (Phase) -> Animation?) -> View`

`func preferredSurroundingsEffect(SurroundingsEffect?) -> View`

`func presentationBackground<S>(S) -> View`

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
View`

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
View`

`func presentationCompactAdaptation(PresentationAdaptation) -> View`

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> View`

`func presentationContentInteraction(PresentationContentInteraction) -> View`

`func presentationCornerRadius(CGFloat?) -> View`

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
View`

`func safeAreaPadding(CGFloat) -> View`

`func safeAreaPadding(EdgeInsets) -> View`

`func safeAreaPadding(Edge.Set, CGFloat?) -> View`

`func scaleEffect(CGFloat, anchor: UnitPoint) ->
ModifiedContent<SignInWithAppleButton, _UniformScaleEffect>`

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> View`

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> View`

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
View`

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> View`

`func scrollClipDisabled(Bool) -> View`

`func scrollContentBackground(Visibility) -> View`

`func scrollIndicatorsFlash(onAppear: Bool) -> View`

`func scrollIndicatorsFlash(trigger: some Equatable) -> View`

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
View`

`func scrollTargetBehavior(some ScrollTargetBehavior) -> View`

`func scrollTargetLayout(isEnabled: Bool) -> View`

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func searchDictationBehavior(TextInputDictationBehavior) -> View`

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> View`

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> View`

`func searchSuggestions<S>(() -> S) -> View`

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> View`

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> View`

`func selectionDisabled(Bool) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> View`

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> View`

`func springLoadingBehavior(SpringLoadingBehavior) -> View`

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) ->
View`

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> View`

`func symbolEffectsRemoved(Bool) -> View`

`func tableColumnHeaders(Visibility) -> View`

`func textEditorStyle(some TextEditorStyle) -> View`

`func textScale(Text.Scale, isEnabled: Bool) -> View`

`func toolbar(Visibility, for: ToolbarPlacement...) -> View`

`func toolbar(removing: ToolbarDefaultItemKind?) -> View`

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> View`

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> View`

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> View`

`func toolbarTitleMenu<C>(content: () -> C) -> View`

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<SignInWithAppleButton>) -> V) -> View`

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> View`

`func transform3DEffect(AffineTransform3D) -> View`

`func typeSelectEquivalent(LocalizedStringKey) -> View`

`func typeSelectEquivalent(Text?) -> View`

`func typeSelectEquivalent<S>(S) -> View`

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> View`

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> View`

`func upperLimbVisibility(Visibility) -> View`

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
View`

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> View`

## Relationships

### Conforms To

  * `View`

## See Also

### Sign In with Apple

Implementing User Authentication with Sign in with Apple

Provide a way for users of your app to set up an account and start using your
services.

Simplifying User Authentication in a tvOS App

Build a fluid sign-in experience for your tvOS apps using
AuthenticationServices.

Sign in with Apple Entitlement

An entitlement that lets your app use Sign in with Apple.

**Key:** com.apple.developer.applesignin

`class ASAuthorizationAppleIDProvider`

A mechanism for generating requests to authenticate users based on their Apple
ID.

`class ASAuthorizationAppleIDCredential`

A credential that results from a successful Apple ID authentication.

Instance Method

# signInWithAppleButtonStyle(_:)

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

AuthenticationServices  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  tvOS
14.0+  watchOS 7.0+

    
    
    func signInWithAppleButtonStyle(_ style: SignInWithAppleButton.Style) -> some View
    

##  Parameters

`style`

    

The sign in style to apply to this button.

## See Also

### Authorizing and authenticating

`struct LocalAuthenticationView`

A SwiftUI view that displays an authentication interface.

`struct SignInWithAppleButton`

The view that creates the Sign in with Apple button for display.

`var authorizationController: AuthorizationController`

A value provided in the SwiftUI environment that views can use to perform
authorization requests.

`var webAuthenticationSession: WebAuthenticationSession`

A value provided in the SwiftUI environment that views can use to authenticate
a user through a web service.

Instance Property

# authorizationController

A value provided in the SwiftUI environment that views can use to perform
authorization requests.

AuthenticationServices  SwiftUI  iOS 16.4+  iPadOS 16.4+  macOS 13.3+  tvOS
16.4+  watchOS 9.4+

    
    
    var authorizationController: AuthorizationController { get }

## Discussion

For example, you can perform authorization requests when the user taps a
button:

## See Also

### Authorizing and authenticating

`struct LocalAuthenticationView`

A SwiftUI view that displays an authentication interface.

`struct SignInWithAppleButton`

The view that creates the Sign in with Apple button for display.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

`var webAuthenticationSession: WebAuthenticationSession`

A value provided in the SwiftUI environment that views can use to authenticate
a user through a web service.

Instance Property

# webAuthenticationSession

A value provided in the SwiftUI environment that views can use to authenticate
a user through a web service.

AuthenticationServices  SwiftUI  iOS 16.4+  iPadOS 16.4+  macOS 13.3+  tvOS
16.4+  watchOS 9.4+

    
    
    var webAuthenticationSession: WebAuthenticationSession { get }

## Discussion

For example, you can start a web authentication session when the user taps a
button:

Use `WebAuthenticationSession/BrowserSession/ephemeral` to request that the
browser doesn’t share cookies or other browsing data between the
authentication session and the user’s normal browser session. Whether the
request is honored depends on the user’s default web browser. Safari always
honors the request.

After the user authenticates, the authentication provider redirects the
browser to a URL that uses the callback scheme. The browser detects the
redirect, dismisses itself, and the complete URL will be returned. Inspect the
URL to determine the outcome of the authentication:

The above example looks for a token stored as a query parameter. The specific
parsing that you have to do depends on how the authentication provider
structures the callback URL.

## See Also

### Authorizing and authenticating

`struct LocalAuthenticationView`

A SwiftUI view that displays an authentication interface.

`struct SignInWithAppleButton`

The view that creates the Sign in with Apple button for display.

`func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View`

Sets the style used for displaying the control (see
`SignInWithAppleButton.Style`).

`var authorizationController: AuthorizationController`

A value provided in the SwiftUI environment that views can use to perform
authorization requests.

Structure

# FamilyActivityPicker

A view in which users specify applications, web domains, and categories
without revealing their choices to the app.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+

    
    
    struct FamilyActivityPicker

## Overview

To prompt the user for their selection, create a binding to a
`FamilyActivitySelection` instance, and use the binding to create a
`FamilyActivityPicker` instance. You can then display the picker like any
SwiftUI view.

Note

A `FamilyControls/FamilyActivityPicker` shown on a parent device only displays
applications and websites from authorized child devices within the Family
Sharing Group. A `FamilyControls/FamilyActivityPicker` shown on an
individually authorized device includes applications and websites from that
same device.

To streamline this process, call the
`familyActivityPicker(isPresented:selection:)` modifier on a view in your user
interface. This modifier displays the picker view as a sheet over your user
interface when the `isPresented` binding is `true`.

When you present the `FamilyActivityPicker`, the system displays a view where
the user can select categories, applications, and web domains. As soon as the
user confirms their selection, the system updates the
`FamilyActivitySelection` binding with the user’s selections. To protect the
user’s privacy, the system uses opaque values to represent the selections.

Your app passes the selected values to the appropriate instances and methods
from the ManagedSettings and DeviceActivity frameworks.

## Topics

### Creating Activity Pickers

`init(selection: Binding<FamilyActivitySelection>)`

Creates a new activity picker.

`func familyActivityPicker(isPresented: Binding<Bool>, selection:
Binding<FamilyActivitySelection>) -> some View`

Presents an activity picker view as a sheet.

### Accessing the Content

`var body: some View`

The content and behavior of the view.

`typealias Body`

The type of view representing the body of this view.

### Adding View Modifiers

API Reference

View Modifiers

Apply standard modifiers to configure the family activity picker view and the
views it contains.

### Initializers

`init(headerText: String?, footerText: String?, selection:
Binding<FamilyActivitySelection>)`

Creates a new activity picker with optional header and footer text.

### Default Implementations

API Reference

View Implementations

## Relationships

### Conforms To

  * `View`

## See Also

### User-Selected Apps and Web Domains

`struct FamilyActivitySelection`

A collection of applications, categories, and web domains selected by the
user.

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

Structure

# DeviceActivityReport

A view that reports the user’s application, category, and web domain activity
in a privacy-preserving way.

DeviceActivity  SwiftUI  iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+

    
    
    struct DeviceActivityReport

## Overview

When you create a report, the system asks your app’s device activity report
extension to provide a `View` representing the user’s device activity. To
protect the user’s privacy, your extension runs in a sandbox. This sandbox
prevents your extension from making network requests or moving sensitive
content outside the extension’s address space. The extension point identifier
for all device activity report extensions is
`com.apple.deviceactivityui.report-extension`. You can configure a report with
a custom context and filter, and then display the report like any SwiftUI
view.

The system will only provide your extension with device activity data if the
user has authorized your app for family controls on their device or on the
device(s) of children in their iCloud family. See `AuthorizationCenter` for
more details.

## Topics

### Structures

`struct Context`

A context indicating how your device activity report extension should
configure its `DeviceActivityReportView`.

### Initializers

`init(DeviceActivityReport.Context, filter: DeviceActivityFilter)`

Creates a new device activity report.

### Instance Properties

`var body: some View`

The content of the device activity report.

### Type Aliases

`typealias Body`

The type of view representing the body of this view.

### Default Implementations

API Reference

View Implementations

## Relationships

### Conforms To

  * `View`

Instance Method

# managedContentStyle(_:)

Applies a managed content style to the view.

ManagedAppDistribution  SwiftUI  iOS 17.2+  iPadOS 17.2+

    
    
    func managedContentStyle(_ style: ManagedContentStyle) -> some View
    

##  Parameters

`style`

    

The style to apply to the view.

## Return Value

The styled view.

Structure

# Chart

A SwiftUI view that displays a chart.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct Chart<Content> where Content : ChartContent

## Overview

To create a chart, instantiate a `Chart` structure with marks that display the
properties of your data. For example, suppose you have an array of
`ValuePerCategory` structures that define data points composed of a `category`
and a `value`:

You can use `BarMark` inside a chart to represent the `category` property as
different bars in the chart and the `value` property as the y value for each
bar:

This chart initializer behaves a lot like a SwiftUI `ForEach`, creating a mark
— in this case, a bar — for each of the values in the `data` array:

### Controlling data series inside a chart

You can compose more sophisticated charts by providing more than one series of
marks to the chart. For example, suppose you have profit data for two
companies:

The following chart creates two different series of `LineMark` instances with
different colors to represent the data for each company. In effect, it moves
the `ForEach` construct from the chart’s initializer into the body of the
chart, enabling you to represent multiple different series:

You indicate which series a line mark belongs to by specifying its `series`
input parameter. The above chart also uses a `RuleMark` to produce a
horizontal line segment that displays a constant threshold value across the
width of the chart:

## Topics

### Creating a Chart

`init(content: () -> Content)`

Creates a chart composed of any number of data series and individual marks.

`init<Data, C>(Data, content: (Data.Element) -> C)`

Creates a chart composed of a series of identifiable marks.

`init<Data, ID, C>(Data, id: KeyPath<Data.Element, ID>, content:
(Data.Element) -> C)`

Creates a chart composed of a series of marks.

## Relationships

### Conforms To

  * `View`

## See Also

### Charts

Creating a chart using Swift Charts

Make a chart by combining chart building blocks in SwiftUI.

Visualizing your app’s data

Build complex and interactive charts using Swift Charts.

`protocol ChartContent`

A type that represents the content that you draw on a chart.

`struct ChartContentBuilder`

A result builder that you use to compose the contents of a chart.

`struct Plot`

A mechanism for grouping chart contents into a single entity.

Structure

# SceneView

A SwiftUI view for displaying 3D SceneKit content.

SceneKit  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.2+
tvOS 14.0+  watchOS 7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    struct SceneView

## Topics

### Creating a Scene View

`init(scene: SCNScene?, pointOfView: SCNNode?, options: SceneView.Options,
preferredFramesPerSecond: Int, antialiasingMode: SCNAntialiasingMode,
delegate: (any SCNSceneRendererDelegate)?, technique: SCNTechnique?)`

`struct SceneView.Options`

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<SceneView, AccessibilityAttachmentModifier>`

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<SceneView, AccessibilityAttachmentModifier>`

`func allowedDynamicRange(Image.DynamicRange?) -> View`

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> View`

`func animation<V>(Animation?, body: (PlaceholderContentView<SceneView>) -> V)
-> View`

`func badgeProminence(BadgeProminence) -> View`

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> View`

`func colorEffect(Shader, isEnabled: Bool) -> View`

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> View`

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> View`

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> View`

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> View`

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
View`

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> View`

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> View`

`func coordinateSpace(NamedCoordinateSpace) -> View`

`func copyable<T>(() -> [T]) -> View`

`func cuttable<T>(for: T.Type, action: () -> [T]) -> View`

`func defaultHoverEffect(HoverEffect?) -> View`

`func defaultScrollAnchor(UnitPoint?) -> View`

`func dialogIcon(Image?) -> View`

`func dialogSeverity(DialogSeverity) -> View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> View`

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> View`

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
View`

`func draggable<V, T>(() -> T, preview: () -> V) -> View`

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> View`

`func environment<T>(T?) -> View`

`func exportableToServices<T>(() -> [T]) -> View`

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> View`

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> View`

`func fileDialogConfirmationLabel(LocalizedStringKey) -> View`

`func fileDialogConfirmationLabel(Text?) -> View`

`func fileDialogConfirmationLabel<S>(S) -> View`

`func fileDialogCustomizationID(String) -> View`

`func fileDialogDefaultDirectory(URL?) -> View`

`func fileDialogImportsUnresolvedAliases(Bool) -> View`

`func fileDialogMessage(LocalizedStringKey) -> View`

`func fileDialogMessage(Text?) -> View`

`func fileDialogMessage<S>(S) -> View`

`func fileDialogURLEnabled(Predicate<URL>) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporterFilenameLabel(LocalizedStringKey) -> View`

`func fileExporterFilenameLabel(Text?) -> View`

`func fileExporterFilenameLabel<S>(S) -> View`

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> View`

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> View`

`func focusEffectDisabled(Bool) -> View`

`func focusable(Bool, interactions: FocusInteractions) -> View`

`func focusedObject<T>(T) -> View`

`func focusedObject<T>(T?) -> View`

`func focusedSceneObject<T>(T) -> View`

`func focusedSceneObject<T>(T?) -> View`

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> View`

`func focusedValue<T>(T?) -> View`

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
View`

`func fontDesign(Font.Design?) -> View`

`func fontWidth(Font.Width?) -> View`

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> View`

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> View`

`func geometryGroup() -> View`

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> View`

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> View`

`func hoverEffect(HoverEffect, isEnabled: Bool) -> View`

`func hoverEffectDisabled(Bool) -> View`

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> View`

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> View`

`func inspectorColumnWidth(CGFloat) -> View`

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
View`

`func invalidatableContent(Bool) -> View`

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<SceneView>, Value) -> some View, keyframes: (Value) ->
some Keyframes) -> View`

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<SceneView>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> View`

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> View`

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> View`

`func listRowHoverEffect(HoverEffect?) -> View`

`func listRowHoverEffectDisabled(Bool) -> View`

`func listRowSpacing(CGFloat?) -> View`

`func listSectionSpacing(CGFloat) -> View`

`func listSectionSpacing(ListSectionSpacing) -> View`

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> View`

`func monospaced(Bool) -> View`

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> View`

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> View`

`func offset(z: CGFloat) -> View`

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> View`

`func onChange<V>(of: V, initial: Bool, () -> Void) -> View`

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> View`

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> View`

`func padding3D(CGFloat) -> View`

`func padding3D(EdgeInsets3D) -> View`

`func padding3D(Edge3D.Set, CGFloat?) -> View`

`func paletteSelectionEffect(PaletteSelectionEffect) -> View`

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> View`

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> View`

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<SceneView>, Phase) -> some View, animation: (Phase) ->
Animation?) -> View`

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<SceneView>, Phase) -> some View, animation: (Phase) ->
Animation?) -> View`

`func preferredSurroundingsEffect(SurroundingsEffect?) -> View`

`func presentationBackground<S>(S) -> View`

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
View`

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
View`

`func presentationCompactAdaptation(PresentationAdaptation) -> View`

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> View`

`func presentationContentInteraction(PresentationContentInteraction) -> View`

`func presentationCornerRadius(CGFloat?) -> View`

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
View`

`func safeAreaPadding(CGFloat) -> View`

`func safeAreaPadding(EdgeInsets) -> View`

`func safeAreaPadding(Edge.Set, CGFloat?) -> View`

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<SceneView,
_UniformScaleEffect>`

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> View`

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> View`

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
View`

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> View`

`func scrollClipDisabled(Bool) -> View`

`func scrollContentBackground(Visibility) -> View`

`func scrollIndicatorsFlash(onAppear: Bool) -> View`

`func scrollIndicatorsFlash(trigger: some Equatable) -> View`

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
View`

`func scrollTargetBehavior(some ScrollTargetBehavior) -> View`

`func scrollTargetLayout(isEnabled: Bool) -> View`

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func searchDictationBehavior(TextInputDictationBehavior) -> View`

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> View`

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> View`

`func searchSuggestions<S>(() -> S) -> View`

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> View`

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> View`

`func selectionDisabled(Bool) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> View`

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> View`

`func springLoadingBehavior(SpringLoadingBehavior) -> View`

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) ->
View`

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> View`

`func symbolEffectsRemoved(Bool) -> View`

`func tableColumnHeaders(Visibility) -> View`

`func textEditorStyle(some TextEditorStyle) -> View`

`func textScale(Text.Scale, isEnabled: Bool) -> View`

`func toolbar(Visibility, for: ToolbarPlacement...) -> View`

`func toolbar(removing: ToolbarDefaultItemKind?) -> View`

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> View`

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> View`

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> View`

`func toolbarTitleMenu<C>(content: () -> C) -> View`

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<SceneView>) -> V) -> View`

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> View`

`func transform3DEffect(AffineTransform3D) -> View`

`func typeSelectEquivalent(LocalizedStringKey) -> View`

`func typeSelectEquivalent(Text?) -> View`

`func typeSelectEquivalent<S>(S) -> View`

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> View`

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> View`

`func upperLimbVisibility(Visibility) -> View`

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
View`

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> View`

## Relationships

### Conforms To

  * `View`

Structure

# SpriteView

A SwiftUI view that renders a SpriteKit scene.

SpriteKit  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.2+
tvOS 14.0+  watchOS 7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    struct SpriteView

## Topics

### Creating a Sprite View

`init(scene: SKScene, transition: SKTransition?, isPaused: Bool,
preferredFramesPerSecond: Int)`

`init(scene: SKScene, transition: SKTransition?, isPaused: Bool,
preferredFramesPerSecond: Int, options: SpriteView.Options, shouldRender:
(TimeInterval) -> Bool)`

`init(scene: SKScene, transition: SKTransition?, isPaused: Bool,
preferredFramesPerSecond: Int, options: SpriteView.Options, debugOptions:
SpriteView.DebugOptions, shouldRender: (TimeInterval) -> Bool)`

`struct SpriteView.Options`

`struct SpriteView.DebugOptions`

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<SpriteView, AccessibilityAttachmentModifier>`

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<SpriteView, AccessibilityAttachmentModifier>`

`func allowedDynamicRange(Image.DynamicRange?) -> View`

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> View`

`func animation<V>(Animation?, body: (PlaceholderContentView<SpriteView>) ->
V) -> View`

`func badgeProminence(BadgeProminence) -> View`

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> View`

`func colorEffect(Shader, isEnabled: Bool) -> View`

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> View`

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> View`

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> View`

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> View`

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
View`

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> View`

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> View`

`func coordinateSpace(NamedCoordinateSpace) -> View`

`func copyable<T>(() -> [T]) -> View`

`func cuttable<T>(for: T.Type, action: () -> [T]) -> View`

`func defaultHoverEffect(HoverEffect?) -> View`

`func defaultScrollAnchor(UnitPoint?) -> View`

`func dialogIcon(Image?) -> View`

`func dialogSeverity(DialogSeverity) -> View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> View`

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> View`

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
View`

`func draggable<V, T>(() -> T, preview: () -> V) -> View`

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> View`

`func environment<T>(T?) -> View`

`func exportableToServices<T>(() -> [T]) -> View`

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> View`

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> View`

`func fileDialogConfirmationLabel(LocalizedStringKey) -> View`

`func fileDialogConfirmationLabel(Text?) -> View`

`func fileDialogConfirmationLabel<S>(S) -> View`

`func fileDialogCustomizationID(String) -> View`

`func fileDialogDefaultDirectory(URL?) -> View`

`func fileDialogImportsUnresolvedAliases(Bool) -> View`

`func fileDialogMessage(LocalizedStringKey) -> View`

`func fileDialogMessage(Text?) -> View`

`func fileDialogMessage<S>(S) -> View`

`func fileDialogURLEnabled(Predicate<URL>) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporterFilenameLabel(LocalizedStringKey) -> View`

`func fileExporterFilenameLabel(Text?) -> View`

`func fileExporterFilenameLabel<S>(S) -> View`

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> View`

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> View`

`func focusEffectDisabled(Bool) -> View`

`func focusable(Bool, interactions: FocusInteractions) -> View`

`func focusedObject<T>(T) -> View`

`func focusedObject<T>(T?) -> View`

`func focusedSceneObject<T>(T) -> View`

`func focusedSceneObject<T>(T?) -> View`

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> View`

`func focusedValue<T>(T?) -> View`

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
View`

`func fontDesign(Font.Design?) -> View`

`func fontWidth(Font.Width?) -> View`

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> View`

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> View`

`func geometryGroup() -> View`

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> View`

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> View`

`func hoverEffect(HoverEffect, isEnabled: Bool) -> View`

`func hoverEffectDisabled(Bool) -> View`

`func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> View`

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> View`

`func inspectorColumnWidth(CGFloat) -> View`

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
View`

`func invalidatableContent(Bool) -> View`

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<SpriteView>, Value) -> some View, keyframes: (Value)
-> some Keyframes) -> View`

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<SpriteView>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> View`

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> View`

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> View`

`func listRowHoverEffect(HoverEffect?) -> View`

`func listRowHoverEffectDisabled(Bool) -> View`

`func listRowSpacing(CGFloat?) -> View`

`func listSectionSpacing(CGFloat) -> View`

`func listSectionSpacing(ListSectionSpacing) -> View`

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> View`

`func monospaced(Bool) -> View`

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> View`

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> View`

`func offset(z: CGFloat) -> View`

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> View`

`func onChange<V>(of: V, initial: Bool, () -> Void) -> View`

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> View`

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> View`

`func padding3D(CGFloat) -> View`

`func padding3D(EdgeInsets3D) -> View`

`func padding3D(Edge3D.Set, CGFloat?) -> View`

`func paletteSelectionEffect(PaletteSelectionEffect) -> View`

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> View`

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> View`

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<SpriteView>, Phase) -> some View, animation: (Phase)
-> Animation?) -> View`

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<SpriteView>, Phase) -> some View, animation: (Phase)
-> Animation?) -> View`

`func preferredSurroundingsEffect(SurroundingsEffect?) -> View`

`func presentationBackground<S>(S) -> View`

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
View`

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
View`

`func presentationCompactAdaptation(PresentationAdaptation) -> View`

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> View`

`func presentationContentInteraction(PresentationContentInteraction) -> View`

`func presentationCornerRadius(CGFloat?) -> View`

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
View`

`func safeAreaPadding(CGFloat) -> View`

`func safeAreaPadding(EdgeInsets) -> View`

`func safeAreaPadding(Edge.Set, CGFloat?) -> View`

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<SpriteView,
_UniformScaleEffect>`

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> View`

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> View`

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
View`

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> View`

`func scrollClipDisabled(Bool) -> View`

`func scrollContentBackground(Visibility) -> View`

`func scrollIndicatorsFlash(onAppear: Bool) -> View`

`func scrollIndicatorsFlash(trigger: some Equatable) -> View`

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
View`

`func scrollTargetBehavior(some ScrollTargetBehavior) -> View`

`func scrollTargetLayout(isEnabled: Bool) -> View`

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func searchDictationBehavior(TextInputDictationBehavior) -> View`

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> View`

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> View`

`func searchSuggestions<S>(() -> S) -> View`

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> View`

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> View`

`func selectionDisabled(Bool) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> View`

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> View`

`func springLoadingBehavior(SpringLoadingBehavior) -> View`

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) ->
View`

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> View`

`func symbolEffectsRemoved(Bool) -> View`

`func tableColumnHeaders(Visibility) -> View`

`func textEditorStyle(some TextEditorStyle) -> View`

`func textScale(Text.Scale, isEnabled: Bool) -> View`

`func toolbar(Visibility, for: ToolbarPlacement...) -> View`

`func toolbar(removing: ToolbarDefaultItemKind?) -> View`

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> View`

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> View`

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> View`

`func toolbarTitleMenu<C>(content: () -> C) -> View`

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<SpriteView>) -> V) -> View`

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> View`

`func transform3DEffect(AffineTransform3D) -> View`

`func typeSelectEquivalent(LocalizedStringKey) -> View`

`func typeSelectEquivalent(Text?) -> View`

`func typeSelectEquivalent<S>(S) -> View`

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> View`

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> View`

`func upperLimbVisibility(Visibility) -> View`

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
View`

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> View`

## Relationships

### Conforms To

  * `View`

Structure

# LocationButton

A SwiftUI button that grants one-time location authorization.

CoreLocationUI  SwiftUI  iOS 15.0+  Mac Catalyst 15.0+  watchOS 8.0+  iPadOS
15.0+

    
    
    struct LocationButton

## Overview

`LocationButton` simplifies requesting one-time authorization to access
location data. Add this button to your SwiftUI user interface in situations
when users may want to grant temporary access to their location data each time
they use a particular feature of your app.

The first time a user taps this button, Core Location asks the user to confirm
that they’re comfortable using this UI element when they want to grant
temporary access to their location data. If the user agrees, the app receives
temporary `CLAuthorizationStatus.authorizedWhenInUse` authorization, like when
the user chooses _Allow Once_ in response to your app’s standard location
authorization request. This temporary authorization expires when your app is
no longer in use.

After the user agrees to using `LocationButton`, the button becomes approved
to request future authorizations without displaying an additional alert to the
user. The next time the user taps it, this button simply grants one-time
authorization without requiring confirmation.

After you receive this temporary authorization, fetch the user’s location
using the Core Location API and perform any app-specific tasks related to that
location data. Connect the button to initiate the tasks you want to perform
after getting authorization by specifying an action when you create the
button. Keep in mind that this action activates every time the user taps this
button, regardless of whether the app already has location authorization.

Create a `LocationButton` in SwiftUI like this:

Important

When a user taps the button, it only provides one-time authorization to fetch
location data — not the location data itself. For more details about fetching
location data, see Configuring your app to use location services.

Configure the button to display an icon, a label, or both using the
`labelStyle(_:)` view modifier. If you include an icon, you can customize its
appearance using the `symbolVariant(_:)` modifier. For design guidance, see
Human Interface Guidelines.

## Topics

### Creating a location button

`init(LocationButton.Title?, action: (() -> Void))`

Creates a location button with the specified title and action.

`struct Title`

Constants that specify the text of a button title.

### Instance Properties

`var body: some View`

The content and behavior of the view.

### Type Aliases

`typealias Body`

The type of view representing the body of this view.

### Default Implementations

API Reference

View Implementations

## Relationships

### Conforms To

  * `View`

## See Also

### Location authorization

Sharing Your Location to Find a Park

Ask for location access using a customizable location button.

`class CLLocationButton`

A button that grants one-time location authorization.

Generic Structure

# Map

A view that displays an embedded map interface.

MapKit  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+
tvOS 14.0+  watchOS 7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    struct Map<Content> where Content : View

## Overview

Use this SwiftUI view to display a `Map` with markers, annotations, and custom
content you provide. You can configure the `Map` to optionally display the
user’s location, track a location, and display various controls to allow them
to interact with and control the map’s display. The following example displays
a map of downtown San Francisco that shows different markers, and an
annotation with custom view content at specific locations:

You create markers, annotations, and overlays using `MapContentBuilder` with
any of several `MapContent` types including:

  * `Annotation`

  * `UserAnnotation`

  * `Marker`

  * `MapCircle`

  * `MapPolygon`

  * `MapPolyline`

You can also add a variety of controls to allow a person to interact with the
map to change the map’s scale, display or hide the device’s current location,
and so on:

  * `MapCompass`

  * `MapPitchButton`

  * `MapPitchSlider`

  * `MapScaleView`

  * `MapUserLocationButton`

  * `MapZoomStepper`

## Topics

### Creating a map

`init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope:
Namespace.ID?)`

Creates a new, empty map with the bounds, interaction modes, and scope you
provide.

`init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes,
scope: Namespace.ID?, content: () -> C)`

Creates a new map with the bounds, interaction modes, scope, and content you
provide.

`init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes,
selection: Binding<MapFeature?>, scope: Namespace.ID?)`

Creates a new, empty map with the bounds, interaction modes, a binding to a
map feature, and scope you provide.

`init<SelectedValue>(bounds: MapCameraBounds?, interactionModes:
MapInteractionModes, selection: Binding<SelectedValue?>, scope:
Namespace.ID?)`

Creates a new, empty map with the bounds, interaction modes, the selected map
feature, and scope you provide.

`init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes,
selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)`

Creates a new map with the bounds, interaction modes, selected map feature,
scope, and map content you provide.

`init<SelectedValue, C>(bounds: MapCameraBounds?, interactionModes:
MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?,
content: () -> C)`

Creates a new map with the bounds, interaction modes, selected value, scope,
and map content you provide.

`init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, scope: Namespace.ID?)`

Creates a new, empty map with the initial camera position, bounds, interaction
modes, and scope you provide.

`init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () ->
C)`

Creates a new map with the initial camera position, bounds, interaction modes,
scope, and map content you provide.

`init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope:
Namespace.ID?)`

Creates a new, empty map with the initial camera position, bounds, interaction
modes, selected map feature, and scope you provide.

`init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope:
Namespace.ID?, content: () -> C)`

Creates a new map with the initial camera position, bounds, interaction modes,
selected map feature, scope, and content you provide.

`init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds:
MapCameraBounds?, interactionModes: MapInteractionModes, selection:
Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)`

Creates a new map with the initial camera position, bounds, interaction modes,
selected map feature, scope, and content you provide.

`init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, scope: Namespace.ID?)`

Creates a new, empty map with the initial camera position, bounds, interaction
modes, and scope you provide.

`init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () ->
C)`

Creates a new map with the initial camera position, bounds, interaction modes,
scope, and content you provide.

`init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope:
Namespace.ID?)`

Creates a new map with the initial camera position, bounds, interaction modes,
scope, and content you provide.

`init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?,
interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope:
Namespace.ID?, content: () -> C)`

Creates a new map with the initial camera position, bounds, interaction modes,
selected feature, scope, and content you provide.

`init<SelectedValue, C>(position: Binding<MapCameraPosition>, bounds:
MapCameraBounds?, interactionModes: MapInteractionModes, selection:
Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)`

Creates a new map with the initial camera position, bounds, interaction modes,
selected feature, scope, and content you provide.

`struct MapInteractionModes`

Options that indicate the user interactions that the map responds to.

### Accessing the view body

`var body: View`

The content and behavior of the view.

### Managing feature selection

`func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) ->
View`

Specifies a custom presentation for the currently selected feature.

`func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> View`

Specifies which map features should have selection disabled.

### Managing Look Around view presentation

`func lookAroundViewer(isPresented: Binding<Bool>, initialScene:
MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool,
pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) ->
View`

Presents a Look Around view with the scene, navigation, road label, and points
of interest characteristics you provide.

`func lookAroundViewer(isPresented: Binding<Bool>, scene:
Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool,
pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) ->
View`

Presents a Look Around view with a binding to a scene, and navigation, road
label, and points of interest characteristics you provide.

### Managing map control sizing and visibility

`func mapControlVisibility(Visibility) -> View`

Configures all Map controls in the environment to have the specified
visibility.

`func mapControls(() -> some View) -> View`

Configures all map views in the associated environment to have standard sized
and positioned controls.

### Managing the camera

`func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes:
(MapCamera) -> some Keyframes<MapCamera>) -> View`

Uses the keyframes you provide to animate the camera of a map when the value
you provide changes.

`func onMapCameraChange(frequency: MapCameraUpdateFrequency,
(MapCameraUpdateContext) -> Void) -> View`

Performs an action when Map camera framing changes that calls a closure that
provides the map camera and the area the camera frames.

`func onMapCameraChange(frequency: MapCameraUpdateFrequency, () -> Void) ->
View`

Performs an action when Map camera framing changes.

### Setting the namespace Identifier

`func mapScope(Namespace.ID) -> View`

Creates a namespace that SwiftUI uses to connect map controls to an associated
map.

### Setting the map style

`func mapStyle(MapStyle) -> View`

Specifies the map style to use.

### Type aliases

`typealias Map.Body`

The content and behavior of the view.

### Deprecated

API Reference

Deprecated Symbols

Map protocols and view modifiers that are no longer supported.

### Initializers

`init<SelectedValue, C>(bounds: MapCameraBounds?, interactionModes:
MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?,
content: () -> C)`

`init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds:
MapCameraBounds?, interactionModes: MapInteractionModes, selection:
Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)`

`init<SelectedValue, C>(position: Binding<MapCameraPosition>, bounds:
MapCameraBounds?, interactionModes: MapInteractionModes, selection:
Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)`

### Instance Methods

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

## Relationships

### Conforms To

  * `View`

## See Also

### Essentials

`struct MapStyle`

A style that you can apply to a map.

Structure

# CameraView

A SwiftUI view into which a video stream or an image snapshot is rendered.

HomeKit  SwiftUI  iOS 14.0+  iPadOS 14.0+  Mac Catalyst 16.2+  tvOS 14.0+
watchOS 7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    struct CameraView

## Topics

### Creating a camera view

`init(source: HMCameraSource)`

Creates a new camera view using the given source.

`class HMCameraSource`

An abstract class for a camera’s data source.

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<CameraView, AccessibilityAttachmentModifier>`

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<CameraView, AccessibilityAttachmentModifier>`

`func allowedDynamicRange(Image.DynamicRange?) -> View`

`func animation<V>(Animation?, body: (PlaceholderContentView<CameraView>) ->
V) -> View`

`func badgeProminence(BadgeProminence) -> View`

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> View`

`func colorEffect(Shader, isEnabled: Bool) -> View`

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> View`

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> View`

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> View`

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> View`

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
View`

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> View`

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> View`

`func coordinateSpace(NamedCoordinateSpace) -> View`

`func defaultHoverEffect(HoverEffect?) -> View`

`func defaultScrollAnchor(UnitPoint?) -> View`

`func dialogIcon(Image?) -> View`

`func dialogSeverity(DialogSeverity) -> View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> View`

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> View`

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
View`

`func draggable<V, T>(() -> T, preview: () -> V) -> View`

`func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool,
isTargeted: (Bool) -> Void) -> View`

`func environment<T>(T?) -> View`

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> View`

`func fileDialogConfirmationLabel(LocalizedStringKey) -> View`

`func fileDialogConfirmationLabel(Text?) -> View`

`func fileDialogConfirmationLabel<S>(S) -> View`

`func fileDialogCustomizationID(String) -> View`

`func fileDialogDefaultDirectory(URL?) -> View`

`func fileDialogImportsUnresolvedAliases(Bool) -> View`

`func fileDialogMessage(LocalizedStringKey) -> View`

`func fileDialogMessage(Text?) -> View`

`func fileDialogMessage<S>(S) -> View`

`func fileDialogURLEnabled(Predicate<URL>) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporterFilenameLabel(LocalizedStringKey) -> View`

`func fileExporterFilenameLabel(Text?) -> View`

`func fileExporterFilenameLabel<S>(S) -> View`

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> View`

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> View`

`func focusEffectDisabled(Bool) -> View`

`func focusable(Bool, interactions: FocusInteractions) -> View`

`func focusedObject<T>(T) -> View`

`func focusedObject<T>(T?) -> View`

`func focusedSceneObject<T>(T) -> View`

`func focusedSceneObject<T>(T?) -> View`

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> View`

`func focusedValue<T>(T?) -> View`

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
View`

`func fontDesign(Font.Design?) -> View`

`func fontWidth(Font.Width?) -> View`

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> View`

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> View`

`func geometryGroup() -> View`

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> View`

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> View`

`func hoverEffect(HoverEffect, isEnabled: Bool) -> View`

`func hoverEffectDisabled(Bool) -> View`

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> View`

`func inspectorColumnWidth(CGFloat) -> View`

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
View`

`func invalidatableContent(Bool) -> View`

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<CameraView>, Value) -> some View, keyframes: (Value)
-> some Keyframes) -> View`

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<CameraView>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> View`

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> View`

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> View`

`func listRowHoverEffect(HoverEffect?) -> View`

`func listRowHoverEffectDisabled(Bool) -> View`

`func listRowSpacing(CGFloat?) -> View`

`func listSectionSpacing(CGFloat) -> View`

`func listSectionSpacing(ListSectionSpacing) -> View`

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> View`

`func monospaced(Bool) -> View`

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> View`

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> View`

`func navigationSubtitle(LocalizedStringKey) -> View`

`func navigationSubtitle(Text) -> View`

`func navigationSubtitle<S>(S) -> View`

`func offset(z: CGFloat) -> View`

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> View`

`func onChange<V>(of: V, initial: Bool, () -> Void) -> View`

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> View`

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> View`

`func padding3D(CGFloat) -> View`

`func padding3D(EdgeInsets3D) -> View`

`func padding3D(Edge3D.Set, CGFloat?) -> View`

`func paletteSelectionEffect(PaletteSelectionEffect) -> View`

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> View`

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<CameraView>, Phase) -> some View, animation: (Phase)
-> Animation?) -> View`

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<CameraView>, Phase) -> some View, animation: (Phase)
-> Animation?) -> View`

`func preferredSurroundingsEffect(SurroundingsEffect?) -> View`

`func presentationBackground<S>(S) -> View`

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
View`

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
View`

`func presentationCompactAdaptation(PresentationAdaptation) -> View`

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> View`

`func presentationContentInteraction(PresentationContentInteraction) -> View`

`func presentationCornerRadius(CGFloat?) -> View`

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
View`

`func safeAreaPadding(CGFloat) -> View`

`func safeAreaPadding(EdgeInsets) -> View`

`func safeAreaPadding(Edge.Set, CGFloat?) -> View`

`func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<CameraView,
_UniformScaleEffect>`

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> View`

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> View`

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
View`

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> View`

`func scrollClipDisabled(Bool) -> View`

`func scrollContentBackground(Visibility) -> View`

`func scrollIndicatorsFlash(onAppear: Bool) -> View`

`func scrollIndicatorsFlash(trigger: some Equatable) -> View`

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
View`

`func scrollTargetBehavior(some ScrollTargetBehavior) -> View`

`func scrollTargetLayout(isEnabled: Bool) -> View`

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func searchDictationBehavior(TextInputDictationBehavior) -> View`

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> View`

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> View`

`func searchSuggestions<S>(() -> S) -> View`

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> View`

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> View`

`func selectionDisabled(Bool) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> View`

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> View`

`func springLoadingBehavior(SpringLoadingBehavior) -> View`

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) ->
View`

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> View`

`func symbolEffectsRemoved(Bool) -> View`

`func tableColumnHeaders(Visibility) -> View`

`func textEditorStyle(some TextEditorStyle) -> View`

`func textScale(Text.Scale, isEnabled: Bool) -> View`

`func toolbar(Visibility, for: ToolbarPlacement...) -> View`

`func toolbar(removing: ToolbarDefaultItemKind?) -> View`

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> View`

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> View`

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> View`

`func toolbarTitleMenu<C>(content: () -> C) -> View`

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<CameraView>) -> V) -> View`

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> View`

`func transform3DEffect(AffineTransform3D) -> View`

`func typeSelectEquivalent(LocalizedStringKey) -> View`

`func typeSelectEquivalent(Text?) -> View`

`func typeSelectEquivalent<S>(S) -> View`

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> View`

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> View`

`func upperLimbVisibility(Visibility) -> View`

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
View`

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> View`

## Relationships

### Conforms To

  * `View`

## See Also

### Managing camera profiles

`var cameraProfiles: [HMCameraProfile]?`

An array of camera profiles implemented by the accessory.

`class HMCameraProfile`

A camera profile that interacts with an accessory's camera.

`class HMCameraView`

The view into which a video stream or an image snapshot is rendered.

Structure

# NowPlayingView

A view that displays the system’s Now Playing interface so that the user can
control audio.

WatchKit  SwiftUI  watchOS 7.0+  Xcode 12.0+

    
    
    struct NowPlayingView

## Overview

With a Now Playing view, users can control current or recently played audio
without leaving your app. The Now Playing view displays information about the
current audio source, such as another app on the user’s Apple Watch or iPhone.
For example, users can play and pause music from their Apple Watch’s Music app
or control the volume of a podcast on their iPhone.

The system automatically selects the source. If the user is listening to audio
on their watch or phone, the system selects that audio source. Otherwise, the
system selects the most recently used source.

Always present the Now Playing view so that it fills the screen in a
nonscrolling container. Don’t add any other elements to the view.

## Topics

### Creating a Now Playing View

`init()`

Creates a view that displays the system’s Now Playing interface.

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<NowPlayingView, AccessibilityAttachmentModifier>`

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<NowPlayingView, AccessibilityAttachmentModifier>`

`func animation<V>(Animation?, body: (PlaceholderContentView<NowPlayingView>)
-> V) -> View`

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> View`

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> View`

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> View`

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> View`

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> View`

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
View`

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> View`

`func coordinateSpace(NamedCoordinateSpace) -> View`

`func datePickerStyle<S>(S) -> View`

`func defaultScrollAnchor(UnitPoint?) -> View`

`func dialogIcon(Image?) -> View`

`func dialogSeverity(DialogSeverity) -> View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> View`

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> View`

`func environment<T>(T?) -> View`

`func focusEffectDisabled(Bool) -> View`

`func focusable(Bool, interactions: FocusInteractions) -> View`

`func focusedObject<T>(T) -> View`

`func focusedObject<T>(T?) -> View`

`func focusedSceneObject<T>(T) -> View`

`func focusedSceneObject<T>(T?) -> View`

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> View`

`func focusedValue<T>(T?) -> View`

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
View`

`func fontDesign(Font.Design?) -> View`

`func fontWidth(Font.Width?) -> View`

`func geometryGroup() -> View`

`func invalidatableContent(Bool) -> View`

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<NowPlayingView>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> View`

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<NowPlayingView>, Value) -> some View,
keyframes: (Value) -> some Keyframes) -> View`

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> View`

`func listSectionSpacing(CGFloat) -> View`

`func listSectionSpacing(ListSectionSpacing) -> View`

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> View`

`func monospaced(Bool) -> View`

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> View`

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> View`

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> View`

`func onChange<V>(of: V, initial: Bool, () -> Void) -> View`

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<NowPlayingView>, Phase) -> some View, animation:
(Phase) -> Animation?) -> View`

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<NowPlayingView>, Phase) -> some View, animation:
(Phase) -> Animation?) -> View`

`func presentationBackground<S>(S) -> View`

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
View`

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
View`

`func presentationCompactAdaptation(PresentationAdaptation) -> View`

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> View`

`func presentationContentInteraction(PresentationContentInteraction) -> View`

`func presentationCornerRadius(CGFloat?) -> View`

`func safeAreaPadding(CGFloat) -> View`

`func safeAreaPadding(EdgeInsets) -> View`

`func safeAreaPadding(Edge.Set, CGFloat?) -> View`

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> View`

`func scrollClipDisabled(Bool) -> View`

`func scrollContentBackground(Visibility) -> View`

`func scrollIndicatorsFlash(onAppear: Bool) -> View`

`func scrollIndicatorsFlash(trigger: some Equatable) -> View`

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
View`

`func scrollTargetBehavior(some ScrollTargetBehavior) -> View`

`func scrollTargetLayout(isEnabled: Bool) -> View`

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

`func searchSuggestions<S>(() -> S) -> View`

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
View`

`func selectionDisabled(Bool) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> View`

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> View`

`func springLoadingBehavior(SpringLoadingBehavior) -> View`

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) ->
View`

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> View`

`func symbolEffectsRemoved(Bool) -> View`

`func textScale(Text.Scale, isEnabled: Bool) -> View`

`func toolbar(Visibility, for: ToolbarPlacement...) -> View`

`func toolbar(removing: ToolbarDefaultItemKind?) -> View`

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> View`

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> View`

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> View`

`func toolbarTitleMenu<C>(content: () -> C) -> View`

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<NowPlayingView>) -> V) -> View`

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> View`

`func typeSelectEquivalent(LocalizedStringKey) -> View`

`func typeSelectEquivalent(Text?) -> View`

`func typeSelectEquivalent<S>(S) -> View`

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> View`

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> View`

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
View`

## Relationships

### Conforms To

  * `View`

## See Also

### User interface

API Reference

Storyboard support

Connect your code to storyboard elements using interface controllers,
interface objects, and event handlers.

Generic Structure

# VideoPlayer

A view that displays content from a player and a native user interface to
control playback.

AVKit  SwiftUI  iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS
14.0+  watchOS 7.0+  visionOS 1.0+  Xcode 12.0+

    
    
    struct VideoPlayer<VideoOverlay> where VideoOverlay : View

## Overview

## Topics

### Creating a Video Player

`init(player: AVPlayer?)`

Creates a video-player user interface for the player object.

Available when `VideoOverlay` is `EmptyView`.

`init(player: AVPlayer?, videoOverlay: () -> VideoOverlay)`

Creates a video-player user interface for the player object.

## Relationships

### Conforms To

  * `View`

## See Also

### Multiplatform Playback and Capture

`func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect:
((AVContinuityDevice?) -> Void)?) -> View`

Presents an interface a person uses to select a nearby continuity device and
connect to their Apple TV.

Generic Structure

# PhotosPicker

A view that displays a Photos picker for choosing assets from the photo
library.

PhotosUI  SwiftUI  iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+
watchOS 9.0+  visionOS 1.0+  Xcode 14.0+

    
    
    struct PhotosPicker<Label> where Label : View

## Overview

Use the Photos picker view to browse and select images and vidoes from the
photo library. The view contains methods for single selection and multiple
selection. For example, the following code displays a button that — when
pressed — shows a picker in multiple selection mode.

When displaying the picker, you can use `PHPickerFilter` options to customize
what it displays. For example, the following code displays `images` and
excludes `screenshots`.

The selection results you get are placeholder objects. A `PhotosPickerItem`
conforms to `Transferable`, and allows you to load a representation you
request. To load a SwiftUI `Image` and track progress, use
`loadTransferable(type:completionHandler:)`.

A failure can occur when the system attempts to retrieve the data. For
example, if the picker tries to download data from iCloud Photos without a
network connection.

Important

`Image` only supports `PNG` file types through its `Transferable` conformance,
so you need to create a custom `Transferable` model to support other image
types. See Bringing Photos picker to your SwiftUI app to learn more.

## Topics

### Creating a picker

`init(selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, label:
() -> Label)`

Creates a picker that selects an item and optionally configures the types of
items to show, item encoding, and label behavior.

`init(selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?,
selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, label:
() -> Label)`

Creates a picker that selects a collection of items and optionally configures
the max selection count, selection behavior, types of items to show, item
encoding, and label behavior.

`init(selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary, label: () -> Label)`

Creates a picker that selects an item from the photo library you specify and
optionally configures the types of items to show, item encoding, and label
behavior.

`init(selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?,
selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary, label: () -> Label)`

Creates a picker that selects a collection of items from the photo library you
specify and optionally configures the max selection count, selection behavior,
types of items to show, item encoding, and label behavior.

### Creating a picker with a title

`init(LocalizedStringKey, selection: Binding<PhotosPickerItem?>, matching:
PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy)`

Creates a picker with a title key and selection, and optionally configures the
types of items to show and item encoding behavior.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)`

Creates a picker with a title and selection, and optionally configures the
types of items to show and item encoding behavior.

Available when `Label` is `Text`.

`init(LocalizedStringKey, selection: Binding<[PhotosPickerItem]>,
maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior,
matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy)`

Creates a picker with a title key and selection, and optionally configures the
max selection count, selection behavior, types of items to show, item
encoding, and label behavior.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?,
selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)`

Creates a picker with a title and selection, and optionally configures the max
selection count, selection behavior, types of items to show, item encoding,
and label behavior.

Available when `Label` is `Text`.

`init(LocalizedStringKey, selection: Binding<PhotosPickerItem?>, matching:
PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)`

Creates a picker with a title key and selection from the photo library you
specify, and optionally configures the types of items to show, item encoding,
and label behavior.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary)`

Creates a picker with a title and selection from the photo library you
specify, and optionally configures the types of items to show, item encoding,
and label behavior.

Available when `Label` is `Text`.

`init(LocalizedStringKey, selection: Binding<[PhotosPickerItem]>,
maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior,
matching: PHPickerFilter?, preferredItemEncoding:
PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)`

Creates a picker with a title key and selection from the photo library you
specify, and optionally configures the max selection count, selection
behavior, types of items to show, item encoding, and label behavior.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?,
selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?,
preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy,
photoLibrary: PHPhotoLibrary)`

Creates a picker with a title and selection from the photo library you
specify, and optionally configures the max selection count, selection
behavior, types of items to show, item encoding, and label behavior.

Available when `Label` is `Text`.

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<PhotosPicker<Label>, AccessibilityAttachmentModifier>`

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<PhotosPicker<Label>, AccessibilityAttachmentModifier>`

`func allowedDynamicRange(Image.DynamicRange?) -> View`

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> View`

`func animation<V>(Animation?, body:
(PlaceholderContentView<PhotosPicker<Label>>) -> V) -> View`

`func badgeProminence(BadgeProminence) -> View`

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> View`

`func colorEffect(Shader, isEnabled: Bool) -> View`

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> View`

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> View`

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> View`

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> View`

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
View`

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> View`

`func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M,
primaryAction: ((Set<I>) -> Void)?) -> View`

`func coordinateSpace(NamedCoordinateSpace) -> View`

`func copyable<T>(() -> [T]) -> View`

`func cuttable<T>(for: T.Type, action: () -> [T]) -> View`

`func defaultHoverEffect(HoverEffect?) -> View`

`func defaultScrollAnchor(UnitPoint?) -> View`

`func dialogIcon(Image?) -> View`

`func dialogSeverity(DialogSeverity) -> View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> View`

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> View`

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
View`

`func environment<T>(T?) -> View`

`func exportableToServices<T>(() -> [T]) -> View`

`func exportableToServices<T>(() -> [T], onEdit: ([T]) -> Bool) -> View`

`func fileDialogBrowserOptions(FileDialogBrowserOptions) -> View`

`func fileDialogConfirmationLabel(LocalizedStringKey) -> View`

`func fileDialogConfirmationLabel(Text?) -> View`

`func fileDialogConfirmationLabel<S>(S) -> View`

`func fileDialogCustomizationID(String) -> View`

`func fileDialogDefaultDirectory(URL?) -> View`

`func fileDialogImportsUnresolvedAliases(Bool) -> View`

`func fileDialogMessage(LocalizedStringKey) -> View`

`func fileDialogMessage(Text?) -> View`

`func fileDialogMessage<S>(S) -> View`

`func fileDialogURLEnabled(Predicate<URL>) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes:
[UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes:
[UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: ()
-> Void) -> View`

`func fileExporterFilenameLabel(LocalizedStringKey) -> View`

`func fileExporterFilenameLabel(Text?) -> View`

`func fileExporterFilenameLabel<S>(S) -> View`

`func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType],
allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) ->
Void, onCancellation: () -> Void) -> View`

`func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion:
(Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> View`

`func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion:
(Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> View`

`func focusEffectDisabled(Bool) -> View`

`func focusable(Bool, interactions: FocusInteractions) -> View`

`func focusedValue<T>(T?) -> View`

`func fontDesign(Font.Design?) -> View`

`func fontWidth(Font.Width?) -> View`

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> View`

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> View`

`func geometryGroup() -> View`

`func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> View`

`func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode)
-> View`

`func hoverEffect(HoverEffect, isEnabled: Bool) -> View`

`func hoverEffectDisabled(Bool) -> View`

`func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> View`

`func inspectorColumnWidth(CGFloat) -> View`

`func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) ->
View`

`func invalidatableContent(Bool) -> View`

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<PhotosPicker<Label>>, Value) -> some View, keyframes:
(Value) -> some Keyframes) -> View`

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<PhotosPicker<Label>>, Value) -> some View,
keyframes: (Value) -> some Keyframes) -> View`

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> View`

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> View`

`func listRowHoverEffect(HoverEffect?) -> View`

`func listRowHoverEffectDisabled(Bool) -> View`

`func listRowSpacing(CGFloat?) -> View`

`func listSectionSpacing(CGFloat) -> View`

`func listSectionSpacing(ListSectionSpacing) -> View`

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> View`

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> View`

`func offset(z: CGFloat) -> View`

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> View`

`func onChange<V>(of: V, initial: Bool, () -> Void) -> View`

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> View`

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func ornament<Content>(visibility: Visibility, attachmentAnchor:
OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () ->
Content) -> View`

`func padding3D(CGFloat) -> View`

`func padding3D(EdgeInsets3D) -> View`

`func padding3D(Edge3D.Set, CGFloat?) -> View`

`func paletteSelectionEffect(PaletteSelectionEffect) -> View`

`func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z:
CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> View`

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<PhotosPicker<Label>>, Phase) -> some View, animation:
(Phase) -> Animation?) -> View`

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<PhotosPicker<Label>>, Phase) -> some View, animation:
(Phase) -> Animation?) -> View`

`func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> View`

`func photosPickerDisabledCapabilities(PHPickerCapabilities) -> View`

`func photosPickerStyle(PhotosPickerStyle) -> View`

`func preferredSurroundingsEffect(SurroundingsEffect?) -> View`

`func presentationBackground<S>(S) -> View`

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
View`

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
View`

`func presentationCompactAdaptation(PresentationAdaptation) -> View`

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> View`

`func presentationContentInteraction(PresentationContentInteraction) -> View`

`func presentationCornerRadius(CGFloat?) -> View`

`func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat),
anchor: UnitPoint3D) -> View`

`func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) ->
View`

`func safeAreaPadding(CGFloat) -> View`

`func safeAreaPadding(EdgeInsets) -> View`

`func safeAreaPadding(Edge.Set, CGFloat?) -> View`

`func scaleEffect(CGFloat, anchor: UnitPoint) ->
ModifiedContent<PhotosPicker<Label>, _UniformScaleEffect>`

`func scaleEffect(CGFloat, anchor: UnitPoint3D) -> View`

`func scaleEffect(Size3D, anchor: UnitPoint3D) -> View`

`func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) ->
View`

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> View`

`func scrollClipDisabled(Bool) -> View`

`func scrollIndicatorsFlash(onAppear: Bool) -> View`

`func scrollIndicatorsFlash(trigger: some Equatable) -> View`

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
View`

`func scrollTargetBehavior(some ScrollTargetBehavior) -> View`

`func scrollTargetLayout(isEnabled: Bool) -> View`

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func searchDictationBehavior(TextInputDictationBehavior) -> View`

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt:
LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?,
token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some
StringProtocol, token: (Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: LocalizedStringKey, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) ->
some View) -> View`

`func searchable<C>(text: Binding<String>, editableTokens: Binding<C>,
placement: SearchFieldPlacement, prompt: some StringProtocol, token:
(Binding<C.Element>) -> some View) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey) -> View`

`func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?) -> View`

`func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>,
placement: SearchFieldPlacement, prompt: S) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey,
token: (C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented:
Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token:
(C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token:
(C.Element) -> T) -> View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) ->
View`

`func searchable<C, T>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> View`

`func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>,
suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement:
SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> View`

`func selectionDisabled(Bool) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> View`

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> View`

`func springLoadingBehavior(SpringLoadingBehavior) -> View`

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) ->
View`

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> View`

`func symbolEffectsRemoved(Bool) -> View`

`func tableColumnHeaders(Visibility) -> View`

`func textEditorStyle(some TextEditorStyle) -> View`

`func textScale(Text.Scale, isEnabled: Bool) -> View`

`func toolbar(removing: ToolbarDefaultItemKind?) -> View`

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> View`

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<PhotosPicker<Label>>) -> V) -> View`

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> View`

`func transform3DEffect(AffineTransform3D) -> View`

`func typeSelectEquivalent(LocalizedStringKey) -> View`

`func typeSelectEquivalent(Text?) -> View`

`func typeSelectEquivalent<S>(S) -> View`

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> View`

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> View`

`func upperLimbVisibility(Visibility) -> View`

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
View`

`func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some
VisualEffect) -> View`

## Relationships

### Conforms To

  * `View`

## See Also

### Photos Picker for SwiftUI

Bringing Photos picker to your SwiftUI app

Select media assets by using a Photos picker view that SwiftUI provides.

Implementing an inline Photos picker

Embed a system-provided, half-height Photos picker into your app’s view.

`struct PhotosPickerItem`

A type that represents an item you use with a Photos picker.

`struct PhotosPickerSelectionBehavior`

A type that describes how the Photos picker handles user selection.

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

Generic Structure

# DevicePicker

A SwiftUI view that displays other devices on the network, and creates an
encrypted connection to a copy of your app running on that device.

DeviceDiscoveryUI  SwiftUI  tvOS 16.0+  Xcode 14.0+

    
    
    struct DevicePicker<Label, Fallback> where Label : View, Fallback : View

## Overview

Always display the picker as a full-screen, modal view. If the user selects a
device, the system calls the closure you passed as the `onSelect` parameter.
If the user cancels the picker, it silently closes.

If the current device doesn’t support device discovery, the system displays
the fallback view instead of the device picker. Use the
DevicePickerSupportedAction environment value to check whether the current
device supports device discovery.

## Topics

### Creating a device picker

`init(NWBrowser.Descriptor, onSelect: (NWEndpoint) -> Void, label: () ->
Label, fallback: () -> Fallback, parameters: (() -> NWParameters)?)`

Creates a view that displays the other, available devices on your local
network.

### Instance Methods

`func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions)
-> ModifiedContent<DevicePicker<Label, Fallback>,
AccessibilityAttachmentModifier>`

`func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) ->
ModifiedContent<DevicePicker<Label, Fallback>,
AccessibilityAttachmentModifier>`

`func allowedDynamicRange(Image.DynamicRange?) -> View`

`func animation<V>(Animation?, body:
(PlaceholderContentView<DevicePicker<Label, Fallback>>) -> V) -> View`

`func buttonRepeatBehavior(ButtonRepeatBehavior) -> View`

`func colorEffect(Shader, isEnabled: Bool) -> View`

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> View`

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> View`

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> View`

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> View`

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> View`

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
View`

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> View`

`func controlGroupStyle<S>(S) -> View`

`func coordinateSpace(NamedCoordinateSpace) -> View`

`func defaultHoverEffect(HoverEffect?) -> View`

`func defaultScrollAnchor(UnitPoint?) -> View`

`func dialogIcon(Image?) -> View`

`func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>)
-> View`

`func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> View`

`func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> View`

`func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) ->
View`

`func environment<T>(T?) -> View`

`func focusEffectDisabled(Bool) -> View`

`func focusable(Bool, interactions: FocusInteractions) -> View`

`func focusedObject<T>(T) -> View`

`func focusedObject<T>(T?) -> View`

`func focusedSceneObject<T>(T) -> View`

`func focusedSceneObject<T>(T?) -> View`

`func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> View`

`func focusedValue<T>(T?) -> View`

`func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) ->
View`

`func fontDesign(Font.Design?) -> View`

`func fontWidth(Font.Width?) -> View`

`func geometryGroup() -> View`

`func hoverEffect(HoverEffect, isEnabled: Bool) -> View`

`func hoverEffectDisabled(Bool) -> View`

`func invalidatableContent(Bool) -> View`

`func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content:
(PlaceholderContentView<DevicePicker<Label, Fallback>>, Value) -> some View,
keyframes: (Value) -> some Keyframes) -> View`

`func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable,
content: (PlaceholderContentView<DevicePicker<Label, Fallback>>, Value) ->
some View, keyframes: (Value) -> some Keyframes) -> View`

`func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> View`

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> View`

`func menuActionDismissBehavior(MenuActionDismissBehavior) -> View`

`func menuIndicator(Visibility) -> View`

`func menuStyle<S>(S) -> View`

`func monospaced(Bool) -> View`

`func navigationDestination<V>(isPresented: Binding<Bool>, destination: () ->
V) -> View`

`func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D)
-> C) -> View`

`func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> View`

`func onChange<V>(of: V, initial: Bool, () -> Void) -> View`

`func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> View`

`func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action:
(KeyPress) -> KeyPress.Result) -> View`

`func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) ->
KeyPress.Result) -> View`

`func phaseAnimator<Phase>(some Sequence, content:
(PlaceholderContentView<DevicePicker<Label, Fallback>>, Phase) -> some View,
animation: (Phase) -> Animation?) -> View`

`func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content:
(PlaceholderContentView<DevicePicker<Label, Fallback>>, Phase) -> some View,
animation: (Phase) -> Animation?) -> View`

`func presentationBackground<S>(S) -> View`

`func presentationBackground<V>(alignment: Alignment, content: () -> V) ->
View`

`func presentationBackgroundInteraction(PresentationBackgroundInteraction) ->
View`

`func presentationCompactAdaptation(PresentationAdaptation) -> View`

`func presentationCompactAdaptation(horizontal: PresentationAdaptation,
vertical: PresentationAdaptation) -> View`

`func presentationContentInteraction(PresentationContentInteraction) -> View`

`func presentationCornerRadius(CGFloat?) -> View`

`func safeAreaPadding(CGFloat) -> View`

`func safeAreaPadding(EdgeInsets) -> View`

`func safeAreaPadding(Edge.Set, CGFloat?) -> View`

`func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> View`

`func scrollClipDisabled(Bool) -> View`

`func scrollIndicatorsFlash(onAppear: Bool) -> View`

`func scrollIndicatorsFlash(trigger: some Equatable) -> View`

`func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) ->
View`

`func scrollTargetBehavior(some ScrollTargetBehavior) -> View`

`func scrollTargetLayout(isEnabled: Bool) -> View`

`func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func scrollTransition(topLeading: ScrollTransitionConfiguration,
bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition:
(EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> View`

`func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) ->
View`

`func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () ->
S) -> View`

`func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> View`

`func searchSuggestions<S>(() -> S) -> View`

`func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) ->
View`

`func selectionDisabled(Bool) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> View`

`func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) ->
Bool) -> View`

`func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> View`

`func springLoadingBehavior(SpringLoadingBehavior) -> View`

`func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) ->
View`

`func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> View`

`func symbolEffectsRemoved(Bool) -> View`

`func textScale(Text.Scale, isEnabled: Bool) -> View`

`func toolbar(Visibility, for: ToolbarPlacement...) -> View`

`func toolbar(removing: ToolbarDefaultItemKind?) -> View`

`func toolbarBackground(Visibility, for: ToolbarPlacement...) -> View`

`func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> View`

`func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> View`

`func toolbarTitleMenu<C>(content: () -> C) -> View`

`func transaction<V>((inout Transaction) -> Void, body:
(PlaceholderContentView<DevicePicker<Label, Fallback>>) -> V) -> View`

`func transaction(value: some Equatable, (inout Transaction) -> Void) -> View`

`func typeSelectEquivalent(LocalizedStringKey) -> View`

`func typeSelectEquivalent(Text?) -> View`

`func typeSelectEquivalent<S>(S) -> View`

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> View`

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> View`

`func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) ->
View`

## Relationships

### Conforms To

  * `View`

## See Also

### Selecting nearby devices

Connecting a tvOS app to other devices over the local network

Display a view in your tvOS app that lists available iOS, iPadOS, and watchOS
devices that the user can connect to over their local network.

`class DDDevicePickerViewController`

A UIKit view that displays other devices on the network, and creates an
encrypted connection to a copy of your app running on that device.

`struct DevicePickerSupportedAction`

An environment value that indicates whether the current device supports device
discovery.

`property list key NSApplicationServices`

A list of service providers and the devices that they support.

Instance Property

# devicePickerSupports

Checks for support to present a DevicePicker.

DeviceDiscoveryUI  SwiftUI  tvOS 16.0+

    
    
    var devicePickerSupports: DevicePickerSupportedAction { get }

## See Also

### Interacting with networked devices

`struct DevicePicker`

A SwiftUI view that displays other devices on the network, and creates an
encrypted connection to a copy of your app running on that device.

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

Instance Property

# isActivityFullscreen

A Boolean value that indicates whether the Live Activity appears in a full-
screen presentation.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    var isActivityFullscreen: Bool { get }

## Discussion

When a Live Activity fills the entire screen, the system extends the
background tint color you set with the `activityBackgroundTint(_:)` modifier
to fill the screen.

Note that this environment variable is always `false` in iOS 16.

## See Also

### Configuring a Live Activity

`func activitySystemActionForegroundColor(Color?) -> some View`

The text color for the auxiliary action button that the system shows next to a
Live Activity on the Lock Screen.

`func activityBackgroundTint(Color?) -> some View`

Sets the tint color for the background of a Live Activity that appears on the
Lock Screen.

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

# currentEntitlementTask(for:priority:action:)

Declares the view as dependent on the entitlement of an in-app purchase
product for `productID` and returns a modified view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func currentEntitlementTask(
        for productID: String,
        priority: TaskPriority = .medium,
        action: @escaping (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()
    ) -> some View
    

##  Parameters

`productID`

    

The product ID to get the entitlement for. The task restarts whenever this
parameter changes.

`priority`

    

The task priority to use when creating the task.

`action`

    

The action to perform when the task’s state changes.

## Discussion

Before a view modified with this method appears, a task will start in the
background to get the current entitlement. While the view is presented, the
task will call `action` whenever the entitlement changes or the task’s state
changes.

Consumable in-app purchases will always pass `nil` to `action`. For auto-
renewable subscriptions, use `subscriptionStatusTask(for:priority:action:)` to
get the full status information for the subscription.

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

`func musicSubscriptionOffer(isPresented: Binding<Bool>, options:
MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) ->
some View`

Initiates the process of presenting a sheet with subscription offers for Apple
Music when the `isPresented` binding is `true`.

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

# inAppPurchaseOptions(_:)

Add a function to call before initiating a purchase from an in-app store
within view, providing a set of options for the purchase.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func inAppPurchaseOptions(_ options: ((Product) async -> Set<Product.PurchaseOption>)?) -> some View
    

##  Parameters

`options`

    

The system calls this function before processing a purchase, with the product
to be purchased is provided as a parameter. Return a set of purchase options
to add to the purchase.

## Discussion

In-app stores within this view will add any default purchase options to the
set you return, and use the result for configuring the purchase. If you just
want to react to in-app purchases beginning without adding purchase options,
you can add an action with `onInAppPurchaseStart(perform:)`.

You can remove any options ancestor views may have added by providing `nil`
for the action. This will result in using the default set of purchase options.

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

# manageSubscriptionsSheet(isPresented:subscriptionGroupID:)

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func manageSubscriptionsSheet(
        isPresented: Binding<Bool>,
        subscriptionGroupID: String
    ) -> some View
    

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

# onInAppPurchaseCompletion(perform:)

Add an action to perform when a purchase initiated from an in-app store within
this view completes.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onInAppPurchaseCompletion(perform action: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View
    

##  Parameters

`action`

    

The action to perform, with the product value and the purchase result provided
as parameters.

## Discussion

By default, transactions from successful in-app store view purchases will be
emitted from `Transaction.updates`. If the purchase fails with an error, an
alert will be displayed. You can revert a view back to this behavior by
providing `nil` for action.

Only one action will be performed for each purchase. Descendant views can
override the action by using another `onInAppPurchaseCompletion(perform:)`
modifier.

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

# onInAppPurchaseStart(perform:)

Add an action to perform when a user triggers the purchase button on an in-app
store within this view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func onInAppPurchaseStart(perform action: ((Product) async -> ())?) -> some View
    

##  Parameters

`action`

    

The action to perform, with the product to be purchased provided as a
parameter.

## Discussion

You can remove any actions ancestor views may have added by providing `nil`
for the action.

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

# productIconBorder()

Adds a standard border to an icon used by an `ProductView` .

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  visionOS 1.0+

    
    
    func productIconBorder() -> some View
    

## Discussion

You can also use this on an icon provided to `StoreView` instances.

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

# productViewStyle(_:)

Sets the style for in-app store products within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func productViewStyle(_ style: some ProductViewStyle) -> some View
    

## Discussion

This modifier styles any `ProductView` or `StoreView` instances within a view.

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

# productDescription(_:)

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func productDescription(_ visibility: Visibility) -> some View
    

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

# storeButton(_:for:)

Specifies the visibility of certain kinds of auxiliary buttons used by
`StoreView` or `SubscriptionStoreView` instances within the view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func storeButton(
        _ visibility: Visibility,
        for buttonKinds: StoreButtonKind...
    ) -> some View
    

##  Parameters

`visibility`

    

The preferred visibility of the buttons.

`buttonKinds`

    

The kinds of buttons to update visibility of.

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

# storeProductTask(for:priority:action:)

Declares the view as dependent on the in-app purchase product for `id` and
returns a modified view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func storeProductTask(
        for id: Product.ID,
        priority: TaskPriority = .medium,
        action: @escaping (Product.TaskState) async -> ()
    ) -> some View
    

##  Parameters

`id`

    

The product ID to load from the App Store. The task restarts whenever this
parameter changes.

`priority`

    

The task priority to use when creating the task.

`action`

    

The action to perform when the task’s state changes.

## Discussion

Before a view modified with this method appears, a task will start in the
background to load the product from the App Store. While the view is
presented, the task will call `action` whenever the product changes or the
task’s state changes.

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

# storeProductsTask(for:priority:action:)

Declares the view as dependent on a collection of in-app purchase products and
returns a modified view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func storeProductsTask(
        for ids: some Collection<String> & Equatable & Sendable,
        priority: TaskPriority = .medium,
        action: @escaping (Product.CollectionTaskState) async -> ()
    ) -> some View
    

##  Parameters

`ids`

    

The product IDs to load from the App Store. The task restarts whenever this
parameter changes.

`priority`

    

The task priority to use when creating the task.

`action`

    

The action to perform when the task’s state changes.

## Discussion

Before a view modified with this method appears, a task will start in the
background to load the products from the App Store. While the view is
presented, the task will call `action` whenever the products change or the
task’s state changes.

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

# subscriptionStatusTask(for:priority:action:)

Declares the view as dependent on the status of an auto-renewable subscription
group for `groupID` and returns a modified view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subscriptionStatusTask(
        for groupID: String,
        priority: TaskPriority = .medium,
        action: @escaping (EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()
    ) -> some View
    

##  Parameters

`groupID`

    

The subscription group ID to get the status for. The task restarts whenever
this parameter changes.

`priority`

    

The task priority to use when creating the task.

`action`

    

The action to perform when the task’s state changes.

## Discussion

Before a view modified with this method appears, a task will start in the
background to get the subscription status. While the view is presented, the
task will call `action` whenever the status changes or the task’s state
changes.

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

# subscriptionStoreButtonLabel(_:)

Configures in-app subscription store instances within a view to use a certain
button label.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  watchOS 10.0+
visionOS 1.0+

    
    
    func subscriptionStoreButtonLabel(_ label: SubscriptionStoreButtonLabel) -> some View
    

## Discussion

The button label is not always respected in every context. For example, if you
have a subscription store that shows multiple subscribe buttons, setting
`SubscriptionStoreButtonLabel/action-swift.type.property` as the button label
will fall back to each subscription’s display name.

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

# subscriptionStoreControlIcon(icon:)

Set a view to use to decorate individual subscription options within a
`SubscriptionStoreView`.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subscriptionStoreControlIcon(@ViewBuilder icon: @escaping (Product, Product.SubscriptionInfo) -> some View) -> some View
    

## Discussion

You can adjust this view to provide different appearances for each
subscription option.

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

# subscriptionStoreControlStyle(_:)

Sets the control style for in-app subscription stores within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subscriptionStoreControlStyle(_ style: some SubscriptionStoreControlStyle) -> some View
    

## Discussion

This modifier styles any `SubscriptionStoreView` instances within a view.

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

# subscriptionStorePickerItemBackground(_:)

Sets the background style for picker items of `SubscriptionStoreView`
instances within this view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  watchOS 10.0+
visionOS 1.0+

    
    
    func subscriptionStorePickerItemBackground(_ backgroundStyle: some ShapeStyle) -> some View
    

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

# subscriptionStorePolicyDestination(for:destination:)

Configures a view as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subscriptionStorePolicyDestination(
        for button: SubscriptionStorePolicyKind,
        @ViewBuilder destination: () -> some View
    ) -> some View
    

##  Parameters

`button`

    

The policy button to associate the URL with.

`destination`

    

The view to present when someone chooses to view the policy.

## Discussion

Except on tvOS, you can also set a URL as the destination using
`subscriptionStorePolicyDestination(url:for:)`. If you do not set a
destination, the system will use the automatic behavior. Check the
documentation for the value you provide for `button` to understand the
automatic behavior.

By default, the subscription store shows the terms of service & privacy policy
buttons if you set a destination for at least one policy. The policy that is
not explicitly set will use the automatic behavior. You can override this
behavior using the `storeButton(_:for:)` modifier, with
`StoreButtonKind/policies` as the second parameter.

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

# subscriptionStorePolicyDestination(url:for:)

Configures a URL as the destination when someone chooses to view the
corresponding policy in a `SubscriptionStoreView` within this view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  watchOS 10.0+
visionOS 1.0+

    
    
    func subscriptionStorePolicyDestination(
        url: URL,
        for button: SubscriptionStorePolicyKind
    ) -> some View
    

##  Parameters

`url`

    

The URL of the web page to open when someone chooses to view the policy.

`button`

    

The policy button to associate the URL with.

## Discussion

You can also set a view as the destination using
`subscriptionStorePolicyDestination(for:destination:)`. If you do not set a
destination, or pass `nil` for `url`, the system will use the automatic
behavior. Check the documentation for the value you provide for `button` to
understand the automatic behavior.

By default, the subscription store shows the terms of service & privacy policy
buttons if you set a destination for at least one policy. The policy that is
not explicitly set will use the automatic behavior. You can override this
behavior using the `storeButton(_:for:)` modifier, with
`StoreButtonKind/policies` as the second parameter.

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

# subscriptionStorePolicyForegroundStyle(_:)

Sets the style for terms of service or privacy policy buttons created by
`SubscriptionStoreView` within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subscriptionStorePolicyForegroundStyle(_ style: some ShapeStyle) -> some View
    

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

# subscriptionStorePolicyForegroundStyle(_:_:)

Sets the style for terms of service and privacy policy buttons created by
`SubscriptionStoreView` within a view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subscriptionStorePolicyForegroundStyle(
        _ primary: some ShapeStyle,
        _ secondary: some ShapeStyle
    ) -> some View
    

##  Parameters

`primary`

    

The color or pattern to use for the terms of service and privacy policy
buttons

`secondary`

    

The color or pattern to use for the conjunction between the buttons in the
policy section

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

# subscriptionStoreSignInAction(_:)

Add an action to perform when someone triggers the sign in button on a
`SubscriptionStoreView` within this view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func subscriptionStoreSignInAction(_ action: (() -> ())?) -> some View
    

##  Parameters

`action`

    

The action to perform. Pass `nil` to remove the sign in action for
subscription stores within this view. The default value is `nil`.

## Discussion

You can only have one sign in action for a view. If an ancestor view specifies
a sign in action, using this modifier will replace the ancestor’s sign in
action.

If the value is `nil`, subscription stores will never show a sign in button.
You can also hide the sign in button without removing the action by using the
`storeButton(_:for:)` modifier, providing `StoreButtonKind/signIn` as the
button kind.

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

# subscriptionStoreControlBackground(_:)

Set the control background style for `SubscriptionStoreView` instances within
the view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func subscriptionStoreControlBackground(_ backgroundStyle: SubscriptionStoreControlBackground) -> some View
    

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

# subscriptionStoreControlBackground(_:)

Set the control background style for `SubscriptionStoreView` instances within
the view.

StoreKit  SwiftUI  iOS 17.0+  iPadOS 17.0+  macOS 14.0+

    
    
    func subscriptionStoreControlBackground(_ backgroundStyle: some ShapeStyle) -> some View
    

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

`func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo)
-> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo,
Product.SubscriptionOffer) async throws ->
Product.SubscriptionOffer.Signature) -> some View`

Select a promotional offer to apply to a purchase made from a subscription
store view.

Instance Method

# subscriptionPromotionalOffer(offer:signature:)

Select a promotional offer to apply to a purchase made from a subscription
store view.

StoreKit  SwiftUI  iOS 17.4+  iPadOS 17.4+  macOS 14.4+  tvOS 17.4+  watchOS
10.4+  visionOS 1.1+

    
    
    func subscriptionPromotionalOffer(
        offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?,
        signature: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature
    ) -> some View
    

##  Parameters

`offer`

    

The system calls this function before drawing the given subscription product
on the subscription store view. Return the promotional offer to apply to the
product, if any, to have system-provided UI reflect the discounted terms under
the selected offer.

`signature`

    

The system calls this function before processing a purchase, with the product
to be purchased provided as a parameter, along with the selected subscription
offer to be applied to the purchase. Return a signature you generate on your
server that validates the selected offer. Errors thrown from this closure will
be surfaced via the `onInAppPurchaseCompletion(perform:)` modifier.

## Discussion

Subscription stores within this view will use the specified subscription offer
to configure the appearance of the subscription plans displayed, when using a
system-provided `SubscriptionStoreControlStyle` to style the in-app
subscription store. Standard `ProductViewStyle` instances don’t show
introductory or promotional offers in UI, instead use `SubscriptionStoreView`.

If the selected offer is determined to be valid using the `signature`
parameter, it will be applied to the purchase. If an offer is determined to be
invalid using its corresponding signature, the purchase will fail with
`StoreKit/Product.PurchaseError/invalidOfferSignature`.

Promotional offers selected through this modifier will overwrite any offers
specified by ancestor views.

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

Instance Method

# healthDataAccessRequest(store:objectType:predicate:trigger:completion:)

Asynchronously requests permission to read a data type that requires per-
object authorization (such as vision prescriptions).

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func healthDataAccessRequest(
        store: HKHealthStore,
        objectType: HKObjectType,
        predicate: NSPredicate? = nil,
        trigger: some Equatable,
        completion: @escaping (Result<Bool, any Error>) -> Void
    ) -> some View
    

##  Parameters

`store`

    

The HealthKit store where you’re requesting authorization.

`objectType`

    

The data type you want to read.

`trigger`

    

A value used to trigger the request. This value must be a `State` variable.
Any change to the variable triggers a request.

`completion`

    

A block that the system calls after the request is complete. The system passes
the result parameter.

`result`

    

A value that indicates whether the request succeeded. This value doesn’t
indicate whether the user actually granted permission. The value is `.success`
if the request succeeded; otherwise, it’s `.error`. You can access the error’s
description from the `.error` value.

## Discussion

Some samples require per-object authorization. For these samples, people can
select which ones your app can read on a sample-by-sample basis. By default,
your app can read any of the per-object authorization samples that it has
saved to the HealthKit store; however, you may not always have access to those
samples. People can update the authorization status for any of these samples
at any time.

Your app can begin by setting up the request in SwiftUI.

Next, query for any samples that it already has permission to read.

Based on the results, you can then decide whether you need to request
authorization for additional samples. Modify the trigger’s value to prompt
someone to modify the samples your app has access to read.

Important

Using the
`healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)`
method to request read access to any data types that require per-object
authorization fails with an `errorInvalidArgument` error.

When your app calls this method, HealthKit displays an authorization sheet
that asks for permission to read the samples that match the predicate and
object type. The person using your app can then select individual samples to
share with your app. The system always asks for permission, regardless of
whether the user previously granted it.

People can individually enable each of the prescriptions. After they respond,
the system calls the callback handler on an arbitrary background queue.

## See Also

### Accessing health data

`func healthDataAccessRequest(store: HKHealthStore, readTypes:
Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any
Error>) -> Void) -> some View`

Requests permission to read the specified HealthKit data types.

`func healthDataAccessRequest(store: HKHealthStore, shareTypes:
Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable,
completion: (Result<Bool, any Error>) -> Void) -> some View`

Requests permission to save and read the specified HealthKit data types.

`func workoutPreview(WorkoutPlan, isPresented: Binding<Bool>) -> some View`

Presents a preview of the workout contents as a modal sheet

Instance Method

# healthDataAccessRequest(store:readTypes:trigger:completion:)

Requests permission to read the specified HealthKit data types.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.2+
visionOS 1.0+

    
    
    func healthDataAccessRequest(
        store: HKHealthStore,
        readTypes: Set<HKObjectType>,
        trigger: some Equatable,
        completion: @escaping (Result<Bool, any Error>) -> Void
    ) -> some View
    

##  Parameters

`store`

    

The HealthKit store where you’re requesting authorization.

`readTypes`

    

An optional set containing the data types you want to read. This set can
contain any concrete subclass of the `HKObjectType` class (any of the
`HKCharacteristicType`, `HKQuantityType`, `HKCategoryType`, `HKWorkoutType`,
or `HKCorrelationType` classes ). If the user grants permission, your app can
read these data types from the HealthKit store.

`trigger`

    

A value used to trigger the request. This value must be a `State` variable.
Any change to the variable triggers a request.

`completion`

    

A block that the system calls after the request is complete. The system passes
the result parameter.

`result`

    

A value that indicates whether the request succeeded. This value doesn’t
indicate whether the user actually granted permission. The value is `.success`
if the request succeeded; otherwise, it’s `.error`. You can access the error’s
description from the `.error` value.

## Discussion

HealthKit performs this request asynchronously when you modify the trigger’s
value. If you call this method with a new data type (a type of data that the
user hasn’t previously granted or denied permission for in this app), the
system automatically displays the authorization sheet when you modify the
trigger’s value. The authorization sheet lists all the requested permissions.
After the user finishes responding, HealthKit calls the completion block on a
background queue. If the user has already chosen to grant or prohibit access
to all of the types specified, HealthKit calls the completion when you modify
the trigger without prompting the user.

  * Authenticating on launch 
  * Full Swift file 

Customize the messages displayed on the permissions sheet by setting the
following key:

  * `NSHealthShareUsageDescription` customizes the message for reading data.

Warning

You must set the usage key, or your app crashes when you request
authorization.

Set the key in the Target Properties list on the app’s Info tab.

After users set the permissions for your app, they can always change them
using either the Settings or the Health app. Your app appears in the Health
app’s Sources tab, even if the user didn’t allow permission to read data.

## See Also

### Accessing health data

`func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType,
predicate: NSPredicate?, trigger: some Equatable, completion: (Result<Bool,
any Error>) -> Void) -> some View`

Asynchronously requests permission to read a data type that requires per-
object authorization (such as vision prescriptions).

`func healthDataAccessRequest(store: HKHealthStore, shareTypes:
Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable,
completion: (Result<Bool, any Error>) -> Void) -> some View`

Requests permission to save and read the specified HealthKit data types.

`func workoutPreview(WorkoutPlan, isPresented: Binding<Bool>) -> some View`

Presents a preview of the workout contents as a modal sheet

Instance Method

# healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)

Requests permission to save and read the specified HealthKit data types.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  watchOS 10.2+
visionOS 1.0+

    
    
    func healthDataAccessRequest(
        store: HKHealthStore,
        shareTypes: Set<HKSampleType>,
        readTypes: Set<HKObjectType>? = nil,
        trigger: some Equatable,
        completion: @escaping (Result<Bool, any Error>) -> Void
    ) -> some View
    

##  Parameters

`store`

    

The HealthKit store where you’re requesting authorization.

`shareTypes`

    

A set containing the data types you want to share. This set can contain any
concrete subclass of the `HKSampleType` class (any of the `HKQuantityType`,
`HKCategoryType`, `HKWorkoutType`, or `HKCorrelationType` classes). If the
user grants permission, your app can create and save these data types to the
HealthKit store.

`readTypes`

    

An optional set containing the data types you want to read. This set can
contain any concrete subclass of the `HKObjectType` class (any of the
`HKCharacteristicType`, `HKQuantityType`, `HKCategoryType`, `HKWorkoutType`,
or `HKCorrelationType` classes ). If the user grants permission, your app can
read these data types from the HealthKit store.

`trigger`

    

A value used to trigger the request. This value must be a `State` variable.
Any change to the variable triggers a request.

`completion`

    

A block that the system calls after the request is complete. The system passes
the result parameter.

`result`

    

A value that indicates whether the request succeeded. This value doesn’t
indicate whether the user actually granted permission. The value is `.success`
if the request succeeded; otherwise, it’s `.error`. You can access the error’s
description from the `.error` value.

## Discussion

HealthKit performs these requests asynchronously when you modify the trigger’s
value. If you call this method with a new data type (a type of data that the
user hasn’t previously granted or denied permission for in this app), the
system automatically displays the authorization sheet when you modify the
trigger’s value. The authorization sheet lists all the requested permissions.
After the user finishes responding, HealthKit calls the completion block on a
background queue. If the user has already chosen to grant or prohibit access
to all of the types specified, HealthKit calls the completion when you modify
the trigger without prompting the user.

Each data type has two separate permissions, one to read it and one to share
it. You can make a single request, and include all the data types your app
needs.

  * Authenticating on launch 
  * Full Swift file 

Customize the messages displayed on the permissions sheet by setting the
following keys:

  * `NSHealthShareUsageDescription` customizes the message for reading data.

  * `NSHealthUpdateUsageDescription` customizes the message for writing data.

Warning

You must set the usage keys, or your app crashes when you request
authorization.

Set these keys in the Target Properties list on the app’s Info tab.

After users set the permissions for your app, they can always change them
using either the Settings or the Health app. Your app appears in the Health
app’s Sources tab, even if the user didn’t allow permission to read or share
data.

## See Also

### Accessing health data

`func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType,
predicate: NSPredicate?, trigger: some Equatable, completion: (Result<Bool,
any Error>) -> Void) -> some View`

Asynchronously requests permission to read a data type that requires per-
object authorization (such as vision prescriptions).

`func healthDataAccessRequest(store: HKHealthStore, readTypes:
Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any
Error>) -> Void) -> some View`

Requests permission to read the specified HealthKit data types.

`func workoutPreview(WorkoutPlan, isPresented: Binding<Bool>) -> some View`

Presents a preview of the workout contents as a modal sheet

Instance Method

# workoutPreview(_:isPresented:)

Presents a preview of the workout contents as a modal sheet

WorkoutKit  SwiftUI  iOS 17.0+  iPadOS 17.0+

    
    
    func workoutPreview(
        _ workout: WorkoutPlan,
        isPresented: Binding<Bool>
    ) -> some View
    

##  Parameters

`workout`

    

the `WorkoutContainer` the preview displays

`isPresented`

    

a binding to a Boolean value that determines whether to present the preview

## Discussion

## See Also

### Accessing health data

`func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType,
predicate: NSPredicate?, trigger: some Equatable, completion: (Result<Bool,
any Error>) -> Void) -> some View`

Asynchronously requests permission to read a data type that requires per-
object authorization (such as vision prescriptions).

`func healthDataAccessRequest(store: HKHealthStore, readTypes:
Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any
Error>) -> Void) -> some View`

Requests permission to read the specified HealthKit data types.

`func healthDataAccessRequest(store: HKHealthStore, shareTypes:
Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable,
completion: (Result<Bool, any Error>) -> Void) -> some View`

Requests permission to save and read the specified HealthKit data types.

Instance Method

# popoverTip(_:arrowEdge:)

Presents a popover tip on the modified view.

tvOS 17.0+

    
    
    func popoverTip<Content>(
        _ tip: Content,
        arrowEdge: Edge = .top
    ) -> some View where Content : Tip
    

## See Also

### Providing tips

`func popoverTip<Content>(Content, arrowEdge: Edge, action: (Tips.Action) ->
Void) -> some View`

Presents a popover tip on the modified view.

`func tipBackground(some ShapeStyle) -> some View`

Sets the tip’s view background to a style. Currently this only applies to
inline tips, not popover tips.

`func tipCornerRadius(CGFloat, antialiased: Bool) -> some View`

`func tipImageSize(CGSize) -> some View`

`func tipViewStyle(some TipViewStyle) -> some View`

Sets the given style for TipView within the view hierarchy.

Instance Method

# popoverTip(_:arrowEdge:action:)

Presents a popover tip on the modified view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.1+  visionOS
1.0+

    
    
    func popoverTip<Content>(
        _ tip: Content,
        arrowEdge: Edge = .top,
        action: @escaping (Tips.Action) -> Void = { _ in }
    ) -> some View where Content : Tip
    

## See Also

### Providing tips

`func popoverTip<Content>(Content, arrowEdge: Edge) -> some View`

Presents a popover tip on the modified view.

`func tipBackground(some ShapeStyle) -> some View`

Sets the tip’s view background to a style. Currently this only applies to
inline tips, not popover tips.

`func tipCornerRadius(CGFloat, antialiased: Bool) -> some View`

`func tipImageSize(CGSize) -> some View`

`func tipViewStyle(some TipViewStyle) -> some View`

Sets the given style for TipView within the view hierarchy.

Instance Method

# tipBackground(_:)

Sets the tip’s view background to a style. Currently this only applies to
inline tips, not popover tips.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func tipBackground(_ style: some ShapeStyle) -> some View
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI draws behind
the modified view.

## Return Value

A view with the specified style drawn behind it.

## See Also

### Providing tips

`func popoverTip<Content>(Content, arrowEdge: Edge) -> some View`

Presents a popover tip on the modified view.

`func popoverTip<Content>(Content, arrowEdge: Edge, action: (Tips.Action) ->
Void) -> some View`

Presents a popover tip on the modified view.

`func tipCornerRadius(CGFloat, antialiased: Bool) -> some View`

`func tipImageSize(CGSize) -> some View`

`func tipViewStyle(some TipViewStyle) -> some View`

Sets the given style for TipView within the view hierarchy.

Instance Method

# tipCornerRadius(_:antialiased:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func tipCornerRadius(
        _ cornerRadius: CGFloat,
        antialiased: Bool = true
    ) -> some View
    

## See Also

### Providing tips

`func popoverTip<Content>(Content, arrowEdge: Edge) -> some View`

Presents a popover tip on the modified view.

`func popoverTip<Content>(Content, arrowEdge: Edge, action: (Tips.Action) ->
Void) -> some View`

Presents a popover tip on the modified view.

`func tipBackground(some ShapeStyle) -> some View`

Sets the tip’s view background to a style. Currently this only applies to
inline tips, not popover tips.

`func tipImageSize(CGSize) -> some View`

`func tipViewStyle(some TipViewStyle) -> some View`

Sets the given style for TipView within the view hierarchy.

Instance Method

# tipImageSize(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func tipImageSize(_ size: CGSize) -> some View
    

## See Also

### Providing tips

`func popoverTip<Content>(Content, arrowEdge: Edge) -> some View`

Presents a popover tip on the modified view.

`func popoverTip<Content>(Content, arrowEdge: Edge, action: (Tips.Action) ->
Void) -> some View`

Presents a popover tip on the modified view.

`func tipBackground(some ShapeStyle) -> some View`

Sets the tip’s view background to a style. Currently this only applies to
inline tips, not popover tips.

`func tipCornerRadius(CGFloat, antialiased: Bool) -> some View`

`func tipViewStyle(some TipViewStyle) -> some View`

Sets the given style for TipView within the view hierarchy.

Instance Method

# tipViewStyle(_:)

Sets the given style for TipView within the view hierarchy.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func tipViewStyle(_ style: some TipViewStyle) -> some View
    

##  Parameters

`style`

    

The style to set.

## Return Value

A view that uses the specified style on its child views.

## Discussion

For more information on styling tips, see `TipKit/TipViewStyle`.

## See Also

### Providing tips

`func popoverTip<Content>(Content, arrowEdge: Edge) -> some View`

Presents a popover tip on the modified view.

`func popoverTip<Content>(Content, arrowEdge: Edge, action: (Tips.Action) ->
Void) -> some View`

Presents a popover tip on the modified view.

`func tipBackground(some ShapeStyle) -> some View`

Sets the tip’s view background to a style. Currently this only applies to
inline tips, not popover tips.

`func tipCornerRadius(CGFloat, antialiased: Bool) -> some View`

`func tipImageSize(CGSize) -> some View`

