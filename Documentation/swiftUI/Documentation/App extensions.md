Article

# Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

## Overview

Widgets display relevant, glanceable content that people can quickly access
for more details. Your app can provide a variety of widgets, letting people
focus on the information that’s most important to them.

A good way to get started with widgets and WidgetKit is by adding a _static_
widget to your app. A static widget doesn’t need any configuration by the
user. For example, a static widget might show a stock market summary, or the
next event on the user’s calendar. The _data_ the widget shows is dynamic, but
the _type_ of data it shows is fixed. Consider the information your app
presents, and choose something that people would find useful to see at a
glance on their device.

Widgets can display data in many sizes, from small watch complications or
Dynamic Island presentations, to extra large iPad and macOS widgets. The
example that follows below focuses on a single size widget, the small system
size, or `WidgetFamily.systemSmall`. The example widget displays the status of
a hypothetical game, such as player turn or the health level of a character.

You build widgets using SwiftUI. While there are similarities to how you
present views in your app, some aspects are unique to developing widgets. For
more information about using SwiftUI, see SwiftUI. However, not all SwiftUI
views work in widgets. For a list of the views that work in widgets, see
SwiftUI views for widgets.

### Add a widget target to your app

The Widget Extension template provides a starting point for creating your
widget. The template creates an extension target that contains a single
widget. Later, you can add additional widgets to the same extension to display
different types of information or to support additional widget sizes.

  1. Open your app project in Xcode and choose File > New > Target.

  2. From the Application Extension group, select Widget Extension, and then click Next.

  3. Enter the name of your extension.

  4. Deselect the Include Live Activity and Include Configuration App Intent checkboxes, if they’re selected.

  5. Click Finish.

Note

Live Activities use WidgetKit and share many aspects of their design and
implementation with the widgets in your app. If your app supports Live
Activities, consider implementing them at the same time you add your widgets.
For more information about Live Activities, see Displaying live data with Live
Activities.

The widget extension template provides an initial implementation that conforms
to the `Widget` protocol. The widget’s `body` property determines the type of
content that the widget presents. Static widgets use a `StaticConfiguration`
for the `body` property. Other types of widget configurations include:

  * `AppIntentConfiguration` that enables user customization, such as a weather widget that needs a zip or postal code for a city, or a package-tracking widget that needs a tracking number.

  * `ActivityConfiguration` to present live data, such as scores during a sporting event or a food delivery estimate.

For more information about these other widget configurations, see Making a
configurable widget and Displaying live data with Live Activities.

### Add configuration details

To configure a static widget, provide the following information:

`kind`

    

A string that identifies the widget. This is an identifier you choose, and
should be descriptive of what the widget represents.

`provider`

    

An object that conforms to `TimelineProvider` and produces a _timeline_ that
tells WidgetKit when to render the widget. A timeline is a sequence that
contains a custom `TimelineEntry` type you define. The entries in this
sequence identify the date when you want WidgetKit to update the widget’s
content and includes properties your widget’s view needs to render in the
custom type.

`content`

    

A closure that contains SwiftUI views. WidgetKit invokes this to render the
widget’s content, passing a `TimelineEntry` parameter from the provider.

Use modifiers to provide additional configuration details, including a display
name, a description, and the families the widget supports. The following code
shows a widget that provides general status for a game:

The widget’s provider generates a timeline for the widget, and includes the
game-status details in each entry. When the date of each timeline entry
arrives, WidgetKit invokes the `content` closure to display the widget’s
content. Finally, the modifiers specify the name and description shown in the
widget gallery, and the sizes that the widget supports.

Important

For an app’s widget to appear in the widget gallery, a person must launch the
app that contains the widget at least once after the app is installed.

Note the usage of the `@main` attribute on this widget. This attribute
indicates that the `GameStatusWidget` is the entry point for the widget
extension, implying that the extension contains a single widget. To support
multiple widgets, see the `WidgetBundle`.

### Provide timeline entries

The timeline provider you define generates a sequence of timeline entries.
Each specifies the date and time to update the widget’s content, and includes
the data your widget needs to render its view. The game-status widget might
define its timeline entry to include a string that represents the status of
the game, as follows:

WidgetKit calls `getTimeline(in:completion:)` to request a the timeline from
the provider. The timeline consists of one or more timeline entries and a
reload policy that informs WidgetKit when to request a subsequent timeline.

The following example shows how the game-status widget’s provider generates a
timeline that consists of a single entry with the current game status from the
server, and a reload policy to request a new timeline in 15 minutes:

In this example, if the widget didn’t have the current status from the server,
it could store a reference to the completion, perform an asynchronous request
to the server to fetch the game status, and call the completion when that
request completes.

For more information about generating timelines, see Keeping a widget up to
date. For more information about handling network, see Making network requests
in a widget extension.

### Generate a preview for the widget gallery

In order for people to be able to use your widget, it needs to be available in
the widget gallery. To show your widget in the widget gallery, WidgetKit asks
the provider for a _preview snapshot_ that displays generic data. WidgetKit
makes this request by calling the provider’s `getSnapshot(in:completion:)`
method with the `context` parameter’s `isPreview` property set to `true`.

In response, you need to create the preview snapshot quickly. If your widget
would normally need assets or information that takes time to generate or fetch
from a server, use sample data instead.

In the following code, the game-status widget’s provider implements the
snapshot method by showing the game status if it’s available, falling back to
an empty status if it doesn’t have the status from its server:

### Display content in your widget

Widgets define their content using a SwiftUI view, commonly by composing other
SwiftUI views. As shown in the Add configuration details section, the widget’s
configuration contains the closure that WidgetKit invokes to render the
widget’s content.

When people add your widget from the widget gallery, they choose the specific
family — for example, small or medium — from the ones your widget supports.
The widget’s content closure has to be capable of rendering each family the
widget supports. WidgetKit sets the corresponding family and additional
properties, such as the color scheme (light or dark), in the SwiftUI
environment.

In the game-status widget’s configuration shown above, the content closure
uses a `GameStatusView` to display the status. Because this widget only
supports the `.systemSmall` family, it uses a composed `GameTurnSummary`
SwiftUI view to display a summary of the game’s current status. For any other
family size, it shows the default view, which indicates that game status is
unavailable.

In your widget, as you add more supported families to the widget’s
configuration, you would add additional cases in the widget view’s `body`
property for each additional family.

Note

The view declares its body with `@ViewBuilder` because the type of view it
uses varies.

### Display a placeholder widget

A placeholder view is similar to a preview snapshot, but instead of showing
example data to let people see the type of data the widget displays, it shows
a generic visual representation with no specific content. When WidgetKit
renders your widget, it may need to render your content as a placeholder, for
example, while you load data in the background or if you tell the system that
your widget contains sensitive information.

### Hide sensitive content

Widgets and watch complications may show sensitive information and can be
highly visible, especially on devices with an Always-On display. When you
create your widget or watch complication, review its content and consider
hiding sensitive information.

To let people decide whether a widget should show sensitive data on a locked
device, mark views that contain sensitive information using the
`privacySensitive(_:)` modifier. In iOS, people can configure whether to show
sensitive data on the Lock Screen and during Always On. In Settings, they can
deactivate data access for Lock Screen widgets in the ALLOW ACCESS WHEN LOCKED
section of Settings > Face ID & Passcode. On Apple Watch, people can configure
whether to show sensitive data during Always On by Choosing Settings > Display
& Brightness > Always On > Hide Sensitive Complications. They can choose to
show redacted content for all or individual complications.

If a person chooses to hide privacy sensitive content, WidgetKit renders a
placeholder or redactions you configure. To configure redactions, implement
the `redacted(reason:)` callback, read out the `privacy` property, and provide
custom placeholder views. You can also choose to render a view as unredacted
with the `unredacted()` view modifier.

As an alternative to marking individual views as privacy sensitive, for
example, if your entire widget content is privacy sensitive, add the Data
Protection capability to your widget extension. Until a person unlocks their
device to match the privacy level you chose, WidgetKit displays placeholder
instead of the widget content. First, enable the Data Protection capability
for your widget extension in Xcode, then set the `Data Protection Entitlement`
entitlement to the value that fits the level of privacy you want to offer:

`NSFileProtectionComplete`

    

WidgetKit hides widget content when the device is locked. Additionally, iOS
widgets aren’t available as iPhone widgets on Mac.

`NSFileProtectionCompleteUnlessOpen`

    

WidgetKit hides widget content when the device is passcode locked.
Additionally, iOS widgets aren’t available as iPhone widgets on Mac.

If you choose the `NSFileProtectionCompleteUntilFirstUserAuthentication` or
`NSFileProtectionNone` protection level for your widget extension:

  * WidgetKit uses its default behavior and displays a placeholder until a person authenticates after they reboot their device.

  * iOS widgets are available as iPhone widgets on Mac.

### Add dynamic content to your widget

Widgets typically present read-only information and don’t generally support
interactive elements such as scrolling lists or text input. Starting with iOS
17 and macOS 14, widgets support some interactive elements and animations. For
details on adding interactivity to your widgets, see Adding interactivity to
widgets and Live Activities.

For a list of views that WidgetKit supports, see SwiftUI views for widgets.
WidgetKit ignores other views when it renders the widget’s’ content.

Although the display of a widget is based on a snapshot of your view, you can
use various SwiftUI views that continue to update while your widget is
visible. For more about providing dynamic content, see Keeping a widget up to
date.

### Respond to user interactions

When people interact with your widget, beyond interactive elements described
above, the system launches your app to handle the request. When the system
activates your app, navigate to the details that correspond to the widget’s
content. Your widget can specify a URL to inform the app what content to
display. To configure custom URLs in your widget:

  * For all widgets, add the `widgetURL(_:)` view modifier to a view in your widget’s view hierarchy. If the widget’s view hierarchy includes more than one `widgetURL` modifier, the behavior is undefined.

  * For widgets that use `WidgetFamily.systemMedium`, `WidgetFamily.systemLarge`, or `WidgetFamily.systemExtraLarge`, add one or more `Link` controls to your widget’s view hierarchy. You can use both `widgetURL` and `Link` controls. If the interaction targets a `Link` control, the system uses the URL in that control. For interactions anywhere else in the widget, the system uses the URL specified in the `widgetURL` view modifier.

For more details about adding links from your widgets to your app, see Linking
to specific app scenes from your widget or Live Activity.

### Preview widgets in Xcode

Xcode allows you to look at previews of your widgets without running your app
in Simulator or on a test device. The following example shows the preview code
from the Emoji Rangers widget of the Building Widgets Using WidgetKit and
SwiftUI sample code project. Note how it uses the `widgetFamily` environment
value to avoid manually specifying a name for each widget.

As you support more widget families in your widget, you can add more preview
views to see multiple sizes in a single preview.

### Expand your widget’s capabilities

To give people flexible access to your app’s content, you can support
additional families, add additional widget types, make your widgets user-
configurable, or add support for Live Activities if your app presents live
data. To explore a plan to support additional features, see Developing a
WidgetKit strategy.

To explore WidgetKit code for the first time, see the following sample code
projects:

  * Building Widgets Using WidgetKit and SwiftUI is the sample code project associated with the WWDC20 code-alongs Widgets Code-along, part 1: The adventure begins, Widgets Code-along, part 2: Alternate timelines, and Widgets Code-along, part 3: Advancing timelines, where you learn how to build your first widget.

  * Emoji Rangers: Supporting Live Activities, interactivity, and animations expands the Emoji Rangers sample code project to include Lock Screen widgets, Live Activities, interactivity, and animations.

  * Fruta: Building a Feature-Rich App with SwiftUI and Backyard Birds: Building an app with SwiftData and widgets are sample code projects that support widgets in addition to other technologies like App Clips and SwiftData.

### Create multiple widget extensions

You can include multiple widget types in your widget extension, although your
app can contain multiple extensions. For example, if some of your widgets use
location information and others don’t, keep the widgets that use location
information in a separate extension. This allows the system to prompt someone
for authorization to use location information only for the widgets from the
extension that uses location information. For details about bundling multiple
widgets in an extension, see `WidgetBundle`.

## See Also

### Widget creation

Supporting additional widget sizes

Offer widgets in additional contexts by adding support for various widget
sizes.

Creating accessory widgets and watch complications

Support accessory widgets that appear on the Lock Screen and as complications
on Apple Watch.

Migrating ClockKit complications to WidgetKit

Leverage WidgetKit’s API to create watchOS complications using SwiftUI.

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Emoji Rangers: Supporting Live Activities, interactivity, and animations

Offer Live Activities, animate data updates, and add interactivity to widgets.

Backyard Birds: Building an app with SwiftData and widgets

Create an app with persistent data, interactive widgets, and an all new in-app
purchase experience.

Fruta: Building a Feature-Rich App with SwiftUI

Create a shared codebase to build a multiplatform app that offers widgets and
an App Clip.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct StaticConfiguration`

An object describing the content of a widget that has no user-configurable
options.

`enum WidgetFamily`

Values that define the widget’s size and shape.

`struct WidgetRenderingMode`

Constants that indicate the rendering mode for a widget.

Article

# Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

## Overview

Widgets use SwiftUI views to display their content. WidgetKit renders the
views on your behalf in a separate process. As a result, your widget extension
is not continually active, even if the widget is onscreen. Despite your widget
not always being active, there are several ways you can keep its content up to
date.

### Plan reloads within a budget

Reloading widgets consumes system resources and causes battery drain due to
additional networking and processing. To reduce this performance impact and
maintain all-day battery life, limit the frequency and number of updates you
request to what’s necessary.

To manage system load, WidgetKit uses a budget to distribute widget reloads
over the course of the day. The budget allocation is dynamic and takes many
factors into account, including:

  * The frequency and times the widget is visible to the user.

  * The widget’s last reload time.

  * Whether the widget’s containing app is active.

WidgetKit maintains different budgets for each active widget the user adds to
their device. For example, if the user adds two instances of a configurable
sports widget, showing information for two different teams, each widget has
its own budget.

A widget’s budget applies to a 24-hour period. WidgetKit tunes the 24-hour
window to the user’s daily usage pattern, which means the daily budget doesn’t
necessarily reset at exactly midnight. For a widget the user frequently views,
a daily budget typically includes from 40 to 70 refreshes. This rate roughly
translates to widget reloads every 15 to 60 minutes, but it’s common for these
intervals to vary due to the many factors involved.

Note

The system takes a few days to learn the user’s behavior. During this learning
period, your widget may receive more reloads than normal.

Cases in which WidgetKit doesn’t count reloads against your widget’s budget
include when:

  * The widget’s containing app is in the foreground.

  * The widget’s containing app has an active audio or navigation session.

  * The widget performs an app intent, such as when the user taps a button or toggles a switch.

  * The widget performs an animation.

  * The system locale changes.

  * Dynamic Type or Accessibility settings change.

For cases such as system appearance changes or system locale changes, don’t
request a timeline reload from your app. The system updates your widgets
automatically. In StandBy, the system refreshes your widget’s display at a
system-defined rate that doesn’t count against the its budget.

Although your widget timeline provider drives your reload schedule, WidgetKit
sometimes reloads your widget to help keep its content fresh. Some common
scenarios include:

  * If a widget is on a Home Screen page that the user rarely visits, WidgetKit may reduce the frequency of reloads for that widget. Later, when the user views the page, WidgetKit may reload the widget when it becomes visible.

  * For widgets that use Location Services, WidgetKit reloads them after a significant location change happens. For more information related to reloads for widgets that use Location Services, see Accessing location information in widgets.

If your widget can predict points in time that it should reload, the best
approach is to generate a timeline for as many future dates as possible. Keep
the interval of entries in the timeline as large as possible for the content
you display. WidgetKit imposes a minimum amount of time before it reloads a
widget. Your timeline provider should create timeline entries that are at
least about 5 minutes apart. WidgetKit may coalesce reloads across multiple
widgets, affecting the exact time a widget is reloaded.

### Generate a timeline for predictable events

Many widgets have predictable points in time where it makes sense to update
their content. For example, a widget that displays weather information might
update the temperature hourly throughout the day. A stock market widget could
update its content frequently during open market hours, but not at all over
the weekend. By planning these times in advance, WidgetKit automatically
refreshes your widget when the appropriate time arrives.

When you define your widget, you implement a custom `TimelineProvider`.
WidgetKit gets a timeline from your provider, and uses it to track when to
update your widget. A timeline is an array of `TimelineEntry` objects. Each
entry in the timeline has a date and time, and additional information the
widget needs to display its view. In addition to the timeline entries, the
timeline specifies a refresh policy that tells WidgetKit when to request a new
timeline.

The following is an example of a game widget that displays a character’s
health level. When the health level is less then 100 percent, the character
recovers at a rate of 25 percent per hour. For example, when the character’s
health level is 25 percent, it takes 3 hours to fully recover to 100 percent.
The following diagram shows how WidgetKit requests the timeline from the
provider, rendering the widget at each time specified in the timeline entries.

When WidgetKit initially requests the timeline, the provider creates one with
four entries. The first entry represents the current time, followed by three
entries at hourly intervals. With the refresh policy set to the default
`atEnd`, WidgetKit requests a new timeline after the last date in the
timeline’s entries. When each date in the timeline arrives, WidgetKit invokes
the widget’s content closure and displays the result. After the last timeline
entry passes, WidgetKit repeats the process by asking the provider for a new
timeline. Because the character’s health has reached 100 percent, the provider
responds with a single entry for the current time and a refresh policy set to
`never`. With this setting, WidgetKit doesn’t ask for another timeline until
the app uses `WidgetCenter` to tell WidgetKit to request a new timeline.

In addition to the `atEnd` and `never` refresh policies, a provider can
specify a different date altogether if the timeline might change before or
after reaching the end of the entries. For example, if a dragon will appear in
2 hours to challenge the character to a battle, the provider sets the reload
policy to `after(_:)`, passing a date 2 hours in the future. The following
diagram shows how WidgetKit, after rendering the widget at the 2-hour mark,
requests a new one.

Due to the battle with the dragon, the character’s healing will take 2
additional hours to reach 100 percent. The new timeline consists of two
entries, one for the current time, and a second entry 2 hours in the future.
The timeline specifies `atEnd` for the refresh policy, indicating there are no
more known events that might alter the timeline.

When the 2 hours have passed, and the character’s health is at 100 percent,
WidgetKit asks the provider for a new timeline. Because the character’s health
has recovered, the provider generates the same final timeline as the first
diagram above. When the user plays the game and the character’s health level
changes, the app uses `WidgetCenter` to have WidgetKit refresh the timeline
and update the widget.

In addition to specifying a date _before_ the end of the timeline, the
provider can specify a date _after_ the end of the timeline. This is useful
when you know that the widget’s state will not change until a later time. For
example, a stock market widget could create a timeline at the close of the
market on Friday with an `after(_:)` refresh policy specifying the time the
market opens on Monday. Because the stock market is closed over the weekend,
there is no need to update the widget until the market opens.

Important

Plan ahead if your widget makes requests to a server when it reloads and uses
`after(_:)` with a specific date in timeline entries. WidgetKit tries to
respect the date you specify, which may cause a significant increase in server
load when multiple devices reload your widget at around the same time.

### Inform WidgetKit when a timeline changes

Your app can tell WidgetKit to request a new timeline when something affects a
widget’s current timeline. In the game widget example above, if the app
receives a push notification indicating a teammate has given the character a
healing potion, the app can tell WidgetKit to reload the timeline and update
the widget’s content. To reload a specific type of widget, your app uses
`WidgetCenter`, as shown here:

The `kind` parameter contains the same string as the value used to create the
widget’s `WidgetConfiguration`.

If your widgets have user-configurable properties, avoid unnecessary reloads
by using WidgetCenter to verify that a widget with the appropriate settings
exists. For example, when the game receives a push notification about a
character receiving a healing potion, it verifies that a widget is showing
that character before reloading the timeline.

In the following code, the app calls `getCurrentConfigurations(_:)` to
retrieve the list of user-configured widgets. It then iterates through the
resulting `WidgetInfo` objects to find one with an `intent` configured with
the character that received the healing potion. If it finds one, the app calls
`reloadTimelines(ofKind:)` for that widget’s `kind`.

If your app uses `WidgetBundle` to support multiple widgets, you can use
`WidgetCenter` to reload the timelines for all your widgets. For example, if
your widgets require the user to sign in to an account but they have signed
out, you can reload all the widgets by calling:

### Display dynamic dates

Even though your widget doesn’t run continually, it can display time-based
information that WidgetKit updates live. For example, it might display a
countdown timer that continues to count down even if your widget extension
isn’t running. For more information, see Displaying dynamic dates in widgets.

### Load data from your server before updating the timeline

You may need to load new data from your server before reloading a timeline. To
do this, use the system’s URL loading system and a `URLSession`. To learn
more, see Making network requests in a widget extension.

## See Also

### Timeline management

`protocol TimelineProvider`

A type that advises WidgetKit when to update a widget’s display.

`protocol IntentTimelineProvider`

A type that advises WidgetKit when to update a user-configurable widget’s
display.

`struct TimelineProviderContext`

An object that contains details about how a widget is rendered, including its
size and whether it appears in the widget gallery.

`protocol TimelineEntry`

A type that specifies the date to display a widget, and, optionally, indicates
the current relevance of the widget’s content.

`struct Timeline`

An object that specifies a date for WidgetKit to update a widget’s view.

`class WidgetCenter`

An object that contains a list of user-configured widgets and is used for
reloading widget timelines.

`protocol AppIntentTimelineProvider`

A type that advises WidgetKit when to update a user-configurable widget’s
display.

Article

# Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

## Overview

To make the most relevant information easily accessible to people, widgets can
provide customizable properties. For example, a person can select a specific
stock for a stock quote widget, or enter a tracking number for a package
delivery widget. Widgets define customizable properties by using app intents,
the same mechanism that Siri Suggestions and Siri Shortcuts use for
customizing those interactions.

To add configurable properties to your widget:

  1. Add custom app intent types that conform to `WidgetConfigurationIntent` to define the configurable properties to your Xcode project.

  2. Specify an `AppIntentTimelineProvider` as your widget’s timeline provider to incorporate the person’s choices into your timeline entries.

  3. Add code to your custom app intent types to provide the data if their properties rely on dynamic data.

If your app already supports Siri Suggestions or Siri Shortcuts and you have a
custom app intent, you’ve probably done most of the work already. Otherwise,
consider leveraging the work you do for your widget to add support for Siri
Suggestions or Siri Shortcuts. For more information on how to get the most
from app intents, see App Intents.

Note

Prior to iOS 17, iPadOS 17, and macOS 14, configurable widgets used SiriKit
Intents. For information on migrating your configurable widgets from the
SiriKit Intents to the App Intents framework, see Migrating widgets from
SiriKit Intents to App Intents.

### Add a custom app intent to your project

To show the character’s information, the person needs a way to select the
character. The following code shows how to define a custom app intent to
represent the choice the person makes:

The static `title` property describes the action the intent enables the person
to take. Use a title case string that combines a verb with a noun. Set the
static `description` to a human-readable string that describes the intent.

To add parameters to the intent, add one or more `@Parameter` property
wrappers. WidgetKit uses the parameter type information to automatically
create the user interface for editing the widget. For example, if the type is
`String`, the person enters a string value. If the type is an `Int`, they use
a number pad. For a parameter that is a predefined, static, list of values,
define a custom type that conforms to `AppEnum`.

Note

The order of the parameters in the intent determines the order in which they
appear when a person edits your widget.

In the example above, the parameter uses a custom `CharacterDetail` type the
app defines to represent a character in the game. To use a custom type as an
app intent parameter, it must conform to `AppEntity`. To implement the
`CharacterDetail` parameter type, the game-status widget uses a structure that
exists in the game’s project. This structure defines a list of available
characters and their details, as follows:

Because characters might vary from game to game, the intent generates the list
dynamically at runtime. WidgetKit uses the app entity’s `defaultQuery`
property to access the dynamic values, as described below.

If your widget includes nonoptional parameters, you must supply a default
value. For types such as `String`, `Int`, or enumerations that use `AppEnum`,
one option is to supply a default value as follows:

A second option is to use a query type that implements `defaultResult()`, as
shown in the next section.

For custom intents with parameters that conform to `AppEntity`, implement
initializer methods to provide default values for the nonoptional parameters,
such as the `init(character:)` method in the code for `SelectCharacterIntent`
shown above. In your timeline provider’s `placeholder(in:)` method, use one of
these initializer methods to initialize the app intent that you pass to the
timeline entry. These methods enable you to customize the placeholder with
values that might be different from the default, if needed.

### Implement a query to provide dynamic values

Some of the tasks that an `EntityQuery` performs include:

  * Mapping `AppEntity` identifiers to the corresponding entity instances.

  * Providing a list of suggested values when a person edits a widget.

  * Specifying a default value for a parameter.

When a person edits a widget with a custom intent that provides dynamic
values, the system invokes the query object’s `suggestedEntities()` method to
get the list of possible choices.

In the entity query, the result is an array of all the `CharacterDetail` types
available.

With the configuration of the custom app intent done, a person can edit the
widget to select a specific character to display.

After the person edits the widget and selects a character, the next step is to
incorporate that choice into the widget’s display.

### Handle customized values in your widget

To support configurable properties, a widget uses the
`AppIntentTimelineProvider` configuration. For example, the character-details
widget defines its configuration as follows:

The `SelectCharacterIntent` parameter determines the customizable properties
for the widget. The configuration uses `CharacterDetailProvider` to manage the
timeline events for the widget. For more information about timeline providers,
see Keeping a widget up to date.

After a person edits the widget, WidgetKit passes the customized values to the
provider when requesting timeline entries. You typically include relevant
details from the intent in the timeline entries the provider generates. In the
following example, the provider uses the `defaultQuery` to look up the
`CharacterDetail` using the character’s `id` in the intent, and then creates a
timeline with an entry containing the character’s detail:

When you include the customized values in the timeline entry, your widget’s
view can display the appropriate content.

### Access customized values in your app

When a person taps on a widget to open your app, WidgetKit passes the
customized intent to your app in an `NSUserActivity`. In your app’s code that
handles the user activity, such as `onContinueUserActivity(_:perform:)` for a
SwiftUI app or `scene(_:continue:)` for a UIKit app, use the
`widgetConfigurationIntent(of:)` method to access the widget’s intent.

To access the intent of any widget that the user has installed, use
`getCurrentConfigurations(_:)` to fetch the `WidgetInfo` objects. Iterate over
the `WidgetInfo` objects and call `widgetConfigurationIntent(of:)`.

### Offer preconfigured complications on Apple Watch

Starting in watchOS 9, iOS 16, and iPadOS 17, you can use WidgetKit to
implement accessory-family widgets that appear as complications on Apple
Watch. Like widgets in iOS and macOS, watch complications use custom intents
to display user-configurable data, and implementing configurable widgets in
watchOS works the same as in iOS or macOS. However, watchOS doesn’t offer a
dedicated user interface for configuring complications. To display data that’s
most relevant to the user in your watch complication, you can create
preconfigured complications and recommend them to your users in the list of
available complications.

In your `AppIntentTimelineProvider` code, implement `recommendations()` and
return the `AppIntentRecommendation` objects you create using your custom
intents.

When your app receives new data that’s relevant to your recommended widget
configurations, invalidate the now outdated recommendations by calling
`invalidateConfigurationRecommendations()`. This tells WidgetKit to get new
recommendations for your preconfigured complications. When you invalidate the
recommendations for preconfigured complications, make sure you return updated
`AppIntentRecommendation` objects in the `recommendations()` callback.

## See Also

### Configurable widgets

Migrating widgets from SiriKit Intents to App Intents

Configure your widgets for backward compatibility.

`struct AppIntentConfiguration`

An object describing the content of a widget that uses a custom intent to
provide user-configurable options.

`struct WidgetInfo`

A structure that contains information about user-configured widgets.

`struct AppIntentRecommendation`

An object that describes a recommended intent configuration for a user-
customizable widget.

`struct IntentConfiguration`

An object describing the content of a widget that uses a custom intent
definition to provide user-configurable options.

`struct IntentRecommendation`

An object that describes a recommended intent configuration for a user-
customizable widget.

Protocol

# Widget

The configuration and content of a widget to display on the Home screen or in
Notification Center.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    protocol Widget

## Overview

Widgets show glanceable and relevant content from your app right on the iOS
Home screen or in Notification Center on macOS. Users can add, configure, and
arrange widgets to suit their individual needs. You can provide multiple types
of widgets, each presenting a specific kind of information. When users want
more information, like to read the full article for a headline or to see the
details of a package delivery, the widget lets them get to the information in
your app quickly.

There are three key components to a widget:

  * A configuration that determines whether the widget is configurable, identifies the widget, and defines the SwiftUI views that show the widget’s content.

  * A timeline provider that drives the process of updating the widget’s view over time.

  * SwiftUI views used by WidgetKit to display the widget.

For information about adding a widget extension to your app, and keeping your
widget up to date, see Creating a widget extension and Keeping a widget up to
date, respectively.

By adding a custom SiriKit intent definition, you can let users customize
their widgets to show the information that’s most relevant to them. If you’ve
already added support for Siri or Shortcuts, you’re well on your way to
supporting customizable widgets. For more information, see Making a
configurable widget.

## Topics

### Implementing a widget

`var body: Self.Body`

The content and behavior of the widget.

**Required**

` associatedtype Body : WidgetConfiguration`

The type of configuration representing the content of the widget.

**Required**

### Running a widget

`init()`

Creates a widget using `body` as its content.

**Required**

` static func main()`

Initializes and runs the widget.

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Protocol

# WidgetBundle

A container used to expose multiple widgets from a single widget extension.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    protocol WidgetBundle

## Overview

To support multiple types of widgets, add the `@main` attribute to a structure
that conforms to `WidgetBundle`. For example, a game might have one widget to
display summary information about the game and a second widget to display
detailed information about individual characters.

## Topics

### Implementing a widget bundle

`var body: Self.Body`

Declares the group of widgets that an app supports.

**Required**

` associatedtype Body : Widget`

The type of widget that represents the content of the bundle.

**Required**

` struct WidgetBundleBuilder`

A custom attribute that constructs a widget bundle’s body.

### Running a widget bundle

`init()`

Creates a widget bundle using the bundle’s body as its content.

**Required**

` static func main()`

Initializes and runs the widget bundle.

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Structure

# LimitedAvailabilityConfiguration

A type-erased widget configuration.

iOS 16.1+  iPadOS 16.1+  macOS 13.0+  Mac Catalyst 16.1+  watchOS 9.1+
visionOS 1.0+

    
    
    @frozen
    struct LimitedAvailabilityConfiguration

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `WidgetConfiguration`

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Protocol

# WidgetConfiguration

A type that describes a widget’s content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    protocol WidgetConfiguration

## Topics

### Implementing a widget

`var body: Self.Body`

The content and behavior of this widget.

**Required**

` associatedtype Body : WidgetConfiguration`

The type of widget configuration representing the body of this configuration.

**Required**

### Setting a name

`func configurationDisplayName<S>(S) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
specified string.

`func configurationDisplayName(Text) -> some WidgetConfiguration`

Sets the name shown for a widget when a user adds or edits it using the
contents of a text view.

`func configurationDisplayName(LocalizedStringKey) -> some
WidgetConfiguration`

Sets the localized name shown for a widget when a user adds or edits the
widget.

### Setting a description

`func description(Text) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
contents of a text view.

`func description<S>(S) -> some WidgetConfiguration`

Sets the description shown for a widget when a user adds or edits it using the
specified string.

`func description(LocalizedStringKey) -> some WidgetConfiguration`

Sets the localized description shown for a widget when a user adds or edits
the widget.

### Setting the appearance

`func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration`

Sets the sizes that a widget supports.

`func contentMarginsDisabled() -> some WidgetConfiguration`

Disable default content margins.

`func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some
WidgetConfiguration`

Sets the disfavored locations for a widget.

`func containerBackgroundRemovable(Bool) -> some WidgetConfiguration`

A modifier that marks the background of a widget as removable.

### Managing background tasks

`func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) ->
some WidgetConfiguration`

Runs the given action when the system provides a background task.

`func onBackgroundURLSessionEvents(matching: ((String) -> Bool)?, (String, ()
-> Void) -> Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session identified by a
closure are waiting to be processed.

`func onBackgroundURLSessionEvents(matching: String, (String, () -> Void) ->
Void) -> some WidgetConfiguration`

Adds an action to perform when events related to a URL session with a matching
identifier are waiting to be processed.

## Relationships

### Conforming Types

  * `EmptyWidgetConfiguration`
  * `LimitedAvailabilityConfiguration`

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`struct EmptyWidgetConfiguration`

An empty widget configuration.

Structure

# EmptyWidgetConfiguration

An empty widget configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  watchOS 9.0+
visionOS 1.0+

    
    
    @frozen
    struct EmptyWidgetConfiguration

## Topics

### Creating a configuration

`init()`

## Relationships

### Conforms To

  * `Sendable`
  * `WidgetConfiguration`

## See Also

### Creating widgets

Building Widgets Using WidgetKit and SwiftUI

Create widgets to show your app’s content on the Home screen, with custom
intents for user-customizable settings.

Creating a widget extension

Display your app’s content in a convenient, informative widget on various
devices.

Keeping a widget up to date

Plan your widget’s timeline to show timely, relevant information using dynamic
views, and update the timeline when things change.

Making a configurable widget

Give people the option to customize their widgets by adding a custom app
intent to your project.

`protocol Widget`

The configuration and content of a widget to display on the Home screen or in
Notification Center.

`protocol WidgetBundle`

A container used to expose multiple widgets from a single widget extension.

`struct LimitedAvailabilityConfiguration`

A type-erased widget configuration.

`protocol WidgetConfiguration`

A type that describes a widget’s content.

Instance Method

# widgetLabel(_:)

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<S>(_ label: S) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

A string that contains the text which WidgetKit displays alongside the
complication.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style. For
example, setting the font and rendering the text along a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(_:)

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel(_ labelKey: LocalizedStringKey) -> some View
    

##  Parameters

`labelKey`

    

A label generated from a localized string.

## Discussion

To add a text label to an accessory family widget, call this method on the
widget’s main SwiftUI view, and pass in a supported `LocalizedStringKey`. The
system determines whether it can use the text label. If it can’t, it ignores
the label. The system also sets the label’s size, placement, and style based
on the clock face. For example, setting the font and rendering the text along
a curve.

The following widget families support text accessory labels:

  * The `WidgetFamily.accessoryCorner` widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.

  * The `WidgetFamily.accessoryCircular` widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel<Label>(label: () -> Label) -> some View`

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

Instance Method

# widgetLabel(label:)

Creates a label for displaying additional content outside an accessory family
widget’s main SwiftUI view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  watchOS 9.0+  visionOS 1.0+

    
    
    func widgetLabel<Label>(@ViewBuilder label: () -> Label) -> some View where Label : View
    

##  Parameters

`label`

    

A view that WidgetKit can display alongside the accessory family widget’s main
SwiftUI view. You can use a `Image`, `Text`, `Gauge`, `ProgressView`, or a
container with multiple subviews.

## Discussion

The system only displays labels on widget-based complications in watchOS. The
system ignores any labels attached to widgets on the Lock Screen on iPhone.
Therefore, you can use the same code to display an accessory family widget on
both iPhone and Apple Watch.

To create the widget label, call `widgetLabel(label:)`on a complication’s main
SwiftUI view. Pass the desired content as the `label` parameter. The label can
be a `Gauge`, `ProgressView`, `Text`, or `Image`. To provide multiple views,
wrap your views in a container, such as a `VStack`. WidgetKit determines
whether it can use any of the label’s content. If it can’t, it ignores the
label.

WidgetKit configures the label so that the watch face presents a unified look.
For example, it sets the size for an image, the font for text, and can even
render text and gauges along a curve.

The following widget families support widget labels:

`WidgetKit/WidgetFamily/accessoryCorner`

    

In watchOS, this widget-based complication can display a `Gauge`, a
`ProgressView`, or a `Text`. Adding a label to an accessory corner causes the
main SwiftUI view to shrink to make space for the label. If you pass a view
containing multiple, valid subviews, the system picks which view to display as
the widget label.

`WidgetKit/WidgetFamily/accessoryCircular`

    

In watchOS, the widget-based complication can display either an `Image` or a
`Text`. To pass both an image and text, wrap those views in a container.

However, WidgetKit only renders the label along the bezel on the Infograph
watch face (the top circular complication). On all other circular
complications — including widgets on all other platforms — WidgetKit ignores
the label.

## See Also

### Labeling a widget

`func widgetLabel<S>(S) -> some View`

Returns a text label that displays additional content outside the accessory
family widget’s main SwiftUI view.

`func widgetLabel(LocalizedStringKey) -> some View`

Returns a localized text label that displays additional content outside the
accessory family widget’s main SwiftUI view.

Instance Method

# widgetAccentable(_:)

Adds the view and all of its subviews to the accented group.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    func widgetAccentable(_ accentable: Bool = true) -> some View
    

##  Parameters

`accentable`

    

A Boolean value that indicates whether to add the view and its subviews to the
accented group.

## Discussion

When the system renders the widget using the
`WidgetKit/WidgetRenderingMode/accented` mode, it divides the widget’s view
hierarchy into two groups: the accented group and the default group. It then
applies a different color to each group.

When applying the colors, the system treats the widget’s views as if they were
template images. It ignores the view’s color — rendering the new colors based
on the view’s alpha channel.

To control your view’s appearance, add the `widgetAccentable(_:)` modifier to
part of your view’s hierarchy. If the `accentable` parameter is `true`, the
system adds that view and all of its subviews to the accent group. It puts all
other views in the default group.

Important

After you call `widgetAccentable(true)` on a view moving it into the accented
group, calling `widgetAccentable(false)` on its subviews doesn’t move the
subviews back into the default group.

Instance Method

# dynamicIsland(verticalPlacement:)

Specifies the vertical placement for a view of an expanded Live Activity that
appears in the Dynamic Island.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  visionOS 1.0+

    
    
    func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View
    

##  Parameters

`verticalPlacement`

    

The vertical placement for a view that’s part of an expanded Live Activity in
the Dynamic Island.

## Return Value

A view with the specified vertical placement.

