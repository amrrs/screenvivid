import QtQuick 6.7
import QtQuick.Controls 6.7

Item {
    id: timeSlider
    width: 20
    height: 220

    property string color: "#484554"
    property bool animationEnabled: true // Property to enable/disable animation

    Rectangle {
        id: timeSliderHead
        width: parent.width
        height: parent.width
        radius: parent.width / 2

        color: parent.color

        MouseArea {
            anchors.fill: parent

            drag {
                target: timeSlider
                axis: Drag.XAxis
                smoothed: true
                minimumX: 0
            }

            onReleased: {
                var currentFrame = Math.round(
                            timeSlider.x / studioWindow.pixelsPerFrame)
                videoController.jump_to_frame(currentFrame)
            }
        }
    }

    Rectangle {
        id: timeSliderBody
        width: 3
        height: parent.height
        anchors.horizontalCenter: parent.horizontalCenter
        color: parent.color
    }

    Behavior on x {
        enabled: animationEnabled
        NumberAnimation {
            duration: 50
            easing.type: Easing.Linear
        }
    }

    Connections {
        target: videoController
        function onCurrentFrameChanged(currentFrame) {
            timeSlider.x = currentFrame * studioWindow.pixelsPerFrame
        }
    }
}
