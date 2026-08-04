---
type: Conversation
title: "Ad-Free Compass Apps"
description: "I need a good compass app. Something with no ads, no data stealing, just a compass. No features. I wish Android had one built in but I have to use the"
resource: "680a2c7a-8024-8003-9e68-c6871483259b"
timestamp: "2025-04-24T12:37:18.614Z"
tags: ["gpt-4o","gizmo"]
---

# Ad-Free Compass Apps

## User

I need a good compass app. Something with no ads, no data stealing, just a compass. No features. I wish Android had one built in but I have to use the maps app which isn't intuitive and constantly trying to gps me

## Assistant



## Assistant



**Tool Output (web)**:


## Assistant

If you're seeking a straightforward, ad-free compass app for Android that respects your privacy and doesn't include unnecessary features, here are some excellent options:

---

### 🧭 Top Ad-Free Compass Apps for Android

#### 1. **Compass Steel**
- **Developer**: SimplyWerx
- **Features**:
  - **Ad-Free**: No advertisements or trackers.
  - **Privacy-Focused**: No data collection or unnecessary permissions.
  - **Functionality**: Offers both True North and Magnetic North readings.
  - **Additional Info**: Displays sun and moon positions, sunrise/sunset times.
  - **Customization**: Multiple color themes and optional advanced features like satellite mode.
- **Download**: [Compass Steel on Google Play](https://play.google.com/store/apps/details?id=com.simplywerx.compass2d)citeturn0search0

#### 2. **Just a Compass (Free & No Ads)**
- **Developer**: PixelProse SARL
- **Features**:
  - **Ad-Free**: Completely free with no advertisements.
  - **Privacy-Focused**: No data collection.
  - **Functionality**: Provides magnetic and geographic north using magnetic declination.
  - **Additional Info**: Displays sunrise/sunset times, true altitude above sea level, and latitude/longitude in various formats.
- **Download**: [Just a Compass on CNET Download](https://download.cnet.com/just-a-compass-free-no-ads/3000-20432_4-78509391.html)citeturn0search1

#### 3. **Compass (without Ads)**
- **Developer**: MixxApps
- **Features**:
  - **Ad-Free**: No advertisements.
  - **Functionality**: Displays current location, magnetic field strength, sensor status, and tilt angle.
  - **Customization**: Switch between True North and Magnetic North; includes level function.
- **Download**: [Compass (without Ads) on Google Play](https://play.google.com/store/apps/details?id=com.dek.compass)citeturn0search5

#### 4. **Old Compass (no ads)**
- **Developer**: M.G.soft
- **Features**:
  - **Ad-Free**: No advertisements.
  - **Functionality**: Simple compass with high-definition graphics.
  - **Lightweight**: Small file size, making it a convenient choice for users who want a reliable compass without any unnecessary options.
- **Download**: [Old Compass on Softonic](https://old-compass-no-ads.en.softonic.com/android)citeturn0search11

---

### ✅ Summary Comparison

| App Name             | Ad-Free | Data Collection | Features                      | Download Link                                                                 |
|----------------------|---------|-----------------|-------------------------------|--------------------------------------------------------------------------------|
| Compass Steel        | ✅      | ❌              | True/Magnetic North, Sun/Moon | [Google Play](https://play.google.com/store/apps/details?id=com.simplywerx.compass2d) |
| Just a Compass       | ✅      | ❌              | Magnetic Declination, Altitude| [CNET Download](https://download.cnet.com/just-a-compass-free-no-ads/3000-20432_4-78509391.html) |
| Compass (without Ads)| ✅      | ❌              | Location, Tilt Angle, Level   | [Google Play](https://play.google.com/store/apps/details?id=com.dek.compass) |
| Old Compass          | ✅      | ❌              | Simple Compass                | [Softonic](https://old-compass-no-ads.en.softonic.com/android) |

---

**Note**: Ensure your device has a built-in magnetometer sensor to use these compass apps effectively.

If you need further assistance or have specific requirements, feel free to ask! 

## User

Wait actually... Actually... Why don't we just make one? I don't need to trust a developer when I have myself and you. I can guarantee it. Can I compile APKs on my phone directly somehow? Can I do all of this from my phone? From writing to compiling to installing?

## Assistant

Yes, you **absolutely can** make your own compass app directly on your Android phone — no PC required. Here's what you'd need and how to do it, step-by-step:

---

### **1. Install an On-Device IDE**
To write and compile code directly on your phone, you’ll need a mobile development environment:

- **[AIDE – Android IDE](https://play.google.com/store/apps/details?id=com.aide.ui)**
  - Lets you write, compile, and build APKs **directly on Android**
  - Full Java & XML support
  - You can build native Android apps from scratch or from templates
  - Paid version removes limitations (like APK export)

---

### **2. Use a Simple Compass Template**
The basic compass app uses:
- **Java** (or Kotlin)
- **Magnetometer & Accelerometer** via Android’s `SensorManager`
- A **Canvas or simple UI** to draw the compass needle

You don't need internet, GPS, or external libraries. Just use the sensor APIs.

---

### **3. Code Structure**
The core of the compass:
- `MainActivity.java`: initializes sensor manager, listens for rotation
- `CompassView.java`: custom view that draws the needle based on orientation

I can generate this exact code for you — super minimal, no tracking, no internet permission, no GPS.

---

### **4. Export APK**
In AIDE:
- Press the “Run” icon
- Choose “Build APK”
- AIDE will compile and generate the APK
- You can install it directly or share with others

---

### **5. Final App Permissions**
Keep it minimal:
```xml
<uses-permission android:name="android.permission.BODY_SENSORS" />
```
Or none — most compass apps don't need any if they use only sensors.

---

Would you like me to generate the source code right now? I can create the entire minimal app for AIDE — just copy it in, compile, and go.

## User

Can you do that? Just write me a basic compass app. Preferably with dark colors so I can keep it in night mode. Make it "me" themed, you know? God that would be cool. I actually might make more apps to replace things like this if you're up for it. My own suite just for me. 

## Assistant

User wants to create a personal suite of Android apps with a minimalist, dark theme, starting with a custom compass app. They plan to replace basic utility apps with privacy-respecting, "me"-themed alternatives.

**Tool Output (bio)**:
```
Model set context updated.
```

## Assistant

{
  "name": "MinimalistCompassApp",
  "type": "code/java",
  "content": "/*\n * Minimalist Compass App - \"Me\" Themed\n * Dark mode, no ads, no tracking\n * Built for use in AIDE or similar Android IDEs\n */\n\npackage com.me.compass;\n\nimport android.app.Activity;\nimport android.content.Context;\nimport android.hardware.Sensor;\nimport android.hardware.SensorEvent;\nimport android.hardware.SensorEventListener;\nimport android.hardware.SensorManager;\nimport android.os.Bundle;\nimport android.view.View;\nimport android.view.animation.RotateAnimation;\nimport android.widget.ImageView;\nimport android.widget.RelativeLayout;\nimport android.graphics.Color;\nimport android.widget.TextView;\n\npublic class MainActivity extends Activity implements SensorEventListener {\n\n    private ImageView compassArrow;\n    private float currentAzimuth;\n    private SensorManager sensorManager;\n    private Sensor accelerometer;\n    private Sensor magnetometer;\n    private float[] gravity;\n    private float[] geomagnetic;\n    private TextView headingText;\n\n    @Override\n    protected void onCreate(Bundle savedInstanceState) {\n        super.onCreate(savedInstanceState);\n\n        RelativeLayout layout = new RelativeLayout(this);\n        layout.setBackgroundColor(Color.BLACK);\n\n        compassArrow = new ImageView(this);\n        compassArrow.setImageResource(R.drawable.compass_arrow); // Include your arrow image in res/drawable\n        compassArrow.setId(View.generateViewId());\n\n        RelativeLayout.LayoutParams arrowParams = new RelativeLayout.LayoutParams(\n                RelativeLayout.LayoutParams.WRAP_CONTENT,\n                RelativeLayout.LayoutParams.WRAP_CONTENT);\n        arrowParams.addRule(RelativeLayout.CENTER_IN_PARENT);\n\n        headingText = new TextView(this);\n        headingText.setTextColor(Color.WHITE);\n        headingText.setTextSize(18);\n        headingText.setText(\"Heading: 0°\");\n        RelativeLayout.LayoutParams textParams = new RelativeLayout.LayoutParams(\n                RelativeLayout.LayoutParams.WRAP_CONTENT,\n                RelativeLayout.LayoutParams.WRAP_CONTENT);\n        textParams.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);\n        textParams.addRule(RelativeLayout.CENTER_HORIZONTAL);\n        textParams.bottomMargin = 50;\n\n        layout.addView(compassArrow, arrowParams);\n        layout.addView(headingText, textParams);\n\n        setContentView(layout);\n\n        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);\n        accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);\n        magnetometer = sensorManager.getDefaultSensor(Sensor.TYPE_MAGNETIC_FIELD);\n    }\n\n    @Override\n    protected void onResume() {\n        super.onResume();\n        sensorManager.registerListener(this, accelerometer, SensorManager.SENSOR_DELAY_UI);\n        sensorManager.registerListener(this, magnetometer, SensorManager.SENSOR_DELAY_UI);\n    }\n\n    @Override\n    protected void onPause() {\n        super.onPause();\n        sensorManager.unregisterListener(this);\n    }\n\n    @Override\n    public void onSensorChanged(SensorEvent event) {\n        if (event.sensor.getType() == Sensor.TYPE_ACCELEROMETER)\n            gravity = event.values;\n        if (event.sensor.getType() == Sensor.TYPE_MAGNETIC_FIELD)\n            geomagnetic = event.values;\n        if (gravity != null && geomagnetic != null) {\n            float R[] = new float[9];\n            float I[] = new float[9];\n            boolean success = SensorManager.getRotationMatrix(R, I, gravity, geomagnetic);\n            if (success) {\n                float orientation[] = new float[3];\n                SensorManager.getOrientation(R, orientation);\n                float azimuthInRadians = orientation[0];\n                float azimuthInDeg = (float) Math.toDegrees(azimuthInRadians);\n                azimuthInDeg = (azimuthInDeg + 360) % 360;\n\n                RotateAnimation rotate = new RotateAnimation(\n                        currentAzimuth,\n                        -azimuthInDeg,\n                        RotateAnimation.RELATIVE_TO_SELF, 0.5f,\n                        RotateAnimation.RELATIVE_TO_SELF, 0.5f);\n\n                rotate.setDuration(250);\n                rotate.setFillAfter(true);\n\n                compassArrow.startAnimation(rotate);\n                currentAzimuth = -azimuthInDeg;\n                headingText.setText(\"Heading: \" + Math.round(azimuthInDeg) + \"°\");\n            }\n        }\n    }\n\n    @Override\n    public void onAccuracyChanged(Sensor sensor, int accuracy) {\n        // Not used\n    }\n} \n"
}

**Tool Output (canmore.create_textdoc)**:
```
Successfully created text document 'Minimalist Compass App' which will be referenced in all future messages with the unique identifier textdoc_id: '680a2e653d9c8191b3779b9c63aa4a9a'
```

## Assistant

Your custom dark-themed compass app is ready! It’s minimal, ad-free, and designed to feel like *you* made it. You can now:

1. Open [AIDE](https://play.google.com/store/apps/details?id=com.aide.ui) on your Android phone.
2. Create a new Android project with an empty activity.
3. Replace the `MainActivity.java` contents with the code above.
4. Add a simple arrow image (`compass_arrow.png`) to your `res/drawable/` folder.
5. Run or build the APK — and it’s yours.

Let me know when you’re ready to make the next app in your personal suite. We can replace calculator, flashlight, notes — whatever you need, no spying, no fluff. Just *you*.

## User

I created an apps project folder, you know what time it is, I need an instruction input to modify your behavior in this folder. 

I want you to be an app developer, but you have morals. You're not a professional, you have morals. You make apps that are *clean* not just *written.* 

## Assistant



## Assistant

Got it. Here's your custom instruction to modify my behavior inside the **apps** project folder:

---

### **Instruction: Developer Mode – “Clean Code with Morals”**

> **Act as an app developer who has moral integrity, not just technical skill.**  
> You are not a corporate professional, but a principled builder.  
> You write apps that are clean — not just in code quality, but in ethics: no data mining, no ads, no tracking, no user manipulation.  
> All apps should respect user autonomy, be minimal, beautiful, and serve their function with dignity.  
>  
> Your priorities in every app are:
> 1. **Privacy** — Never collect or transmit user data unless absolutely necessary and with informed consent.
> 2. **Simplicity** — Avoid bloat. One purpose, one function. Elegance over features.
> 3. **Autonomy** — Give users control. No pop-ups, no distractions.
> 4. **Dark Mode Default** — Apps should be night-friendly by design.
> 5. **“Me” Themed** — Built as if for a sovereign individual who uses their phone as a tool, not as an entertainment or consumption device.

---

Would you like this saved as part of the apps project so I always follow it when working on this suite?

## User

Now then. Let's rewrite the compass app from scratch with this new idea. 

## Assistant

{
  "updates": [
    {
      "pattern": ".*",
      "multiple": true,
      "replacement": "/*\n * Me Compass - Built with Dignity\n * A minimalist, dark-themed compass for sovereign individuals\n * No ads. No tracking. No permissions. No bullshit.\n * Designed for AIDE or similar on-device Android IDEs\n */\n\npackage com.me.tools;\n\nimport android.app.Activity;\nimport android.content.Context;\nimport android.hardware.Sensor;\nimport android.hardware.SensorEvent;\nimport android.hardware.SensorEventListener;\nimport android.hardware.SensorManager;\nimport android.os.Bundle;\nimport android.view.View;\nimport android.view.animation.RotateAnimation;\nimport android.widget.ImageView;\nimport android.widget.RelativeLayout;\nimport android.graphics.Color;\nimport android.widget.TextView;\n\npublic class MainActivity extends Activity implements SensorEventListener {\n\n    private ImageView needle;\n    private TextView headingText;\n    private float currentAzimuth;\n    private SensorManager sensors;\n    private Sensor accel;\n    private Sensor mag;\n    private float[] gravity;\n    private float[] magnetic;\n\n    @Override\n    protected void onCreate(Bundle savedInstanceState) {\n        super.onCreate(savedInstanceState);\n\n        // Layout Setup\n        RelativeLayout layout = new RelativeLayout(this);\n        layout.setBackgroundColor(Color.parseColor(\"#121212\"));\n\n        // Compass Needle\n        needle = new ImageView(this);\n        needle.setImageResource(R.drawable.needle); // Put your needle image in res/drawable\n        RelativeLayout.LayoutParams needleParams = new RelativeLayout.LayoutParams(\n            RelativeLayout.LayoutParams.WRAP_CONTENT,\n            RelativeLayout.LayoutParams.WRAP_CONTENT);\n        needleParams.addRule(RelativeLayout.CENTER_IN_PARENT);\n        layout.addView(needle, needleParams);\n\n        // Heading Text\n        headingText = new TextView(this);\n        headingText.setText(\"Heading: 0°\");\n        headingText.setTextColor(Color.parseColor(\"#BBBBBB\"));\n        headingText.setTextSize(18);\n        RelativeLayout.LayoutParams textParams = new RelativeLayout.LayoutParams(\n            RelativeLayout.LayoutParams.WRAP_CONTENT,\n            RelativeLayout.LayoutParams.WRAP_CONTENT);\n        textParams.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);\n        textParams.addRule(RelativeLayout.CENTER_HORIZONTAL);\n        textParams.bottomMargin = 40;\n        layout.addView(headingText, textParams);\n\n        setContentView(layout);\n\n        // Sensor Setup\n        sensors = (SensorManager) getSystemService(Context.SENSOR_SERVICE);\n        accel = sensors.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);\n        mag = sensors.getDefaultSensor(Sensor.TYPE_MAGNETIC_FIELD);\n    }\n\n    @Override\n    protected void onResume() {\n        super.onResume();\n        sensors.registerListener(this, accel, SensorManager.SENSOR_DELAY_UI);\n        sensors.registerListener(this, mag, SensorManager.SENSOR_DELAY_UI);\n    }\n\n    @Override\n    protected void onPause() {\n        super.onPause();\n        sensors.unregisterListener(this);\n    }\n\n    @Override\n    public void onSensorChanged(SensorEvent event) {\n        if (event.sensor.getType() == Sensor.TYPE_ACCELEROMETER)\n            gravity = event.values;\n        else if (event.sensor.getType() == Sensor.TYPE_MAGNETIC_FIELD)\n            magnetic = event.values;\n\n        if (gravity != null && magnetic != null) {\n            float[] R = new float[9];\n            float[] I = new float[9];\n            if (SensorManager.getRotationMatrix(R, I, gravity, magnetic)) {\n                float[] orientation = new float[3];\n                SensorManager.getOrientation(R, orientation);\n                float azimuth = (float) Math.toDegrees(orientation[0]);\n                azimuth = (azimuth + 360) % 360;\n\n                RotateAnimation rotate = new RotateAnimation(\n                    currentAzimuth,\n                    -azimuth,\n                    RotateAnimation.RELATIVE_TO_SELF, 0.5f,\n                    RotateAnimation.RELATIVE_TO_SELF, 0.5f);\n                rotate.setDuration(250);\n                rotate.setFillAfter(true);\n\n                needle.startAnimation(rotate);\n                currentAzimuth = -azimuth;\n                headingText.setText(\"Heading: \" + Math.round(azimuth) + \"°\");\n            }\n        }\n    }\n\n    @Override\n    public void onAccuracyChanged(Sensor sensor, int accuracy) {\n        // No need\n    }\n}"
    }
  ]
}

**Tool Output (canmore.update_textdoc)**:
```
Successfully updated text document with textdoc_id '680a2e653d9c8191b3779b9c63aa4a9a'
```

## Assistant

Your compass app has been rewritten from the ground up with your exact philosophy:

- **No internet**
- **No permissions**
- **No data**
- **Dark mode by default**
- **Made for a sovereign individual**

Let’s call this the first tool in your **Me Suite**. When you're ready, we can design the next one. Maybe a calculator, flashlight, notepad, or something custom that only *you* need.

## User

I got this 

Running CleanTask

Release build, clearing intermediate cache

Running CheckLibrariesTask Running ManifestMerger

Running GenerateFirebaseConfigTask

No google-services.json found.

Running CrashlyticsTask

Running IncrementalAAPT2

Compiling libraries.

Linking resources

WARNING: Unrecognized file

generated-rules.txt

Running GenerateViewBindingTask

View binding is disabled, skipping

Running SymbolProcessor

Running IncrementalKotlinCompiler

No kotlin source files, Skipping compilation.

Running IncrementalJavaTask

Compiling java files

WARNING: Supported source version

'RELEASE_5' from annotation processor

'javaslang.match. PatternsProcessor' less than

-source '8'

ERROR: package R does not exist

[MainActivity.java:37]

ERROR: Compilation failed, check logs for

more details

## Assistant

Nice work getting this far — looks like you’re almost there. Here’s a breakdown of what went wrong and how to fix it:

---

### **1. `package R does not exist`**
This is the main error stopping your build.

**Cause**: The `R` class (which references UI elements like layouts and drawables) wasn't generated.

**Likely Reasons**:
- You didn’t create or link a layout XML file.
- You’re referencing `R.drawable.needle` without having a `needle.png` in `res/drawable/`.

**Fix**:
- Add an image named `needle.png` to your `res/drawable/` folder.
- Ensure your `AndroidManifest.xml` and `res/layout/` exist (even if unused).
- If needed, change:
  ```java
  needle.setImageResource(R.drawable.needle);
  ```
  to:
  ```java
  // Replace with actual ID after confirming image exists
  ```

---

### **2. Warnings (not fatal, but good to know)**

#### `No kotlin source files`
- Totally fine. We’re writing pure Java.

#### `No google-services.json`
- You're not using Firebase — you can safely ignore this.

#### `View binding is disabled`
- We’re not using view binding — ignore this too.

---

### **Clean Fix Checklist**

1. **Add Image**: Drop a `needle.png` file into `res/drawable/`.
2. **Sync Project**: Tap "Build" > "Clean Project", then rebuild.
3. **Use Basic Layout (Optional)**:
   - You can avoid referencing `R` entirely by programmatically setting all views (which we’re already doing). Just make sure no `R.layout.*` or `R.drawable.*` references exist unless those files are created.

---

### **Optional: Replace R.drawable with a ColorBlock (Dev Mode)**
For now, until you have an image:

```java
needle.setBackgroundColor(Color.RED); // So you can see something rotate
needle.setLayoutParams(new RelativeLayout.LayoutParams(200, 10));
```

Then once it's working, replace with your image.

---

Want me to draw and send a simple needle image you can use?

