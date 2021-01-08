<!DOCTYPE html>
<!-- saved from url=(0025)http://localhost:8890/lab -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  
  <title>JupyterLab</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  





  <script id="jupyter-config-data" type="application/json">
    {"appName": "JupyterLab", "appNamespace": "jupyterlab", "appSettingsDir": "C:/Users/Khaled/anaconda3/share/jupyter/lab/settings", "appUrl": "/lab", "appVersion": "2.2.6", "baseUrl": "/", "buildAvailable": true, "buildCheck": true, "cacheFiles": true, "devMode": false, "exposeAppInBrowser": false, "fullAppUrl": "/lab", "fullListingsUrl": "/lab/api/listings", "fullMathjaxUrl": "/static/components/MathJax/MathJax.js", "fullSettingsUrl": "/lab/api/settings", "fullStaticUrl": "/static/lab", "fullThemesUrl": "/lab/api/themes", "fullTreeUrl": "/lab/tree", "fullWorkspacesApiUrl": "/lab/api/workspaces", "fullWorkspacesUrl": "/lab/workspaces", "ignorePlugins": [], "listingsUrl": "/lab/api/listings", "mathjaxConfig": "TeX-AMS-MML_HTMLorMML-full,Safe", "notebookVersion": "[6, 1, 4]", "quitButton": true, "schemasDir": "C:/Users/Khaled/anaconda3/share/jupyter/lab/schemas", "serverRoot": "C:/Users/Khaled", "settingsUrl": "/lab/api/settings", "staticDir": "C:/Users/Khaled/anaconda3/share/jupyter/lab/static", "staticUrl": "/static/lab", "store_id": 0, "templatesDir": "C:/Users/Khaled/anaconda3/share/jupyter/lab/static", "terminalsAvailable": true, "themesDir": "C:/Users/Khaled/anaconda3/share/jupyter/lab/themes", "themesUrl": "/lab/api/themes", "token": "086743b84fe72d13ef60345c4582b408e525542a0d612ec7", "treeUrl": "/lab/tree", "userSettingsDir": "C:/Users/Khaled/.jupyter/lab/user-settings", "workspacesApiUrl": "/lab/api/workspaces", "workspacesDir": "C:/Users/Khaled/.jupyter/lab/workspaces", "workspacesUrl": "/lab/workspaces", "wsUrl": ""}
  </script>

  
  <link rel="icon" type="image/x-icon" href="http://localhost:8890/static/base/images/favicon.ico" class="idle favicon">
  <link rel="" type="image/x-icon" href="http://localhost:8890/static/base/images/favicon-busy-1.ico" class="busy favicon">
  

<style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Widget, /* </DEPRECATED> */
.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


/* <DEPRECATED> */ .p-Widget.p-mod-hidden, /* </DEPRECATED> */
.lm-Widget.lm-mod-hidden {
  display: none !important;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-CommandPalette, /* </DEPRECATED> */
.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-CommandPalette-search, /* </DEPRECATED> */
.lm-CommandPalette-search {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-content, /* </DEPRECATED> */
.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-CommandPalette-header, /* </DEPRECATED> */
.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


/* <DEPRECATED> */ .p-CommandPalette-item, /* </DEPRECATED> */
.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


/* <DEPRECATED> */ .p-CommandPalette-itemIcon, /* </DEPRECATED> */
.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemContent, /* </DEPRECATED> */
.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


/* <DEPRECATED> */ .p-CommandPalette-itemShortcut, /* </DEPRECATED> */
.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemLabel, /* </DEPRECATED> */
.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
	border:1px solid transparent;
  background-color: transparent;
  position: absolute;
	z-index:1;
	right:3%;
	top: 0;
	bottom: 0;
	margin: auto;
	padding: 7px 0;
	display: none;
	vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
	content: "X";
	display: block;
	width: 15px;
	height: 15px;
	text-align: center;
	color:#000;
	font-weight: normal;
	font-size: 12px;
	cursor: pointer;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-DockPanel, /* </DEPRECATED> */
.lm-DockPanel {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-widget, /* </DEPRECATED> */
.lm-DockPanel-widget {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-tabBar, /* </DEPRECATED> */
.lm-DockPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-DockPanel-handle, /* </DEPRECATED> */
.lm-DockPanel-handle {
  z-index: 2;
}


/* <DEPRECATED> */ .p-DockPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-DockPanel-handle:after, /* </DEPRECATED> */
.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


/* <DEPRECATED> */ .p-DockPanel-overlay, /* </DEPRECATED> */
.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


/* <DEPRECATED> */ .p-DockPanel-overlay.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Menu, /* </DEPRECATED> */
.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-Menu-content, /* </DEPRECATED> */
.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-Menu-item, /* </DEPRECATED> */
.lm-Menu-item {
  display: table-row;
}


/* <DEPRECATED> */
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed,
/* </DEPRECATED> */
.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}


/* <DEPRECATED> */
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon,
/* </DEPRECATED> */
.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


/* <DEPRECATED> */ .p-Menu-itemLabel, /* </DEPRECATED> */
.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


/* <DEPRECATED> */ .p-Menu-itemShortcut, /* </DEPRECATED> */
.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-MenuBar, /* </DEPRECATED> */
.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-MenuBar-content, /* </DEPRECATED> */
.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


/* <DEPRECATED> */ .p--MenuBar-item, /* </DEPRECATED> */
.lm-MenuBar-item {
  box-sizing: border-box;
}


/* <DEPRECATED> */
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel,
/* </DEPRECATED> */
.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-ScrollBar, /* </DEPRECATED> */
.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-ScrollBar-button, /* </DEPRECATED> */
.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-track, /* </DEPRECATED> */
.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-thumb, /* </DEPRECATED> */
.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-SplitPanel-child, /* </DEPRECATED> */
.lm-SplitPanel-child {
  z-index: 0;
}


/* <DEPRECATED> */ .p-SplitPanel-handle, /* </DEPRECATED> */
.lm-SplitPanel-handle {
  z-index: 1;
}


/* <DEPRECATED> */ .p-SplitPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-SplitPanel-handle:after, /* </DEPRECATED> */
.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabBar, /* </DEPRECATED> */
.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-content, /* </DEPRECATED> */
.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


/* <DEPRECATED> */
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-TabBar-tabLabel, /* </DEPRECATED> */
.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
}


/* <DEPRECATED> */ .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabPanel-tabBar, /* </DEPRECATED> */
.lm-TabPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-TabPanel-stackedPanel, /* </DEPRECATED> */
.lm-TabPanel-stackedPanel {
  z-index: 0;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
</style><style>@charset "UTF-8";
html{
  -webkit-box-sizing:border-box;
          box-sizing:border-box; }

*,
*::before,
*::after{
  -webkit-box-sizing:inherit;
          box-sizing:inherit; }

body{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none;
  color:#182026;
  font-family:-apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", "Icons16", sans-serif; }

p{
  margin-bottom:10px;
  margin-top:0; }

small{
  font-size:12px; }

strong{
  font-weight:600; }

::-moz-selection{
  background:rgba(125, 188, 255, 0.6); }

::selection{
  background:rgba(125, 188, 255, 0.6); }
.bp3-heading{
  color:#182026;
  font-weight:600;
  margin:0 0 10px;
  padding:0; }
  .bp3-dark .bp3-heading{
    color:#f5f8fa; }

h1.bp3-heading, .bp3-running-text h1{
  font-size:36px;
  line-height:40px; }

h2.bp3-heading, .bp3-running-text h2{
  font-size:28px;
  line-height:32px; }

h3.bp3-heading, .bp3-running-text h3{
  font-size:22px;
  line-height:25px; }

h4.bp3-heading, .bp3-running-text h4{
  font-size:18px;
  line-height:21px; }

h5.bp3-heading, .bp3-running-text h5{
  font-size:16px;
  line-height:19px; }

h6.bp3-heading, .bp3-running-text h6{
  font-size:14px;
  line-height:16px; }
.bp3-ui-text{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none; }

.bp3-monospace-text{
  font-family:monospace;
  text-transform:none; }

.bp3-text-muted{
  color:#5c7080; }
  .bp3-dark .bp3-text-muted{
    color:#a7b6c2; }

.bp3-text-disabled{
  color:rgba(92, 112, 128, 0.6); }
  .bp3-dark .bp3-text-disabled{
    color:rgba(167, 182, 194, 0.6); }

.bp3-text-overflow-ellipsis{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal; }
.bp3-running-text{
  font-size:14px;
  line-height:1.5; }
  .bp3-running-text h1{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h1{
      color:#f5f8fa; }
  .bp3-running-text h2{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h2{
      color:#f5f8fa; }
  .bp3-running-text h3{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h3{
      color:#f5f8fa; }
  .bp3-running-text h4{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h4{
      color:#f5f8fa; }
  .bp3-running-text h5{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h5{
      color:#f5f8fa; }
  .bp3-running-text h6{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h6{
      color:#f5f8fa; }
  .bp3-running-text hr{
    border:none;
    border-bottom:1px solid rgba(16, 22, 26, 0.15);
    margin:20px 0; }
    .bp3-dark .bp3-running-text hr{
      border-color:rgba(255, 255, 255, 0.15); }
  .bp3-running-text p{
    margin:0 0 10px;
    padding:0; }

.bp3-text-large{
  font-size:16px; }

.bp3-text-small{
  font-size:12px; }
a{
  color:#106ba3;
  text-decoration:none; }
  a:hover{
    color:#106ba3;
    cursor:pointer;
    text-decoration:underline; }
  a .bp3-icon, a .bp3-icon-standard, a .bp3-icon-large{
    color:inherit; }
  a code,
  .bp3-dark a code{
    color:inherit; }
  .bp3-dark a,
  .bp3-dark a:hover{
    color:#48aff0; }
    .bp3-dark a .bp3-icon, .bp3-dark a .bp3-icon-standard, .bp3-dark a .bp3-icon-large,
    .bp3-dark a:hover .bp3-icon,
    .bp3-dark a:hover .bp3-icon-standard,
    .bp3-dark a:hover .bp3-icon-large{
      color:inherit; }
.bp3-running-text code, .bp3-code{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  font-size:smaller;
  padding:2px 5px; }
  .bp3-dark .bp3-running-text code, .bp3-running-text .bp3-dark code, .bp3-dark .bp3-code{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
  .bp3-running-text a > code, a > .bp3-code{
    color:#137cbd; }
    .bp3-dark .bp3-running-text a > code, .bp3-running-text .bp3-dark a > code, .bp3-dark a > .bp3-code{
      color:inherit; }

.bp3-running-text pre, .bp3-code-block{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
  color:#182026;
  display:block;
  font-size:13px;
  line-height:1.4;
  margin:10px 0;
  padding:13px 15px 12px;
  word-break:break-all;
  word-wrap:break-word; }
  .bp3-dark .bp3-running-text pre, .bp3-running-text .bp3-dark pre, .bp3-dark .bp3-code-block{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
  .bp3-running-text pre > code, .bp3-code-block > code{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit;
    font-size:inherit;
    padding:0; }

.bp3-running-text kbd, .bp3-key{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-family:inherit;
  font-size:12px;
  height:24px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  line-height:24px;
  min-width:24px;
  padding:3px 6px;
  vertical-align:middle; }
  .bp3-running-text kbd .bp3-icon, .bp3-key .bp3-icon, .bp3-running-text kbd .bp3-icon-standard, .bp3-key .bp3-icon-standard, .bp3-running-text kbd .bp3-icon-large, .bp3-key .bp3-icon-large{
    margin-right:5px; }
  .bp3-dark .bp3-running-text kbd, .bp3-running-text .bp3-dark kbd, .bp3-dark .bp3-key{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
.bp3-running-text blockquote, .bp3-blockquote{
  border-left:solid 4px rgba(167, 182, 194, 0.5);
  margin:0 0 10px;
  padding:0 20px; }
  .bp3-dark .bp3-running-text blockquote, .bp3-running-text .bp3-dark blockquote, .bp3-dark .bp3-blockquote{
    border-color:rgba(115, 134, 148, 0.5); }
.bp3-running-text ul,
.bp3-running-text ol, .bp3-list{
  margin:10px 0;
  padding-left:30px; }
  .bp3-running-text ul li:not(:last-child), .bp3-running-text ol li:not(:last-child), .bp3-list li:not(:last-child){
    margin-bottom:5px; }
  .bp3-running-text ul ol, .bp3-running-text ol ol, .bp3-list ol,
  .bp3-running-text ul ul,
  .bp3-running-text ol ul,
  .bp3-list ul{
    margin-top:5px; }

.bp3-list-unstyled{
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-list-unstyled li{
    padding:0; }
.bp3-rtl{
  text-align:right; }

.bp3-dark{
  color:#f5f8fa; }

:focus{
  outline:rgba(19, 124, 189, 0.6) auto 2px;
  outline-offset:2px;
  -moz-outline-radius:6px; }

.bp3-focus-disabled :focus{
  outline:none !important; }
  .bp3-focus-disabled :focus ~ .bp3-control-indicator{
    outline:none !important; }

.bp3-alert{
  max-width:400px;
  padding:20px; }

.bp3-alert-body{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-alert-body .bp3-icon{
    font-size:40px;
    margin-right:20px;
    margin-top:0; }

.bp3-alert-contents{
  word-break:break-word; }

.bp3-alert-footer{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:reverse;
      -ms-flex-direction:row-reverse;
          flex-direction:row-reverse;
  margin-top:10px; }
  .bp3-alert-footer .bp3-button{
    margin-left:10px; }
.bp3-breadcrumbs{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  cursor:default;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:wrap;
      flex-wrap:wrap;
  height:30px;
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-breadcrumbs > li{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }
    .bp3-breadcrumbs > li::after{
      background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.71 7.29l-4-4a1.003 1.003 0 00-1.42 1.42L8.59 8 5.3 11.29c-.19.18-.3.43-.3.71a1.003 1.003 0 001.71.71l4-4c.18-.18.29-.43.29-.71 0-.28-.11-.53-.29-.71z' fill='%235C7080'/%3e%3c/svg%3e");
      content:"";
      display:block;
      height:16px;
      margin:0 5px;
      width:16px; }
    .bp3-breadcrumbs > li:last-of-type::after{
      display:none; }

.bp3-breadcrumb,
.bp3-breadcrumb-current,
.bp3-breadcrumbs-collapsed{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-size:16px; }

.bp3-breadcrumb,
.bp3-breadcrumbs-collapsed{
  color:#5c7080; }

.bp3-breadcrumb:hover{
  text-decoration:none; }

.bp3-breadcrumb.bp3-disabled{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-breadcrumb .bp3-icon{
  margin-right:5px; }

.bp3-breadcrumb-current{
  color:inherit;
  font-weight:600; }
  .bp3-breadcrumb-current .bp3-input{
    font-size:inherit;
    font-weight:inherit;
    vertical-align:baseline; }

.bp3-breadcrumbs-collapsed{
  background:#ced9e0;
  border:none;
  border-radius:3px;
  cursor:pointer;
  margin-right:2px;
  padding:1px 5px;
  vertical-align:text-bottom; }
  .bp3-breadcrumbs-collapsed::before{
    background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cg fill='%235C7080'%3e%3ccircle cx='2' cy='8.03' r='2'/%3e%3ccircle cx='14' cy='8.03' r='2'/%3e%3ccircle cx='8' cy='8.03' r='2'/%3e%3c/g%3e%3c/svg%3e") center no-repeat;
    content:"";
    display:block;
    height:16px;
    width:16px; }
  .bp3-breadcrumbs-collapsed:hover{
    background:#bfccd6;
    color:#182026;
    text-decoration:none; }

.bp3-dark .bp3-breadcrumb,
.bp3-dark .bp3-breadcrumbs-collapsed{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumbs > li::after{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumb.bp3-disabled{
  color:rgba(167, 182, 194, 0.6); }

.bp3-dark .bp3-breadcrumb-current{
  color:#f5f8fa; }

.bp3-dark .bp3-breadcrumbs-collapsed{
  background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-breadcrumbs-collapsed:hover{
    background:rgba(16, 22, 26, 0.6);
    color:#f5f8fa; }
.bp3-button{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  min-height:30px;
  min-width:30px; }
  .bp3-button > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-button > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-button::before,
  .bp3-button > *{
    margin-right:7px; }
  .bp3-button:empty::before,
  .bp3-button > :last-child{
    margin-right:0; }
  .bp3-button:empty{
    padding:0 !important; }
  .bp3-button:disabled, .bp3-button.bp3-disabled{
    cursor:not-allowed; }
  .bp3-button.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button.bp3-align-right,
  .bp3-align-right .bp3-button{
    text-align:right; }
  .bp3-button.bp3-align-left,
  .bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-button:not([class*="bp3-intent-"]){
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026; }
    .bp3-button:not([class*="bp3-intent-"]):hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-button:not([class*="bp3-intent-"]):active, .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active:hover, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-button.bp3-intent-primary{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover, .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover{
      background-color:#106ba3;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      background-color:#0e5a8a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:disabled, .bp3-button.bp3-intent-primary.bp3-disabled{
      background-color:rgba(19, 124, 189, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-success{
    background-color:#0f9960;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-success:hover, .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-success:hover{
      background-color:#0d8050;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      background-color:#0a6640;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:disabled, .bp3-button.bp3-intent-success.bp3-disabled{
      background-color:rgba(15, 153, 96, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-warning{
    background-color:#d9822b;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover, .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover{
      background-color:#bf7326;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      background-color:#a66321;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:disabled, .bp3-button.bp3-intent-warning.bp3-disabled{
      background-color:rgba(217, 130, 43, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-danger{
    background-color:#db3737;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover, .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover{
      background-color:#c23030;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      background-color:#a82a2a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:disabled, .bp3-button.bp3-intent-danger.bp3-disabled{
      background-color:rgba(219, 55, 55, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
    stroke:#ffffff; }
  .bp3-button.bp3-large,
  .bp3-large .bp3-button{
    min-height:40px;
    min-width:40px;
    font-size:16px;
    padding:5px 15px; }
    .bp3-button.bp3-large::before,
    .bp3-button.bp3-large > *,
    .bp3-large .bp3-button::before,
    .bp3-large .bp3-button > *{
      margin-right:10px; }
    .bp3-button.bp3-large:empty::before,
    .bp3-button.bp3-large > :last-child,
    .bp3-large .bp3-button:empty::before,
    .bp3-large .bp3-button > :last-child{
      margin-right:0; }
  .bp3-button.bp3-small,
  .bp3-small .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-button.bp3-loading{
    position:relative; }
    .bp3-button.bp3-loading[class*="bp3-icon-"]::before{
      visibility:hidden; }
    .bp3-button.bp3-loading .bp3-button-spinner{
      margin:0;
      position:absolute; }
    .bp3-button.bp3-loading > :not(.bp3-button-spinner){
      visibility:hidden; }
  .bp3-button[class*="bp3-icon-"]::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    color:#5c7080; }
  .bp3-button .bp3-icon, .bp3-button .bp3-icon-standard, .bp3-button .bp3-icon-large{
    color:#5c7080; }
    .bp3-button .bp3-icon.bp3-align-right, .bp3-button .bp3-icon-standard.bp3-align-right, .bp3-button .bp3-icon-large.bp3-align-right{
      margin-left:7px; }
  .bp3-button .bp3-icon:first-child:last-child,
  .bp3-button .bp3-spinner + .bp3-icon:last-child{
    margin:0 -7px; }
  .bp3-dark .bp3-button:not([class*="bp3-intent-"]){
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover, .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"])[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-large{
      color:#a7b6c2; }
  .bp3-dark .bp3-button[class*="bp3-intent-"]{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:active, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:disabled, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-disabled{
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.3); }
    .bp3-dark .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
      stroke:#8a9ba8; }
  .bp3-button:disabled::before,
  .bp3-button:disabled .bp3-icon, .bp3-button:disabled .bp3-icon-standard, .bp3-button:disabled .bp3-icon-large, .bp3-button.bp3-disabled::before,
  .bp3-button.bp3-disabled .bp3-icon, .bp3-button.bp3-disabled .bp3-icon-standard, .bp3-button.bp3-disabled .bp3-icon-large, .bp3-button[class*="bp3-intent-"]::before,
  .bp3-button[class*="bp3-intent-"] .bp3-icon, .bp3-button[class*="bp3-intent-"] .bp3-icon-standard, .bp3-button[class*="bp3-intent-"] .bp3-icon-large{
    color:inherit !important; }
  .bp3-button.bp3-minimal{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button.bp3-minimal:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-minimal:active, .bp3-button.bp3-minimal.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-minimal:disabled, .bp3-button.bp3-minimal:disabled:hover, .bp3-button.bp3-minimal.bp3-disabled, .bp3-button.bp3-minimal.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-minimal{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-minimal:hover, .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-minimal:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-minimal:disabled, .bp3-dark .bp3-button.bp3-minimal:disabled:hover, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover, .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover, .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover, .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover, .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button.bp3-outlined{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    border:1px solid rgba(24, 32, 38, 0.2);
    -webkit-box-sizing:border-box;
            box-sizing:border-box; }
    .bp3-button.bp3-outlined:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-outlined:active, .bp3-button.bp3-outlined.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-outlined{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-outlined:hover, .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-outlined:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover, .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover, .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover, .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover, .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled:hover{
      border-color:rgba(92, 112, 128, 0.1); }
    .bp3-dark .bp3-button.bp3-outlined{
      border-color:rgba(255, 255, 255, 0.4); }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        border-color:rgba(255, 255, 255, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      border-color:rgba(16, 107, 163, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        border-color:rgba(16, 107, 163, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        border-color:rgba(72, 175, 240, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          border-color:rgba(72, 175, 240, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      border-color:rgba(13, 128, 80, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        border-color:rgba(13, 128, 80, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        border-color:rgba(61, 204, 145, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          border-color:rgba(61, 204, 145, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      border-color:rgba(191, 115, 38, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        border-color:rgba(191, 115, 38, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        border-color:rgba(255, 179, 102, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          border-color:rgba(255, 179, 102, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      border-color:rgba(194, 48, 48, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        border-color:rgba(194, 48, 48, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        border-color:rgba(255, 115, 115, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          border-color:rgba(255, 115, 115, 0.2); }

a.bp3-button{
  text-align:center;
  text-decoration:none;
  -webkit-transition:none;
  transition:none; }
  a.bp3-button, a.bp3-button:hover, a.bp3-button:active{
    color:#182026; }
  a.bp3-button.bp3-disabled{
    color:rgba(92, 112, 128, 0.6); }

.bp3-button-text{
  -webkit-box-flex:0;
      -ms-flex:0 1 auto;
          flex:0 1 auto; }

.bp3-button.bp3-align-left .bp3-button-text, .bp3-button.bp3-align-right .bp3-button-text,
.bp3-button-group.bp3-align-left .bp3-button-text,
.bp3-button-group.bp3-align-right .bp3-button-text{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto; }
.bp3-button-group{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex; }
  .bp3-button-group .bp3-button{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    position:relative;
    z-index:4; }
    .bp3-button-group .bp3-button:focus{
      z-index:5; }
    .bp3-button-group .bp3-button:hover{
      z-index:6; }
    .bp3-button-group .bp3-button:active, .bp3-button-group .bp3-button.bp3-active{
      z-index:7; }
    .bp3-button-group .bp3-button:disabled, .bp3-button-group .bp3-button.bp3-disabled{
      z-index:3; }
    .bp3-button-group .bp3-button[class*="bp3-intent-"]{
      z-index:9; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:focus{
        z-index:10; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:hover{
        z-index:11; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:active, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-active{
        z-index:12; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:disabled, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-disabled{
        z-index:8; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:first-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:first-child){
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    border-bottom-right-radius:0;
    border-top-right-radius:0;
    margin-right:-1px; }
  .bp3-button-group.bp3-minimal .bp3-button{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button-group.bp3-minimal .bp3-button:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button-group.bp3-minimal .bp3-button{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
      color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
      color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button-group .bp3-popover-wrapper,
  .bp3-button-group .bp3-popover-target{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button-group .bp3-button.bp3-fill,
  .bp3-button-group.bp3-fill .bp3-button:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-vertical{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column;
    vertical-align:top; }
    .bp3-button-group.bp3-vertical.bp3-fill{
      height:100%;
      width:unset; }
    .bp3-button-group.bp3-vertical .bp3-button{
      margin-right:0 !important;
      width:100%; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:first-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:first-child{
      border-radius:3px 3px 0 0; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:last-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:last-child{
      border-radius:0 0 3px 3px; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:not(:last-child){
      margin-bottom:-1px; }
  .bp3-button-group.bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    margin-right:1px; }
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-button:not(:last-child){
    margin-bottom:1px; }
.bp3-callout{
  font-size:14px;
  line-height:1.5;
  background-color:rgba(138, 155, 168, 0.15);
  border-radius:3px;
  padding:10px 12px 9px;
  position:relative;
  width:100%; }
  .bp3-callout[class*="bp3-icon-"]{
    padding-left:40px; }
    .bp3-callout[class*="bp3-icon-"]::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout.bp3-callout-icon{
    padding-left:40px; }
    .bp3-callout.bp3-callout-icon > .bp3-icon:first-child{
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout .bp3-heading{
    line-height:20px;
    margin-bottom:5px;
    margin-top:0; }
    .bp3-callout .bp3-heading:last-child{
      margin-bottom:0; }
  .bp3-dark .bp3-callout{
    background-color:rgba(138, 155, 168, 0.2); }
    .bp3-dark .bp3-callout[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
  .bp3-callout.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15); }
    .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-primary .bp3-heading{
      color:#106ba3; }
    .bp3-dark .bp3-callout.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-primary .bp3-heading{
        color:#48aff0; }
  .bp3-callout.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15); }
    .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-success .bp3-heading{
      color:#0d8050; }
    .bp3-dark .bp3-callout.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-success .bp3-heading{
        color:#3dcc91; }
  .bp3-callout.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15); }
    .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-warning .bp3-heading{
      color:#bf7326; }
    .bp3-dark .bp3-callout.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-warning .bp3-heading{
        color:#ffb366; }
  .bp3-callout.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15); }
    .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-danger .bp3-heading{
      color:#c23030; }
    .bp3-dark .bp3-callout.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-danger .bp3-heading{
        color:#ff7373; }
  .bp3-running-text .bp3-callout{
    margin:20px 0; }
.bp3-card{
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
  padding:20px;
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-card.bp3-dark,
  .bp3-dark .bp3-card{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-0{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }
  .bp3-elevation-0.bp3-dark,
  .bp3-dark .bp3-elevation-0{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-1{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-1.bp3-dark,
  .bp3-dark .bp3-elevation-1{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-elevation-2{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-2.bp3-dark,
  .bp3-dark .bp3-elevation-2{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4); }

.bp3-elevation-3{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-3.bp3-dark,
  .bp3-dark .bp3-elevation-3{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-elevation-4{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-4.bp3-dark,
  .bp3-dark .bp3-elevation-4{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:hover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  cursor:pointer; }
  .bp3-card.bp3-interactive:hover.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:hover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:active{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  opacity:0.9;
  -webkit-transition-duration:0;
          transition-duration:0; }
  .bp3-card.bp3-interactive:active.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:active{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-collapse{
  height:0;
  overflow-y:hidden;
  -webkit-transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-collapse .bp3-collapse-body{
    -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-collapse .bp3-collapse-body[aria-hidden="true"]{
      display:none; }

.bp3-context-menu .bp3-popover-target{
  display:block; }

.bp3-context-menu-popover-target{
  position:fixed; }

.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-dialog-container{
  opacity:1;
  -webkit-transform:scale(1);
          transform:scale(1);
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  min-height:100%;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  width:100%; }
  .bp3-dialog-container.bp3-overlay-enter > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5); }
  .bp3-dialog-container.bp3-overlay-enter-active > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear-active > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-dialog-container.bp3-overlay-exit > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-dialog-container.bp3-overlay-exit-active > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }

.bp3-dialog{
  background:#ebf1f5;
  border-radius:6px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:30px 0;
  padding-bottom:20px;
  pointer-events:all;
  -webkit-user-select:text;
     -moz-user-select:text;
      -ms-user-select:text;
          user-select:text;
  width:500px; }
  .bp3-dialog:focus{
    outline:0; }
  .bp3-dialog.bp3-dark,
  .bp3-dark .bp3-dialog{
    background:#293742;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-dialog-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:6px 6px 0 0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding-left:20px;
  padding-right:5px; }
  .bp3-dialog-header .bp3-icon-large,
  .bp3-dialog-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-dialog-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-dialog-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-dialog-header{
    background:#30404d;
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-dialog-header .bp3-icon-large,
    .bp3-dark .bp3-dialog-header .bp3-icon{
      color:#a7b6c2; }

.bp3-dialog-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  margin:20px; }

.bp3-dialog-footer{
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  margin:0 20px; }

.bp3-dialog-footer-actions{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:end;
      -ms-flex-pack:end;
          justify-content:flex-end; }
  .bp3-dialog-footer-actions .bp3-button{
    margin-left:10px; }
.bp3-drawer{
  background:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0;
  padding:0; }
  .bp3-drawer:focus{
    outline:0; }
  .bp3-drawer.bp3-position-top{
    height:50%;
    left:0;
    right:0;
    top:0; }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter, .bp3-drawer.bp3-position-top.bp3-overlay-appear{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%); }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter-active, .bp3-drawer.bp3-position-top.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit-active{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-bottom{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter-active, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-left{
    bottom:0;
    left:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter, .bp3-drawer.bp3-position-left.bp3-overlay-appear{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%); }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter-active, .bp3-drawer.bp3-position-left.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit-active{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-right{
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter, .bp3-drawer.bp3-position-right.bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter-active, .bp3-drawer.bp3-position-right.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right):not(.bp3-vertical){
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right).bp3-vertical{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-dark,
  .bp3-dark .bp3-drawer{
    background:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-drawer-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border-radius:0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding:5px;
  padding-left:20px;
  position:relative; }
  .bp3-drawer-header .bp3-icon-large,
  .bp3-drawer-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-drawer-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-drawer-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-drawer-header{
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-drawer-header .bp3-icon-large,
    .bp3-dark .bp3-drawer-header .bp3-icon{
      color:#a7b6c2; }

.bp3-drawer-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  overflow:auto; }

.bp3-drawer-footer{
  -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  padding:10px 20px;
  position:relative; }
  .bp3-dark .bp3-drawer-footer{
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4); }
.bp3-editable-text{
  cursor:text;
  display:inline-block;
  max-width:100%;
  position:relative;
  vertical-align:top;
  white-space:nowrap; }
  .bp3-editable-text::before{
    bottom:-3px;
    left:-3px;
    position:absolute;
    right:-3px;
    top:-3px;
    border-radius:3px;
    content:"";
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#137cbd; }
  .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4); }
  .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#0f9960; }
  .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4); }
  .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#d9822b; }
  .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4); }
  .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#db3737; }
  .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4); }
  .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15); }
  .bp3-dark .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#48aff0; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4);
            box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#3dcc91; }
  .bp3-dark .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4);
            box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#ffb366; }
  .bp3-dark .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4);
            box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#ff7373; }
  .bp3-dark .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4);
            box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-editable-text-input,
.bp3-editable-text-content{
  color:inherit;
  display:inherit;
  font:inherit;
  letter-spacing:inherit;
  max-width:inherit;
  min-width:inherit;
  position:relative;
  resize:none;
  text-transform:inherit;
  vertical-align:top; }

.bp3-editable-text-input{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0;
  white-space:pre-wrap;
  width:100%; }
  .bp3-editable-text-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:focus{
    outline:none; }
  .bp3-editable-text-input::-ms-clear{
    display:none; }

.bp3-editable-text-content{
  overflow:hidden;
  padding-right:2px;
  text-overflow:ellipsis;
  white-space:pre; }
  .bp3-editable-text-editing > .bp3-editable-text-content{
    left:0;
    position:absolute;
    visibility:hidden; }
  .bp3-editable-text-placeholder > .bp3-editable-text-content{
    color:rgba(92, 112, 128, 0.6); }
    .bp3-dark .bp3-editable-text-placeholder > .bp3-editable-text-content{
      color:rgba(167, 182, 194, 0.6); }

.bp3-editable-text.bp3-multiline{
  display:block; }
  .bp3-editable-text.bp3-multiline .bp3-editable-text-content{
    overflow:auto;
    white-space:pre-wrap;
    word-wrap:break-word; }
.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-control-group{
  -webkit-transform:translateZ(0);
          transform:translateZ(0);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:stretch;
      -ms-flex-align:stretch;
          align-items:stretch; }
  .bp3-control-group > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select,
  .bp3-control-group .bp3-input,
  .bp3-control-group .bp3-select{
    position:relative; }
  .bp3-control-group .bp3-input{
    border-radius:inherit;
    z-index:2; }
    .bp3-control-group .bp3-input:focus{
      border-radius:3px;
      z-index:14; }
    .bp3-control-group .bp3-input[class*="bp3-intent"]{
      z-index:13; }
      .bp3-control-group .bp3-input[class*="bp3-intent"]:focus{
        z-index:15; }
    .bp3-control-group .bp3-input[readonly], .bp3-control-group .bp3-input:disabled, .bp3-control-group .bp3-input.bp3-disabled{
      z-index:1; }
  .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input{
    z-index:13; }
    .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input:focus{
      z-index:15; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select select,
  .bp3-control-group .bp3-select select{
    -webkit-transform:translateZ(0);
            transform:translateZ(0);
    border-radius:inherit;
    z-index:4; }
    .bp3-control-group .bp3-button:focus,
    .bp3-control-group .bp3-html-select select:focus,
    .bp3-control-group .bp3-select select:focus{
      z-index:5; }
    .bp3-control-group .bp3-button:hover,
    .bp3-control-group .bp3-html-select select:hover,
    .bp3-control-group .bp3-select select:hover{
      z-index:6; }
    .bp3-control-group .bp3-button:active,
    .bp3-control-group .bp3-html-select select:active,
    .bp3-control-group .bp3-select select:active{
      z-index:7; }
    .bp3-control-group .bp3-button[readonly], .bp3-control-group .bp3-button:disabled, .bp3-control-group .bp3-button.bp3-disabled,
    .bp3-control-group .bp3-html-select select[readonly],
    .bp3-control-group .bp3-html-select select:disabled,
    .bp3-control-group .bp3-html-select select.bp3-disabled,
    .bp3-control-group .bp3-select select[readonly],
    .bp3-control-group .bp3-select select:disabled,
    .bp3-control-group .bp3-select select.bp3-disabled{
      z-index:3; }
    .bp3-control-group .bp3-button[class*="bp3-intent"],
    .bp3-control-group .bp3-html-select select[class*="bp3-intent"],
    .bp3-control-group .bp3-select select[class*="bp3-intent"]{
      z-index:9; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:focus{
        z-index:10; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:hover{
        z-index:11; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:active{
        z-index:12; }
      .bp3-control-group .bp3-button[class*="bp3-intent"][readonly], .bp3-control-group .bp3-button[class*="bp3-intent"]:disabled, .bp3-control-group .bp3-button[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"].bp3-disabled{
        z-index:8; }
  .bp3-control-group .bp3-input-group > .bp3-icon,
  .bp3-control-group .bp3-input-group > .bp3-button,
  .bp3-control-group .bp3-input-group > .bp3-input-action{
    z-index:16; }
  .bp3-control-group .bp3-select::after,
  .bp3-control-group .bp3-html-select::after,
  .bp3-control-group .bp3-select > .bp3-icon,
  .bp3-control-group .bp3-html-select > .bp3-icon{
    z-index:17; }
  .bp3-control-group .bp3-select:focus-within{
    z-index:5; }
  .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:-1px; }
  .bp3-control-group:not(.bp3-vertical) > .bp3-divider:not(:first-child){
    margin-left:6px; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:0; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > .bp3-button + .bp3-button{
    margin-left:1px; }
  .bp3-control-group .bp3-popover-wrapper,
  .bp3-control-group .bp3-popover-target{
    border-radius:inherit; }
  .bp3-control-group > :first-child{
    border-radius:3px 0 0 3px; }
  .bp3-control-group > :last-child{
    border-radius:0 3px 3px 0;
    margin-right:0; }
  .bp3-control-group > :only-child{
    border-radius:3px;
    margin-right:0; }
  .bp3-control-group .bp3-input-group .bp3-button{
    border-radius:3px; }
  .bp3-control-group .bp3-numeric-input:not(:first-child) .bp3-input-group{
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-fill > *:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-vertical{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-control-group.bp3-vertical > *{
      margin-top:-1px; }
    .bp3-control-group.bp3-vertical > :first-child{
      border-radius:3px 3px 0 0;
      margin-top:0; }
    .bp3-control-group.bp3-vertical > :last-child{
      border-radius:0 0 3px 3px; }
.bp3-control{
  cursor:pointer;
  display:block;
  margin-bottom:10px;
  position:relative;
  text-transform:none; }
  .bp3-control input:checked ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control:not(.bp3-align-right){
    padding-left:26px; }
    .bp3-control:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-26px; }
  .bp3-control.bp3-align-right{
    padding-right:26px; }
    .bp3-control.bp3-align-right .bp3-control-indicator{
      margin-right:-26px; }
  .bp3-control.bp3-disabled{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-control.bp3-inline{
    display:inline-block;
    margin-right:20px; }
  .bp3-control input{
    left:0;
    opacity:0;
    position:absolute;
    top:0;
    z-index:-1; }
  .bp3-control .bp3-control-indicator{
    background-clip:padding-box;
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    border:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    cursor:pointer;
    display:inline-block;
    font-size:16px;
    height:1em;
    margin-right:10px;
    margin-top:-3px;
    position:relative;
    -webkit-user-select:none;
       -moz-user-select:none;
        -ms-user-select:none;
            user-select:none;
    vertical-align:middle;
    width:1em; }
    .bp3-control .bp3-control-indicator::before{
      content:"";
      display:block;
      height:1em;
      width:1em; }
  .bp3-control:hover .bp3-control-indicator{
    background-color:#ebf1f5; }
  .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
    background:#d8e1e8;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    cursor:not-allowed; }
  .bp3-control input:focus ~ .bp3-control-indicator{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:2px;
    -moz-outline-radius:6px; }
  .bp3-control.bp3-align-right .bp3-control-indicator{
    float:right;
    margin-left:10px;
    margin-top:1px; }
  .bp3-control.bp3-large{
    font-size:16px; }
    .bp3-control.bp3-large:not(.bp3-align-right){
      padding-left:30px; }
      .bp3-control.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
        margin-left:-30px; }
    .bp3-control.bp3-large.bp3-align-right{
      padding-right:30px; }
      .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
        margin-right:-30px; }
    .bp3-control.bp3-large .bp3-control-indicator{
      font-size:20px; }
    .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-top:0; }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control.bp3-checkbox .bp3-control-indicator{
    border-radius:3px; }
  .bp3-control.bp3-checkbox input:checked ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M12 5c-.28 0-.53.11-.71.29L7 9.59l-2.29-2.3a1.003 1.003 0 00-1.42 1.42l3 3c.18.18.43.29.71.29s.53-.11.71-.29l5-5A1.003 1.003 0 0012 5z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M11 7H5c-.55 0-1 .45-1 1s.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-radio .bp3-control-indicator{
    border-radius:50%; }
  .bp3-control.bp3-radio input:checked ~ .bp3-control-indicator::before{
    background-image:radial-gradient(#ffffff, #ffffff 28%, transparent 32%); }
  .bp3-control.bp3-radio input:checked:disabled ~ .bp3-control-indicator::before{
    opacity:0.5; }
  .bp3-control.bp3-radio input:focus ~ .bp3-control-indicator{
    -moz-outline-radius:16px; }
  .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(167, 182, 194, 0.5); }
  .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(115, 134, 148, 0.5); }
  .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(92, 112, 128, 0.5); }
  .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5); }
    .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5); }
    .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch:not(.bp3-align-right){
    padding-left:38px; }
    .bp3-control.bp3-switch:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-38px; }
  .bp3-control.bp3-switch.bp3-align-right{
    padding-right:38px; }
    .bp3-control.bp3-switch.bp3-align-right .bp3-control-indicator{
      margin-right:-38px; }
  .bp3-control.bp3-switch .bp3-control-indicator{
    border:none;
    border-radius:1.75em;
    -webkit-box-shadow:none !important;
            box-shadow:none !important;
    min-width:1.75em;
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:auto; }
    .bp3-control.bp3-switch .bp3-control-indicator::before{
      background:#ffffff;
      border-radius:50%;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
      height:calc(1em - 4px);
      left:0;
      margin:2px;
      position:absolute;
      -webkit-transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      width:calc(1em - 4px); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    left:calc(100% - 1em); }
  .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right){
    padding-left:45px; }
    .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-45px; }
  .bp3-control.bp3-switch.bp3-large.bp3-align-right{
    padding-right:45px; }
    .bp3-control.bp3-switch.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-right:-45px; }
  .bp3-dark .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.7); }
  .bp3-dark .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.9); }
  .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(57, 75, 89, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-dark .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-dark .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch .bp3-control-indicator::before{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-control.bp3-switch .bp3-switch-inner-text{
    font-size:0.7em;
    text-align:center; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:first-child{
    line-height:0;
    margin-left:0.5em;
    margin-right:1.2em;
    visibility:hidden; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:last-child{
    line-height:1em;
    margin-left:1.2em;
    margin-right:0.5em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:first-child{
    line-height:1em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:last-child{
    line-height:0;
    visibility:hidden; }
  .bp3-dark .bp3-control{
    color:#f5f8fa; }
    .bp3-dark .bp3-control.bp3-disabled{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-control .bp3-control-indicator{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-control:hover .bp3-control-indicator{
      background-color:#30404d; }
    .bp3-dark .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
      background:#202b33;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-control input:disabled ~ .bp3-control-indicator{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      cursor:not-allowed; }
    .bp3-dark .bp3-control.bp3-checkbox input:disabled:checked ~ .bp3-control-indicator, .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
      color:rgba(167, 182, 194, 0.6); }
.bp3-file-input{
  cursor:pointer;
  display:inline-block;
  height:30px;
  position:relative; }
  .bp3-file-input input{
    margin:0;
    min-width:200px;
    opacity:0; }
    .bp3-file-input input:disabled + .bp3-file-upload-input,
    .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
      background:rgba(206, 217, 224, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      resize:none; }
      .bp3-file-input input:disabled + .bp3-file-upload-input::after,
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
        background-color:rgba(206, 217, 224, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(92, 112, 128, 0.6);
        cursor:not-allowed;
        outline:none; }
        .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active:hover,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active:hover{
          background:rgba(206, 217, 224, 0.7); }
      .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input, .bp3-dark
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
        background:rgba(57, 75, 89, 0.5);
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after, .bp3-dark
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
          background-color:rgba(57, 75, 89, 0.5);
          background-image:none;
          -webkit-box-shadow:none;
                  box-shadow:none;
          color:rgba(167, 182, 194, 0.6); }
          .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-dark
          .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active{
            background:rgba(57, 75, 89, 0.7); }
  .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#182026; }
  .bp3-dark .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#f5f8fa; }
  .bp3-file-input.bp3-fill{
    width:100%; }
  .bp3-file-input.bp3-large,
  .bp3-large .bp3-file-input{
    height:40px; }
  .bp3-file-input .bp3-file-upload-input-custom-text::after{
    content:attr(bp3-button-text); }

.bp3-file-upload-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:rgba(92, 112, 128, 0.6);
  left:0;
  padding-right:80px;
  position:absolute;
  right:0;
  top:0;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-file-upload-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:focus, .bp3-file-upload-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-file-upload-input[type="search"], .bp3-file-upload-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-file-upload-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-file-upload-input:disabled, .bp3-file-upload-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-file-upload-input::after{
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026;
    min-height:24px;
    min-width:24px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    border-radius:3px;
    content:"Browse";
    line-height:24px;
    margin:3px;
    position:absolute;
    right:0;
    text-align:center;
    top:0;
    width:70px; }
    .bp3-file-upload-input::after:hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-file-upload-input::after:active, .bp3-file-upload-input::after.bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-file-upload-input::after:disabled, .bp3-file-upload-input::after.bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-file-upload-input::after:disabled.bp3-active, .bp3-file-upload-input::after:disabled.bp3-active:hover, .bp3-file-upload-input::after.bp3-disabled.bp3-active, .bp3-file-upload-input::after.bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-file-upload-input:hover::after{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-file-upload-input:active::after{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-large .bp3-file-upload-input{
    font-size:16px;
    height:40px;
    line-height:40px;
    padding-right:95px; }
    .bp3-large .bp3-file-upload-input[type="search"], .bp3-large .bp3-file-upload-input.bp3-round{
      padding:0 15px; }
    .bp3-large .bp3-file-upload-input::after{
      min-height:30px;
      min-width:30px;
      line-height:30px;
      margin:5px;
      width:85px; }
  .bp3-dark .bp3-file-upload-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:disabled, .bp3-dark .bp3-file-upload-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::after{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover, .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover{
        background-color:#30404d;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        background-color:#202b33;
        background-image:none;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
      .bp3-dark .bp3-file-upload-input::after:disabled, .bp3-dark .bp3-file-upload-input::after.bp3-disabled{
        background-color:rgba(57, 75, 89, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-upload-input::after:disabled.bp3-active, .bp3-dark .bp3-file-upload-input::after.bp3-disabled.bp3-active{
          background:rgba(57, 75, 89, 0.7); }
      .bp3-dark .bp3-file-upload-input::after .bp3-button-spinner .bp3-spinner-head{
        background:rgba(16, 22, 26, 0.5);
        stroke:#8a9ba8; }
    .bp3-dark .bp3-file-upload-input:hover::after{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:active::after{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
.bp3-file-upload-input::after{
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
.bp3-form-group{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0 0 15px; }
  .bp3-form-group label.bp3-label{
    margin-bottom:5px; }
  .bp3-form-group .bp3-control{
    margin-top:7px; }
  .bp3-form-group .bp3-form-helper-text{
    color:#5c7080;
    font-size:12px;
    margin-top:5px; }
  .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#106ba3; }
  .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#0d8050; }
  .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#bf7326; }
  .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#c23030; }
  .bp3-form-group.bp3-inline{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row; }
    .bp3-form-group.bp3-inline.bp3-large label.bp3-label{
      line-height:40px;
      margin:0 10px 0 0; }
    .bp3-form-group.bp3-inline label.bp3-label{
      line-height:30px;
      margin:0 10px 0 0; }
  .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-dark .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#48aff0; }
  .bp3-dark .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#3dcc91; }
  .bp3-dark .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#ffb366; }
  .bp3-dark .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#ff7373; }
  .bp3-dark .bp3-form-group .bp3-form-helper-text{
    color:#a7b6c2; }
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(167, 182, 194, 0.6) !important; }
.bp3-input-group{
  display:block;
  position:relative; }
  .bp3-input-group .bp3-input{
    position:relative;
    width:100%; }
    .bp3-input-group .bp3-input:not(:first-child){
      padding-left:30px; }
    .bp3-input-group .bp3-input:not(:last-child){
      padding-right:30px; }
  .bp3-input-group .bp3-input-action,
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-button,
  .bp3-input-group > .bp3-icon{
    position:absolute;
    top:0; }
    .bp3-input-group .bp3-input-action:first-child,
    .bp3-input-group > .bp3-input-left-container:first-child,
    .bp3-input-group > .bp3-button:first-child,
    .bp3-input-group > .bp3-icon:first-child{
      left:0; }
    .bp3-input-group .bp3-input-action:last-child,
    .bp3-input-group > .bp3-input-left-container:last-child,
    .bp3-input-group > .bp3-button:last-child,
    .bp3-input-group > .bp3-icon:last-child{
      right:0; }
  .bp3-input-group .bp3-button{
    min-height:24px;
    min-width:24px;
    margin:3px;
    padding:0 7px; }
    .bp3-input-group .bp3-button:empty{
      padding:0; }
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-icon{
    z-index:1; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon{
    color:#5c7080; }
    .bp3-input-group > .bp3-input-left-container > .bp3-icon:empty,
    .bp3-input-group > .bp3-icon:empty{
      font-family:"Icons16", sans-serif;
      font-size:16px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon,
  .bp3-input-group .bp3-input-action > .bp3-spinner{
    margin:7px; }
  .bp3-input-group .bp3-tag{
    margin:5px; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus),
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
    color:#5c7080; }
    .bp3-dark .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus), .bp3-dark
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
      color:#a7b6c2; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large{
      color:#5c7080; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled,
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled{
    color:rgba(92, 112, 128, 0.6) !important; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-large{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-input-group.bp3-disabled{
    cursor:not-allowed; }
    .bp3-input-group.bp3-disabled .bp3-icon{
      color:rgba(92, 112, 128, 0.6); }
  .bp3-input-group.bp3-large .bp3-button{
    min-height:30px;
    min-width:30px;
    margin:5px; }
  .bp3-input-group.bp3-large > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-large > .bp3-icon,
  .bp3-input-group.bp3-large .bp3-input-action > .bp3-spinner{
    margin:12px; }
  .bp3-input-group.bp3-large .bp3-input{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input-group.bp3-large .bp3-input[type="search"], .bp3-input-group.bp3-large .bp3-input.bp3-round{
      padding:0 15px; }
    .bp3-input-group.bp3-large .bp3-input:not(:first-child){
      padding-left:40px; }
    .bp3-input-group.bp3-large .bp3-input:not(:last-child){
      padding-right:40px; }
  .bp3-input-group.bp3-small .bp3-button{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small .bp3-tag{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-small > .bp3-icon,
  .bp3-input-group.bp3-small .bp3-input-action > .bp3-spinner{
    margin:4px; }
  .bp3-input-group.bp3-small .bp3-input{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input-group.bp3-small .bp3-input[type="search"], .bp3-input-group.bp3-small .bp3-input.bp3-round{
      padding:0 12px; }
    .bp3-input-group.bp3-small .bp3-input:not(:first-child){
      padding-left:24px; }
    .bp3-input-group.bp3-small .bp3-input:not(:last-child){
      padding-right:24px; }
  .bp3-input-group.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-input-group.bp3-round .bp3-button,
  .bp3-input-group.bp3-round .bp3-input,
  .bp3-input-group.bp3-round .bp3-tag{
    border-radius:30px; }
  .bp3-dark .bp3-input-group .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-input-group.bp3-disabled .bp3-icon{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-input-group.bp3-intent-primary .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input-group.bp3-intent-primary .bp3-input:disabled, .bp3-input-group.bp3-intent-primary .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-primary > .bp3-icon{
    color:#106ba3; }
    .bp3-dark .bp3-input-group.bp3-intent-primary > .bp3-icon{
      color:#48aff0; }
  .bp3-input-group.bp3-intent-success .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input-group.bp3-intent-success .bp3-input:disabled, .bp3-input-group.bp3-intent-success .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-success > .bp3-icon{
    color:#0d8050; }
    .bp3-dark .bp3-input-group.bp3-intent-success > .bp3-icon{
      color:#3dcc91; }
  .bp3-input-group.bp3-intent-warning .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input-group.bp3-intent-warning .bp3-input:disabled, .bp3-input-group.bp3-intent-warning .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-warning > .bp3-icon{
    color:#bf7326; }
    .bp3-dark .bp3-input-group.bp3-intent-warning > .bp3-icon{
      color:#ffb366; }
  .bp3-input-group.bp3-intent-danger .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input-group.bp3-intent-danger .bp3-input:disabled, .bp3-input-group.bp3-intent-danger .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-danger > .bp3-icon{
    color:#c23030; }
    .bp3-dark .bp3-input-group.bp3-intent-danger > .bp3-icon{
      color:#ff7373; }
.bp3-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle; }
  .bp3-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:focus, .bp3-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-input[type="search"], .bp3-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-input:disabled, .bp3-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-input.bp3-large{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input.bp3-large[type="search"], .bp3-input.bp3-large.bp3-round{
      padding:0 15px; }
  .bp3-input.bp3-small{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input.bp3-small[type="search"], .bp3-input.bp3-small.bp3-round{
      padding:0 12px; }
  .bp3-input.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-dark .bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input:disabled, .bp3-dark .bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-input.bp3-intent-primary{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input.bp3-intent-primary:disabled, .bp3-input.bp3-intent-primary.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary:focus{
        -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #137cbd;
                box-shadow:inset 0 0 0 1px #137cbd; }
      .bp3-dark .bp3-input.bp3-intent-primary:disabled, .bp3-dark .bp3-input.bp3-intent-primary.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-success{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input.bp3-intent-success:disabled, .bp3-input.bp3-intent-success.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-success{
      -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success:focus{
        -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #0f9960;
                box-shadow:inset 0 0 0 1px #0f9960; }
      .bp3-dark .bp3-input.bp3-intent-success:disabled, .bp3-dark .bp3-input.bp3-intent-success.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-warning{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input.bp3-intent-warning:disabled, .bp3-input.bp3-intent-warning.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning:focus{
        -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #d9822b;
                box-shadow:inset 0 0 0 1px #d9822b; }
      .bp3-dark .bp3-input.bp3-intent-warning:disabled, .bp3-dark .bp3-input.bp3-intent-warning.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-danger{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input.bp3-intent-danger:disabled, .bp3-input.bp3-intent-danger.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger:focus{
        -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #db3737;
                box-shadow:inset 0 0 0 1px #db3737; }
      .bp3-dark .bp3-input.bp3-intent-danger:disabled, .bp3-dark .bp3-input.bp3-intent-danger.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input::-ms-clear{
    display:none; }
textarea.bp3-input{
  max-width:100%;
  padding:10px; }
  textarea.bp3-input, textarea.bp3-input.bp3-large, textarea.bp3-input.bp3-small{
    height:auto;
    line-height:inherit; }
  textarea.bp3-input.bp3-small{
    padding:8px; }
  .bp3-dark textarea.bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark textarea.bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input:disabled, .bp3-dark textarea.bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
label.bp3-label{
  display:block;
  margin-bottom:15px;
  margin-top:0; }
  label.bp3-label .bp3-html-select,
  label.bp3-label .bp3-input,
  label.bp3-label .bp3-select,
  label.bp3-label .bp3-slider,
  label.bp3-label .bp3-popover-wrapper{
    display:block;
    margin-top:5px;
    text-transform:none; }
  label.bp3-label .bp3-button-group{
    margin-top:5px; }
  label.bp3-label .bp3-select select,
  label.bp3-label .bp3-html-select select{
    font-weight:400;
    vertical-align:top;
    width:100%; }
  label.bp3-label.bp3-disabled,
  label.bp3-label.bp3-disabled .bp3-text-muted{
    color:rgba(92, 112, 128, 0.6); }
  label.bp3-label.bp3-inline{
    line-height:30px; }
    label.bp3-label.bp3-inline .bp3-html-select,
    label.bp3-label.bp3-inline .bp3-input,
    label.bp3-label.bp3-inline .bp3-input-group,
    label.bp3-label.bp3-inline .bp3-select,
    label.bp3-label.bp3-inline .bp3-popover-wrapper{
      display:inline-block;
      margin:0 0 0 5px;
      vertical-align:top; }
    label.bp3-label.bp3-inline .bp3-button-group{
      margin:0 0 0 5px; }
    label.bp3-label.bp3-inline .bp3-input-group .bp3-input{
      margin-left:0; }
    label.bp3-label.bp3-inline.bp3-large{
      line-height:40px; }
  label.bp3-label:not(.bp3-inline) .bp3-popover-target{
    display:block; }
  .bp3-dark label.bp3-label{
    color:#f5f8fa; }
    .bp3-dark label.bp3-label.bp3-disabled,
    .bp3-dark label.bp3-label.bp3-disabled .bp3-text-muted{
      color:rgba(167, 182, 194, 0.6); }
.bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button{
  -webkit-box-flex:1;
      -ms-flex:1 1 14px;
          flex:1 1 14px;
  min-height:0;
  padding:0;
  width:30px; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:first-child{
    border-radius:0 3px 0 0; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:last-child{
    border-radius:0 0 3px 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:first-child{
  border-radius:3px 0 0 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:last-child{
  border-radius:0 0 0 3px; }

.bp3-numeric-input.bp3-large .bp3-button-group.bp3-vertical > .bp3-button{
  width:40px; }

form{
  display:block; }
.bp3-html-select select,
.bp3-select select{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  -moz-appearance:none;
  -webkit-appearance:none;
  border-radius:3px;
  height:30px;
  padding:0 25px 0 10px;
  width:100%; }
  .bp3-html-select select > *, .bp3-select select > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-html-select select > .bp3-fill, .bp3-select select > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-html-select select::before,
  .bp3-select select::before, .bp3-html-select select > *, .bp3-select select > *{
    margin-right:7px; }
  .bp3-html-select select:empty::before,
  .bp3-select select:empty::before,
  .bp3-html-select select > :last-child,
  .bp3-select select > :last-child{
    margin-right:0; }
  .bp3-html-select select:hover,
  .bp3-select select:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-html-select select:active,
  .bp3-select select:active, .bp3-html-select select.bp3-active,
  .bp3-select select.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-html-select select:disabled,
  .bp3-select select:disabled, .bp3-html-select select.bp3-disabled,
  .bp3-select select.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-html-select select:disabled.bp3-active,
    .bp3-select select:disabled.bp3-active, .bp3-html-select select:disabled.bp3-active:hover,
    .bp3-select select:disabled.bp3-active:hover, .bp3-html-select select.bp3-disabled.bp3-active,
    .bp3-select select.bp3-disabled.bp3-active, .bp3-html-select select.bp3-disabled.bp3-active:hover,
    .bp3-select select.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }

.bp3-html-select.bp3-minimal select,
.bp3-select.bp3-minimal select{
  background:none;
  -webkit-box-shadow:none;
          box-shadow:none; }
  .bp3-html-select.bp3-minimal select:hover,
  .bp3-select.bp3-minimal select:hover{
    background:rgba(167, 182, 194, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026;
    text-decoration:none; }
  .bp3-html-select.bp3-minimal select:active,
  .bp3-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal select.bp3-active,
  .bp3-select.bp3-minimal select.bp3-active{
    background:rgba(115, 134, 148, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026; }
  .bp3-html-select.bp3-minimal select:disabled,
  .bp3-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal select:disabled:hover,
  .bp3-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal select.bp3-disabled,
  .bp3-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal select.bp3-disabled:hover,
  .bp3-select.bp3-minimal select.bp3-disabled:hover{
    background:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
    .bp3-html-select.bp3-minimal select:disabled.bp3-active,
    .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active{
      background:rgba(115, 134, 148, 0.3); }
  .bp3-dark .bp3-html-select.bp3-minimal select, .bp3-html-select.bp3-minimal .bp3-dark select,
  .bp3-dark .bp3-select.bp3-minimal select, .bp3-select.bp3-minimal .bp3-dark select{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover, .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover{
      background:rgba(138, 155, 168, 0.15); }
    .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:rgba(138, 155, 168, 0.3);
      color:#f5f8fa; }
    .bp3-dark .bp3-html-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal .bp3-dark select:disabled,
    .bp3-dark .bp3-select.bp3-minimal select:disabled, .bp3-select.bp3-minimal .bp3-dark select:disabled, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select:disabled:hover, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover{
      background:none;
      color:rgba(167, 182, 194, 0.6);
      cursor:not-allowed; }
      .bp3-dark .bp3-html-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active{
        background:rgba(138, 155, 168, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-primary,
  .bp3-select.bp3-minimal select.bp3-intent-primary{
    color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover{
      background:rgba(19, 124, 189, 0.15);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:rgba(19, 124, 189, 0.3);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled{
      background:none;
      color:rgba(16, 107, 163, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active{
        background:rgba(19, 124, 189, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
      stroke:#106ba3; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary{
      color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.2);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(72, 175, 240, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-success,
  .bp3-select.bp3-minimal select.bp3-intent-success{
    color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover{
      background:rgba(15, 153, 96, 0.15);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:rgba(15, 153, 96, 0.3);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled{
      background:none;
      color:rgba(13, 128, 80, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active{
        background:rgba(15, 153, 96, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
      stroke:#0d8050; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success{
      color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.2);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(61, 204, 145, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-warning,
  .bp3-select.bp3-minimal select.bp3-intent-warning{
    color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover{
      background:rgba(217, 130, 43, 0.15);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:rgba(217, 130, 43, 0.3);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled{
      background:none;
      color:rgba(191, 115, 38, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active{
        background:rgba(217, 130, 43, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
      stroke:#bf7326; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning{
      color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.2);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(255, 179, 102, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-danger,
  .bp3-select.bp3-minimal select.bp3-intent-danger{
    color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover{
      background:rgba(219, 55, 55, 0.15);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:rgba(219, 55, 55, 0.3);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled{
      background:none;
      color:rgba(194, 48, 48, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active{
        background:rgba(219, 55, 55, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
      stroke:#c23030; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger{
      color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.2);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(255, 115, 115, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }

.bp3-html-select.bp3-large select,
.bp3-select.bp3-large select{
  font-size:16px;
  height:40px;
  padding-right:35px; }

.bp3-dark .bp3-html-select select, .bp3-dark .bp3-select select{
  background-color:#394b59;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
  color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover, .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    background-color:#202b33;
    background-image:none;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-html-select select:disabled, .bp3-dark .bp3-select select:disabled, .bp3-dark .bp3-html-select select.bp3-disabled, .bp3-dark .bp3-select select.bp3-disabled{
    background-color:rgba(57, 75, 89, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-html-select select:disabled.bp3-active, .bp3-dark .bp3-select select:disabled.bp3-active, .bp3-dark .bp3-html-select select.bp3-disabled.bp3-active, .bp3-dark .bp3-select select.bp3-disabled.bp3-active{
      background:rgba(57, 75, 89, 0.7); }
  .bp3-dark .bp3-html-select select .bp3-button-spinner .bp3-spinner-head, .bp3-dark .bp3-select select .bp3-button-spinner .bp3-spinner-head{
    background:rgba(16, 22, 26, 0.5);
    stroke:#8a9ba8; }

.bp3-html-select select:disabled,
.bp3-select select:disabled{
  background-color:rgba(206, 217, 224, 0.5);
  -webkit-box-shadow:none;
          box-shadow:none;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-html-select .bp3-icon,
.bp3-select .bp3-icon, .bp3-select::after{
  color:#5c7080;
  pointer-events:none;
  position:absolute;
  right:7px;
  top:7px; }
  .bp3-html-select .bp3-disabled.bp3-icon,
  .bp3-select .bp3-disabled.bp3-icon, .bp3-disabled.bp3-select::after{
    color:rgba(92, 112, 128, 0.6); }
.bp3-html-select,
.bp3-select{
  display:inline-block;
  letter-spacing:normal;
  position:relative;
  vertical-align:middle; }
  .bp3-html-select select::-ms-expand,
  .bp3-select select::-ms-expand{
    display:none; }
  .bp3-html-select .bp3-icon,
  .bp3-select .bp3-icon{
    color:#5c7080; }
    .bp3-html-select .bp3-icon:hover,
    .bp3-select .bp3-icon:hover{
      color:#182026; }
    .bp3-dark .bp3-html-select .bp3-icon, .bp3-dark
    .bp3-select .bp3-icon{
      color:#a7b6c2; }
      .bp3-dark .bp3-html-select .bp3-icon:hover, .bp3-dark
      .bp3-select .bp3-icon:hover{
        color:#f5f8fa; }
  .bp3-html-select.bp3-large::after,
  .bp3-html-select.bp3-large .bp3-icon,
  .bp3-select.bp3-large::after,
  .bp3-select.bp3-large .bp3-icon{
    right:12px;
    top:12px; }
  .bp3-html-select.bp3-fill,
  .bp3-html-select.bp3-fill select,
  .bp3-select.bp3-fill,
  .bp3-select.bp3-fill select{
    width:100%; }
  .bp3-dark .bp3-html-select option, .bp3-dark
  .bp3-select option{
    background-color:#30404d;
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select option:disabled, .bp3-dark
  .bp3-select option:disabled{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-html-select::after, .bp3-dark
  .bp3-select::after{
    color:#a7b6c2; }

.bp3-select::after{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  content:""; }
.bp3-running-text table, table.bp3-html-table{
  border-spacing:0;
  font-size:14px; }
  .bp3-running-text table th, table.bp3-html-table th,
  .bp3-running-text table td,
  table.bp3-html-table td{
    padding:11px;
    text-align:left;
    vertical-align:top; }
  .bp3-running-text table th, table.bp3-html-table th{
    color:#182026;
    font-weight:600; }
  
  .bp3-running-text table td,
  table.bp3-html-table td{
    color:#182026; }
  .bp3-running-text table tbody tr:first-child th, table.bp3-html-table tbody tr:first-child th,
  .bp3-running-text table tbody tr:first-child td,
  table.bp3-html-table tbody tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-running-text table th, .bp3-running-text .bp3-dark table th, .bp3-dark table.bp3-html-table th{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table td, .bp3-running-text .bp3-dark table td, .bp3-dark table.bp3-html-table td{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table tbody tr:first-child th, .bp3-running-text .bp3-dark table tbody tr:first-child th, .bp3-dark table.bp3-html-table tbody tr:first-child th,
  .bp3-dark .bp3-running-text table tbody tr:first-child td,
  .bp3-running-text .bp3-dark table tbody tr:first-child td,
  .bp3-dark table.bp3-html-table tbody tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }

table.bp3-html-table.bp3-html-table-condensed th,
table.bp3-html-table.bp3-html-table-condensed td, table.bp3-html-table.bp3-small th,
table.bp3-html-table.bp3-small td{
  padding-bottom:6px;
  padding-top:6px; }

table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(191, 204, 214, 0.15); }

table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered tbody tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:none;
          box-shadow:none; }
  table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(191, 204, 214, 0.3);
  cursor:pointer; }

table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(191, 204, 214, 0.4); }

.bp3-dark table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(92, 112, 128, 0.15); }

.bp3-dark table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }

.bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15); }

.bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:first-child{
    -webkit-box-shadow:none;
            box-shadow:none; }

.bp3-dark table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(92, 112, 128, 0.3);
  cursor:pointer; }

.bp3-dark table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(92, 112, 128, 0.4); }

.bp3-key-combo{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center; }
  .bp3-key-combo > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-key-combo > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-key-combo::before,
  .bp3-key-combo > *{
    margin-right:5px; }
  .bp3-key-combo:empty::before,
  .bp3-key-combo > :last-child{
    margin-right:0; }

.bp3-hotkey-dialog{
  padding-bottom:0;
  top:40px; }
  .bp3-hotkey-dialog .bp3-dialog-body{
    margin:0;
    padding:0; }
  .bp3-hotkey-dialog .bp3-hotkey-label{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1; }

.bp3-hotkey-column{
  margin:auto;
  max-height:80vh;
  overflow-y:auto;
  padding:30px; }
  .bp3-hotkey-column .bp3-heading{
    margin-bottom:20px; }
    .bp3-hotkey-column .bp3-heading:not(:first-child){
      margin-top:40px; }

.bp3-hotkey{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:justify;
      -ms-flex-pack:justify;
          justify-content:space-between;
  margin-left:0;
  margin-right:0; }
  .bp3-hotkey:not(:last-child){
    margin-bottom:10px; }
.bp3-icon{
  display:inline-block;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  vertical-align:text-bottom; }
  .bp3-icon:not(:empty)::before{
    content:"" !important;
    content:unset !important; }
  .bp3-icon > svg{
    display:block; }
    .bp3-icon > svg:not([fill]){
      fill:currentColor; }

.bp3-icon.bp3-intent-primary, .bp3-icon-standard.bp3-intent-primary, .bp3-icon-large.bp3-intent-primary{
  color:#106ba3; }
  .bp3-dark .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-icon-large.bp3-intent-primary{
    color:#48aff0; }

.bp3-icon.bp3-intent-success, .bp3-icon-standard.bp3-intent-success, .bp3-icon-large.bp3-intent-success{
  color:#0d8050; }
  .bp3-dark .bp3-icon.bp3-intent-success, .bp3-dark .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-icon-large.bp3-intent-success{
    color:#3dcc91; }

.bp3-icon.bp3-intent-warning, .bp3-icon-standard.bp3-intent-warning, .bp3-icon-large.bp3-intent-warning{
  color:#bf7326; }
  .bp3-dark .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-icon-large.bp3-intent-warning{
    color:#ffb366; }

.bp3-icon.bp3-intent-danger, .bp3-icon-standard.bp3-intent-danger, .bp3-icon-large.bp3-intent-danger{
  color:#c23030; }
  .bp3-dark .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-icon-large.bp3-intent-danger{
    color:#ff7373; }

span.bp3-icon-standard{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon-large{
  font-family:"Icons20", sans-serif;
  font-size:20px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon:empty{
  font-family:"Icons20";
  font-size:inherit;
  font-style:normal;
  font-weight:400;
  line-height:1; }
  span.bp3-icon:empty::before{
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased; }

.bp3-icon-add::before{
  content:""; }

.bp3-icon-add-column-left::before{
  content:""; }

.bp3-icon-add-column-right::before{
  content:""; }

.bp3-icon-add-row-bottom::before{
  content:""; }

.bp3-icon-add-row-top::before{
  content:""; }

.bp3-icon-add-to-artifact::before{
  content:""; }

.bp3-icon-add-to-folder::before{
  content:""; }

.bp3-icon-airplane::before{
  content:""; }

.bp3-icon-align-center::before{
  content:""; }

.bp3-icon-align-justify::before{
  content:""; }

.bp3-icon-align-left::before{
  content:""; }

.bp3-icon-align-right::before{
  content:""; }

.bp3-icon-alignment-bottom::before{
  content:""; }

.bp3-icon-alignment-horizontal-center::before{
  content:""; }

.bp3-icon-alignment-left::before{
  content:""; }

.bp3-icon-alignment-right::before{
  content:""; }

.bp3-icon-alignment-top::before{
  content:""; }

.bp3-icon-alignment-vertical-center::before{
  content:""; }

.bp3-icon-annotation::before{
  content:""; }

.bp3-icon-application::before{
  content:""; }

.bp3-icon-applications::before{
  content:""; }

.bp3-icon-archive::before{
  content:""; }

.bp3-icon-arrow-bottom-left::before{
  content:"↙"; }

.bp3-icon-arrow-bottom-right::before{
  content:"↘"; }

.bp3-icon-arrow-down::before{
  content:"↓"; }

.bp3-icon-arrow-left::before{
  content:"←"; }

.bp3-icon-arrow-right::before{
  content:"→"; }

.bp3-icon-arrow-top-left::before{
  content:"↖"; }

.bp3-icon-arrow-top-right::before{
  content:"↗"; }

.bp3-icon-arrow-up::before{
  content:"↑"; }

.bp3-icon-arrows-horizontal::before{
  content:"↔"; }

.bp3-icon-arrows-vertical::before{
  content:"↕"; }

.bp3-icon-asterisk::before{
  content:"*"; }

.bp3-icon-automatic-updates::before{
  content:""; }

.bp3-icon-badge::before{
  content:""; }

.bp3-icon-ban-circle::before{
  content:""; }

.bp3-icon-bank-account::before{
  content:""; }

.bp3-icon-barcode::before{
  content:""; }

.bp3-icon-blank::before{
  content:""; }

.bp3-icon-blocked-person::before{
  content:""; }

.bp3-icon-bold::before{
  content:""; }

.bp3-icon-book::before{
  content:""; }

.bp3-icon-bookmark::before{
  content:""; }

.bp3-icon-box::before{
  content:""; }

.bp3-icon-briefcase::before{
  content:""; }

.bp3-icon-bring-data::before{
  content:""; }

.bp3-icon-build::before{
  content:""; }

.bp3-icon-calculator::before{
  content:""; }

.bp3-icon-calendar::before{
  content:""; }

.bp3-icon-camera::before{
  content:""; }

.bp3-icon-caret-down::before{
  content:"⌄"; }

.bp3-icon-caret-left::before{
  content:"〈"; }

.bp3-icon-caret-right::before{
  content:"〉"; }

.bp3-icon-caret-up::before{
  content:"⌃"; }

.bp3-icon-cell-tower::before{
  content:""; }

.bp3-icon-changes::before{
  content:""; }

.bp3-icon-chart::before{
  content:""; }

.bp3-icon-chat::before{
  content:""; }

.bp3-icon-chevron-backward::before{
  content:""; }

.bp3-icon-chevron-down::before{
  content:""; }

.bp3-icon-chevron-forward::before{
  content:""; }

.bp3-icon-chevron-left::before{
  content:""; }

.bp3-icon-chevron-right::before{
  content:""; }

.bp3-icon-chevron-up::before{
  content:""; }

.bp3-icon-circle::before{
  content:""; }

.bp3-icon-circle-arrow-down::before{
  content:""; }

.bp3-icon-circle-arrow-left::before{
  content:""; }

.bp3-icon-circle-arrow-right::before{
  content:""; }

.bp3-icon-circle-arrow-up::before{
  content:""; }

.bp3-icon-citation::before{
  content:""; }

.bp3-icon-clean::before{
  content:""; }

.bp3-icon-clipboard::before{
  content:""; }

.bp3-icon-cloud::before{
  content:"☁"; }

.bp3-icon-cloud-download::before{
  content:""; }

.bp3-icon-cloud-upload::before{
  content:""; }

.bp3-icon-code::before{
  content:""; }

.bp3-icon-code-block::before{
  content:""; }

.bp3-icon-cog::before{
  content:""; }

.bp3-icon-collapse-all::before{
  content:""; }

.bp3-icon-column-layout::before{
  content:""; }

.bp3-icon-comment::before{
  content:""; }

.bp3-icon-comparison::before{
  content:""; }

.bp3-icon-compass::before{
  content:""; }

.bp3-icon-compressed::before{
  content:""; }

.bp3-icon-confirm::before{
  content:""; }

.bp3-icon-console::before{
  content:""; }

.bp3-icon-contrast::before{
  content:""; }

.bp3-icon-control::before{
  content:""; }

.bp3-icon-credit-card::before{
  content:""; }

.bp3-icon-cross::before{
  content:"✗"; }

.bp3-icon-crown::before{
  content:""; }

.bp3-icon-cube::before{
  content:""; }

.bp3-icon-cube-add::before{
  content:""; }

.bp3-icon-cube-remove::before{
  content:""; }

.bp3-icon-curved-range-chart::before{
  content:""; }

.bp3-icon-cut::before{
  content:""; }

.bp3-icon-dashboard::before{
  content:""; }

.bp3-icon-data-lineage::before{
  content:""; }

.bp3-icon-database::before{
  content:""; }

.bp3-icon-delete::before{
  content:""; }

.bp3-icon-delta::before{
  content:"Δ"; }

.bp3-icon-derive-column::before{
  content:""; }

.bp3-icon-desktop::before{
  content:""; }

.bp3-icon-diagnosis::before{
  content:""; }

.bp3-icon-diagram-tree::before{
  content:""; }

.bp3-icon-direction-left::before{
  content:""; }

.bp3-icon-direction-right::before{
  content:""; }

.bp3-icon-disable::before{
  content:""; }

.bp3-icon-document::before{
  content:""; }

.bp3-icon-document-open::before{
  content:""; }

.bp3-icon-document-share::before{
  content:""; }

.bp3-icon-dollar::before{
  content:"$"; }

.bp3-icon-dot::before{
  content:"•"; }

.bp3-icon-double-caret-horizontal::before{
  content:""; }

.bp3-icon-double-caret-vertical::before{
  content:""; }

.bp3-icon-double-chevron-down::before{
  content:""; }

.bp3-icon-double-chevron-left::before{
  content:""; }

.bp3-icon-double-chevron-right::before{
  content:""; }

.bp3-icon-double-chevron-up::before{
  content:""; }

.bp3-icon-doughnut-chart::before{
  content:""; }

.bp3-icon-download::before{
  content:""; }

.bp3-icon-drag-handle-horizontal::before{
  content:""; }

.bp3-icon-drag-handle-vertical::before{
  content:""; }

.bp3-icon-draw::before{
  content:""; }

.bp3-icon-drive-time::before{
  content:""; }

.bp3-icon-duplicate::before{
  content:""; }

.bp3-icon-edit::before{
  content:"✎"; }

.bp3-icon-eject::before{
  content:"⏏"; }

.bp3-icon-endorsed::before{
  content:""; }

.bp3-icon-envelope::before{
  content:"✉"; }

.bp3-icon-equals::before{
  content:""; }

.bp3-icon-eraser::before{
  content:""; }

.bp3-icon-error::before{
  content:""; }

.bp3-icon-euro::before{
  content:"€"; }

.bp3-icon-exchange::before{
  content:""; }

.bp3-icon-exclude-row::before{
  content:""; }

.bp3-icon-expand-all::before{
  content:""; }

.bp3-icon-export::before{
  content:""; }

.bp3-icon-eye-off::before{
  content:""; }

.bp3-icon-eye-on::before{
  content:""; }

.bp3-icon-eye-open::before{
  content:""; }

.bp3-icon-fast-backward::before{
  content:""; }

.bp3-icon-fast-forward::before{
  content:""; }

.bp3-icon-feed::before{
  content:""; }

.bp3-icon-feed-subscribed::before{
  content:""; }

.bp3-icon-film::before{
  content:""; }

.bp3-icon-filter::before{
  content:""; }

.bp3-icon-filter-keep::before{
  content:""; }

.bp3-icon-filter-list::before{
  content:""; }

.bp3-icon-filter-open::before{
  content:""; }

.bp3-icon-filter-remove::before{
  content:""; }

.bp3-icon-flag::before{
  content:"⚑"; }

.bp3-icon-flame::before{
  content:""; }

.bp3-icon-flash::before{
  content:""; }

.bp3-icon-floppy-disk::before{
  content:""; }

.bp3-icon-flow-branch::before{
  content:""; }

.bp3-icon-flow-end::before{
  content:""; }

.bp3-icon-flow-linear::before{
  content:""; }

.bp3-icon-flow-review::before{
  content:""; }

.bp3-icon-flow-review-branch::before{
  content:""; }

.bp3-icon-flows::before{
  content:""; }

.bp3-icon-folder-close::before{
  content:""; }

.bp3-icon-folder-new::before{
  content:""; }

.bp3-icon-folder-open::before{
  content:""; }

.bp3-icon-folder-shared::before{
  content:""; }

.bp3-icon-folder-shared-open::before{
  content:""; }

.bp3-icon-follower::before{
  content:""; }

.bp3-icon-following::before{
  content:""; }

.bp3-icon-font::before{
  content:""; }

.bp3-icon-fork::before{
  content:""; }

.bp3-icon-form::before{
  content:""; }

.bp3-icon-full-circle::before{
  content:""; }

.bp3-icon-full-stacked-chart::before{
  content:""; }

.bp3-icon-fullscreen::before{
  content:""; }

.bp3-icon-function::before{
  content:""; }

.bp3-icon-gantt-chart::before{
  content:""; }

.bp3-icon-geolocation::before{
  content:""; }

.bp3-icon-geosearch::before{
  content:""; }

.bp3-icon-git-branch::before{
  content:""; }

.bp3-icon-git-commit::before{
  content:""; }

.bp3-icon-git-merge::before{
  content:""; }

.bp3-icon-git-new-branch::before{
  content:""; }

.bp3-icon-git-pull::before{
  content:""; }

.bp3-icon-git-push::before{
  content:""; }

.bp3-icon-git-repo::before{
  content:""; }

.bp3-icon-glass::before{
  content:""; }

.bp3-icon-globe::before{
  content:""; }

.bp3-icon-globe-network::before{
  content:""; }

.bp3-icon-graph::before{
  content:""; }

.bp3-icon-graph-remove::before{
  content:""; }

.bp3-icon-greater-than::before{
  content:""; }

.bp3-icon-greater-than-or-equal-to::before{
  content:""; }

.bp3-icon-grid::before{
  content:""; }

.bp3-icon-grid-view::before{
  content:""; }

.bp3-icon-group-objects::before{
  content:""; }

.bp3-icon-grouped-bar-chart::before{
  content:""; }

.bp3-icon-hand::before{
  content:""; }

.bp3-icon-hand-down::before{
  content:""; }

.bp3-icon-hand-left::before{
  content:""; }

.bp3-icon-hand-right::before{
  content:""; }

.bp3-icon-hand-up::before{
  content:""; }

.bp3-icon-header::before{
  content:""; }

.bp3-icon-header-one::before{
  content:""; }

.bp3-icon-header-two::before{
  content:""; }

.bp3-icon-headset::before{
  content:""; }

.bp3-icon-heart::before{
  content:"♥"; }

.bp3-icon-heart-broken::before{
  content:""; }

.bp3-icon-heat-grid::before{
  content:""; }

.bp3-icon-heatmap::before{
  content:""; }

.bp3-icon-help::before{
  content:"?"; }

.bp3-icon-helper-management::before{
  content:""; }

.bp3-icon-highlight::before{
  content:""; }

.bp3-icon-history::before{
  content:""; }

.bp3-icon-home::before{
  content:"⌂"; }

.bp3-icon-horizontal-bar-chart::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-asc::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-desc::before{
  content:""; }

.bp3-icon-horizontal-distribution::before{
  content:""; }

.bp3-icon-id-number::before{
  content:""; }

.bp3-icon-image-rotate-left::before{
  content:""; }

.bp3-icon-image-rotate-right::before{
  content:""; }

.bp3-icon-import::before{
  content:""; }

.bp3-icon-inbox::before{
  content:""; }

.bp3-icon-inbox-filtered::before{
  content:""; }

.bp3-icon-inbox-geo::before{
  content:""; }

.bp3-icon-inbox-search::before{
  content:""; }

.bp3-icon-inbox-update::before{
  content:""; }

.bp3-icon-info-sign::before{
  content:"ℹ"; }

.bp3-icon-inheritance::before{
  content:""; }

.bp3-icon-inner-join::before{
  content:""; }

.bp3-icon-insert::before{
  content:""; }

.bp3-icon-intersection::before{
  content:""; }

.bp3-icon-ip-address::before{
  content:""; }

.bp3-icon-issue::before{
  content:""; }

.bp3-icon-issue-closed::before{
  content:""; }

.bp3-icon-issue-new::before{
  content:""; }

.bp3-icon-italic::before{
  content:""; }

.bp3-icon-join-table::before{
  content:""; }

.bp3-icon-key::before{
  content:""; }

.bp3-icon-key-backspace::before{
  content:""; }

.bp3-icon-key-command::before{
  content:""; }

.bp3-icon-key-control::before{
  content:""; }

.bp3-icon-key-delete::before{
  content:""; }

.bp3-icon-key-enter::before{
  content:""; }

.bp3-icon-key-escape::before{
  content:""; }

.bp3-icon-key-option::before{
  content:""; }

.bp3-icon-key-shift::before{
  content:""; }

.bp3-icon-key-tab::before{
  content:""; }

.bp3-icon-known-vehicle::before{
  content:""; }

.bp3-icon-lab-test::before{
  content:""; }

.bp3-icon-label::before{
  content:""; }

.bp3-icon-layer::before{
  content:""; }

.bp3-icon-layers::before{
  content:""; }

.bp3-icon-layout::before{
  content:""; }

.bp3-icon-layout-auto::before{
  content:""; }

.bp3-icon-layout-balloon::before{
  content:""; }

.bp3-icon-layout-circle::before{
  content:""; }

.bp3-icon-layout-grid::before{
  content:""; }

.bp3-icon-layout-group-by::before{
  content:""; }

.bp3-icon-layout-hierarchy::before{
  content:""; }

.bp3-icon-layout-linear::before{
  content:""; }

.bp3-icon-layout-skew-grid::before{
  content:""; }

.bp3-icon-layout-sorted-clusters::before{
  content:""; }

.bp3-icon-learning::before{
  content:""; }

.bp3-icon-left-join::before{
  content:""; }

.bp3-icon-less-than::before{
  content:""; }

.bp3-icon-less-than-or-equal-to::before{
  content:""; }

.bp3-icon-lifesaver::before{
  content:""; }

.bp3-icon-lightbulb::before{
  content:""; }

.bp3-icon-link::before{
  content:""; }

.bp3-icon-list::before{
  content:"☰"; }

.bp3-icon-list-columns::before{
  content:""; }

.bp3-icon-list-detail-view::before{
  content:""; }

.bp3-icon-locate::before{
  content:""; }

.bp3-icon-lock::before{
  content:""; }

.bp3-icon-log-in::before{
  content:""; }

.bp3-icon-log-out::before{
  content:""; }

.bp3-icon-manual::before{
  content:""; }

.bp3-icon-manually-entered-data::before{
  content:""; }

.bp3-icon-map::before{
  content:""; }

.bp3-icon-map-create::before{
  content:""; }

.bp3-icon-map-marker::before{
  content:""; }

.bp3-icon-maximize::before{
  content:""; }

.bp3-icon-media::before{
  content:""; }

.bp3-icon-menu::before{
  content:""; }

.bp3-icon-menu-closed::before{
  content:""; }

.bp3-icon-menu-open::before{
  content:""; }

.bp3-icon-merge-columns::before{
  content:""; }

.bp3-icon-merge-links::before{
  content:""; }

.bp3-icon-minimize::before{
  content:""; }

.bp3-icon-minus::before{
  content:"−"; }

.bp3-icon-mobile-phone::before{
  content:""; }

.bp3-icon-mobile-video::before{
  content:""; }

.bp3-icon-moon::before{
  content:""; }

.bp3-icon-more::before{
  content:""; }

.bp3-icon-mountain::before{
  content:""; }

.bp3-icon-move::before{
  content:""; }

.bp3-icon-mugshot::before{
  content:""; }

.bp3-icon-multi-select::before{
  content:""; }

.bp3-icon-music::before{
  content:""; }

.bp3-icon-new-drawing::before{
  content:""; }

.bp3-icon-new-grid-item::before{
  content:""; }

.bp3-icon-new-layer::before{
  content:""; }

.bp3-icon-new-layers::before{
  content:""; }

.bp3-icon-new-link::before{
  content:""; }

.bp3-icon-new-object::before{
  content:""; }

.bp3-icon-new-person::before{
  content:""; }

.bp3-icon-new-prescription::before{
  content:""; }

.bp3-icon-new-text-box::before{
  content:""; }

.bp3-icon-ninja::before{
  content:""; }

.bp3-icon-not-equal-to::before{
  content:""; }

.bp3-icon-notifications::before{
  content:""; }

.bp3-icon-notifications-updated::before{
  content:""; }

.bp3-icon-numbered-list::before{
  content:""; }

.bp3-icon-numerical::before{
  content:""; }

.bp3-icon-office::before{
  content:""; }

.bp3-icon-offline::before{
  content:""; }

.bp3-icon-oil-field::before{
  content:""; }

.bp3-icon-one-column::before{
  content:""; }

.bp3-icon-outdated::before{
  content:""; }

.bp3-icon-page-layout::before{
  content:""; }

.bp3-icon-panel-stats::before{
  content:""; }

.bp3-icon-panel-table::before{
  content:""; }

.bp3-icon-paperclip::before{
  content:""; }

.bp3-icon-paragraph::before{
  content:""; }

.bp3-icon-path::before{
  content:""; }

.bp3-icon-path-search::before{
  content:""; }

.bp3-icon-pause::before{
  content:""; }

.bp3-icon-people::before{
  content:""; }

.bp3-icon-percentage::before{
  content:""; }

.bp3-icon-person::before{
  content:""; }

.bp3-icon-phone::before{
  content:"☎"; }

.bp3-icon-pie-chart::before{
  content:""; }

.bp3-icon-pin::before{
  content:""; }

.bp3-icon-pivot::before{
  content:""; }

.bp3-icon-pivot-table::before{
  content:""; }

.bp3-icon-play::before{
  content:""; }

.bp3-icon-plus::before{
  content:"+"; }

.bp3-icon-polygon-filter::before{
  content:""; }

.bp3-icon-power::before{
  content:""; }

.bp3-icon-predictive-analysis::before{
  content:""; }

.bp3-icon-prescription::before{
  content:""; }

.bp3-icon-presentation::before{
  content:""; }

.bp3-icon-print::before{
  content:"⎙"; }

.bp3-icon-projects::before{
  content:""; }

.bp3-icon-properties::before{
  content:""; }

.bp3-icon-property::before{
  content:""; }

.bp3-icon-publish-function::before{
  content:""; }

.bp3-icon-pulse::before{
  content:""; }

.bp3-icon-random::before{
  content:""; }

.bp3-icon-record::before{
  content:""; }

.bp3-icon-redo::before{
  content:""; }

.bp3-icon-refresh::before{
  content:""; }

.bp3-icon-regression-chart::before{
  content:""; }

.bp3-icon-remove::before{
  content:""; }

.bp3-icon-remove-column::before{
  content:""; }

.bp3-icon-remove-column-left::before{
  content:""; }

.bp3-icon-remove-column-right::before{
  content:""; }

.bp3-icon-remove-row-bottom::before{
  content:""; }

.bp3-icon-remove-row-top::before{
  content:""; }

.bp3-icon-repeat::before{
  content:""; }

.bp3-icon-reset::before{
  content:""; }

.bp3-icon-resolve::before{
  content:""; }

.bp3-icon-rig::before{
  content:""; }

.bp3-icon-right-join::before{
  content:""; }

.bp3-icon-ring::before{
  content:""; }

.bp3-icon-rotate-document::before{
  content:""; }

.bp3-icon-rotate-page::before{
  content:""; }

.bp3-icon-satellite::before{
  content:""; }

.bp3-icon-saved::before{
  content:""; }

.bp3-icon-scatter-plot::before{
  content:""; }

.bp3-icon-search::before{
  content:""; }

.bp3-icon-search-around::before{
  content:""; }

.bp3-icon-search-template::before{
  content:""; }

.bp3-icon-search-text::before{
  content:""; }

.bp3-icon-segmented-control::before{
  content:""; }

.bp3-icon-select::before{
  content:""; }

.bp3-icon-selection::before{
  content:"⦿"; }

.bp3-icon-send-to::before{
  content:""; }

.bp3-icon-send-to-graph::before{
  content:""; }

.bp3-icon-send-to-map::before{
  content:""; }

.bp3-icon-series-add::before{
  content:""; }

.bp3-icon-series-configuration::before{
  content:""; }

.bp3-icon-series-derived::before{
  content:""; }

.bp3-icon-series-filtered::before{
  content:""; }

.bp3-icon-series-search::before{
  content:""; }

.bp3-icon-settings::before{
  content:""; }

.bp3-icon-share::before{
  content:""; }

.bp3-icon-shield::before{
  content:""; }

.bp3-icon-shop::before{
  content:""; }

.bp3-icon-shopping-cart::before{
  content:""; }

.bp3-icon-signal-search::before{
  content:""; }

.bp3-icon-sim-card::before{
  content:""; }

.bp3-icon-slash::before{
  content:""; }

.bp3-icon-small-cross::before{
  content:""; }

.bp3-icon-small-minus::before{
  content:""; }

.bp3-icon-small-plus::before{
  content:""; }

.bp3-icon-small-tick::before{
  content:""; }

.bp3-icon-snowflake::before{
  content:""; }

.bp3-icon-social-media::before{
  content:""; }

.bp3-icon-sort::before{
  content:""; }

.bp3-icon-sort-alphabetical::before{
  content:""; }

.bp3-icon-sort-alphabetical-desc::before{
  content:""; }

.bp3-icon-sort-asc::before{
  content:""; }

.bp3-icon-sort-desc::before{
  content:""; }

.bp3-icon-sort-numerical::before{
  content:""; }

.bp3-icon-sort-numerical-desc::before{
  content:""; }

.bp3-icon-split-columns::before{
  content:""; }

.bp3-icon-square::before{
  content:""; }

.bp3-icon-stacked-chart::before{
  content:""; }

.bp3-icon-star::before{
  content:"★"; }

.bp3-icon-star-empty::before{
  content:"☆"; }

.bp3-icon-step-backward::before{
  content:""; }

.bp3-icon-step-chart::before{
  content:""; }

.bp3-icon-step-forward::before{
  content:""; }

.bp3-icon-stop::before{
  content:""; }

.bp3-icon-stopwatch::before{
  content:""; }

.bp3-icon-strikethrough::before{
  content:""; }

.bp3-icon-style::before{
  content:""; }

.bp3-icon-swap-horizontal::before{
  content:""; }

.bp3-icon-swap-vertical::before{
  content:""; }

.bp3-icon-symbol-circle::before{
  content:""; }

.bp3-icon-symbol-cross::before{
  content:""; }

.bp3-icon-symbol-diamond::before{
  content:""; }

.bp3-icon-symbol-square::before{
  content:""; }

.bp3-icon-symbol-triangle-down::before{
  content:""; }

.bp3-icon-symbol-triangle-up::before{
  content:""; }

.bp3-icon-tag::before{
  content:""; }

.bp3-icon-take-action::before{
  content:""; }

.bp3-icon-taxi::before{
  content:""; }

.bp3-icon-text-highlight::before{
  content:""; }

.bp3-icon-th::before{
  content:""; }

.bp3-icon-th-derived::before{
  content:""; }

.bp3-icon-th-disconnect::before{
  content:""; }

.bp3-icon-th-filtered::before{
  content:""; }

.bp3-icon-th-list::before{
  content:""; }

.bp3-icon-thumbs-down::before{
  content:""; }

.bp3-icon-thumbs-up::before{
  content:""; }

.bp3-icon-tick::before{
  content:"✓"; }

.bp3-icon-tick-circle::before{
  content:""; }

.bp3-icon-time::before{
  content:"⏲"; }

.bp3-icon-timeline-area-chart::before{
  content:""; }

.bp3-icon-timeline-bar-chart::before{
  content:""; }

.bp3-icon-timeline-events::before{
  content:""; }

.bp3-icon-timeline-line-chart::before{
  content:""; }

.bp3-icon-tint::before{
  content:""; }

.bp3-icon-torch::before{
  content:""; }

.bp3-icon-tractor::before{
  content:""; }

.bp3-icon-train::before{
  content:""; }

.bp3-icon-translate::before{
  content:""; }

.bp3-icon-trash::before{
  content:""; }

.bp3-icon-tree::before{
  content:""; }

.bp3-icon-trending-down::before{
  content:""; }

.bp3-icon-trending-up::before{
  content:""; }

.bp3-icon-truck::before{
  content:""; }

.bp3-icon-two-columns::before{
  content:""; }

.bp3-icon-unarchive::before{
  content:""; }

.bp3-icon-underline::before{
  content:"⎁"; }

.bp3-icon-undo::before{
  content:"⎌"; }

.bp3-icon-ungroup-objects::before{
  content:""; }

.bp3-icon-unknown-vehicle::before{
  content:""; }

.bp3-icon-unlock::before{
  content:""; }

.bp3-icon-unpin::before{
  content:""; }

.bp3-icon-unresolve::before{
  content:""; }

.bp3-icon-updated::before{
  content:""; }

.bp3-icon-upload::before{
  content:""; }

.bp3-icon-user::before{
  content:""; }

.bp3-icon-variable::before{
  content:""; }

.bp3-icon-vertical-bar-chart-asc::before{
  content:""; }

.bp3-icon-vertical-bar-chart-desc::before{
  content:""; }

.bp3-icon-vertical-distribution::before{
  content:""; }

.bp3-icon-video::before{
  content:""; }

.bp3-icon-volume-down::before{
  content:""; }

.bp3-icon-volume-off::before{
  content:""; }

.bp3-icon-volume-up::before{
  content:""; }

.bp3-icon-walk::before{
  content:""; }

.bp3-icon-warning-sign::before{
  content:""; }

.bp3-icon-waterfall-chart::before{
  content:""; }

.bp3-icon-widget::before{
  content:""; }

.bp3-icon-widget-button::before{
  content:""; }

.bp3-icon-widget-footer::before{
  content:""; }

.bp3-icon-widget-header::before{
  content:""; }

.bp3-icon-wrench::before{
  content:""; }

.bp3-icon-zoom-in::before{
  content:""; }

.bp3-icon-zoom-out::before{
  content:""; }

.bp3-icon-zoom-to-fit::before{
  content:""; }
.bp3-submenu > .bp3-popover-wrapper{
  display:block; }

.bp3-submenu .bp3-popover-target{
  display:block; }

.bp3-submenu.bp3-popover{
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0 5px; }
  .bp3-submenu.bp3-popover > .bp3-popover-content{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-submenu.bp3-popover, .bp3-submenu.bp3-popover.bp3-dark{
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-dark .bp3-submenu.bp3-popover > .bp3-popover-content, .bp3-submenu.bp3-popover.bp3-dark > .bp3-popover-content{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
.bp3-menu{
  background:#ffffff;
  border-radius:3px;
  color:#182026;
  list-style:none;
  margin:0;
  min-width:180px;
  padding:5px;
  text-align:left; }

.bp3-menu-divider{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px; }
  .bp3-dark .bp3-menu-divider{
    border-top-color:rgba(255, 255, 255, 0.15); }

.bp3-menu-item{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  border-radius:2px;
  color:inherit;
  line-height:20px;
  padding:5px 7px;
  text-decoration:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-menu-item > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-menu-item > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-menu-item::before,
  .bp3-menu-item > *{
    margin-right:7px; }
  .bp3-menu-item:empty::before,
  .bp3-menu-item > :last-child{
    margin-right:0; }
  .bp3-menu-item > .bp3-fill{
    word-break:break-word; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    background-color:rgba(167, 182, 194, 0.3);
    cursor:pointer;
    text-decoration:none; }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-dark .bp3-menu-item{
    color:inherit; }
    .bp3-dark .bp3-menu-item:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
      background-color:rgba(138, 155, 168, 0.15);
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-disabled{
      background-color:inherit;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-menu-item.bp3-intent-primary{
    color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-primary::before, .bp3-menu-item.bp3-intent-primary::after,
    .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary:active, .bp3-menu-item.bp3-intent-primary:active::before, .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-success{
    color:#0d8050; }
    .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-success::before, .bp3-menu-item.bp3-intent-success::after,
    .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-menu-item.bp3-intent-success:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success:active, .bp3-menu-item.bp3-intent-success:active::before, .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-warning{
    color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-warning::before, .bp3-menu-item.bp3-intent-warning::after,
    .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning:active, .bp3-menu-item.bp3-intent-warning:active::before, .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-danger{
    color:#c23030; }
    .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-danger::before, .bp3-menu-item.bp3-intent-danger::after,
    .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger:active, .bp3-menu-item.bp3-intent-danger:active::before, .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    margin-right:7px; }
  .bp3-menu-item::before,
  .bp3-menu-item > .bp3-icon{
    color:#5c7080;
    margin-top:2px; }
  .bp3-menu-item .bp3-menu-item-label{
    color:#5c7080; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    color:inherit; }
  .bp3-menu-item.bp3-active, .bp3-menu-item:active{
    background-color:rgba(115, 134, 148, 0.3); }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit !important;
    color:rgba(92, 112, 128, 0.6) !important;
    cursor:not-allowed !important;
    outline:none !important; }
    .bp3-menu-item.bp3-disabled::before,
    .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-large .bp3-menu-item{
    font-size:16px;
    line-height:22px;
    padding:9px 7px; }
    .bp3-large .bp3-menu-item .bp3-icon{
      margin-top:3px; }
    .bp3-large .bp3-menu-item::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      margin-right:10px;
      margin-top:1px; }

button.bp3-menu-item{
  background:none;
  border:none;
  text-align:left;
  width:100%; }
.bp3-menu-header{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px;
  cursor:default;
  padding-left:2px; }
  .bp3-dark .bp3-menu-header{
    border-top-color:rgba(255, 255, 255, 0.15); }
  .bp3-menu-header:first-of-type{
    border-top:none; }
  .bp3-menu-header > h6{
    color:#182026;
    font-weight:600;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    line-height:17px;
    margin:0;
    padding:10px 7px 0 1px; }
    .bp3-dark .bp3-menu-header > h6{
      color:#f5f8fa; }
  .bp3-menu-header:first-of-type > h6{
    padding-top:0; }
  .bp3-large .bp3-menu-header > h6{
    font-size:18px;
    padding-bottom:5px;
    padding-top:15px; }
  .bp3-large .bp3-menu-header:first-of-type > h6{
    padding-top:0; }

.bp3-dark .bp3-menu{
  background:#30404d;
  color:#f5f8fa; }

.bp3-dark .bp3-menu-item.bp3-intent-primary{
  color:#48aff0; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary::before, .bp3-dark .bp3-menu-item.bp3-intent-primary::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
    color:#48aff0; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active{
    background-color:#137cbd; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary:active{
    background-color:#106ba3; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary:active, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item.bp3-intent-success{
  color:#3dcc91; }
  .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-success::before, .bp3-dark .bp3-menu-item.bp3-intent-success::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
    color:#3dcc91; }
  .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active{
    background-color:#0f9960; }
  .bp3-dark .bp3-menu-item.bp3-intent-success:active{
    background-color:#0d8050; }
  .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success:active, .bp3-dark .bp3-menu-item.bp3-intent-success:active::before, .bp3-dark .bp3-menu-item.bp3-intent-success:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item.bp3-intent-warning{
  color:#ffb366; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning::before, .bp3-dark .bp3-menu-item.bp3-intent-warning::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
    color:#ffb366; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active{
    background-color:#d9822b; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning:active{
    background-color:#bf7326; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning:active, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item.bp3-intent-danger{
  color:#ff7373; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger::before, .bp3-dark .bp3-menu-item.bp3-intent-danger::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
    color:#ff7373; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active{
    background-color:#db3737; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger:active{
    background-color:#c23030; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger:active, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item::before,
.bp3-dark .bp3-menu-item > .bp3-icon{
  color:#a7b6c2; }

.bp3-dark .bp3-menu-item .bp3-menu-item-label{
  color:#a7b6c2; }

.bp3-dark .bp3-menu-item.bp3-active, .bp3-dark .bp3-menu-item:active{
  background-color:rgba(138, 155, 168, 0.3); }

.bp3-dark .bp3-menu-item.bp3-disabled{
  color:rgba(167, 182, 194, 0.6) !important; }
  .bp3-dark .bp3-menu-item.bp3-disabled::before,
  .bp3-dark .bp3-menu-item.bp3-disabled > .bp3-icon,
  .bp3-dark .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
    color:rgba(167, 182, 194, 0.6) !important; }

.bp3-dark .bp3-menu-divider,
.bp3-dark .bp3-menu-header{
  border-color:rgba(255, 255, 255, 0.15); }

.bp3-dark .bp3-menu-header > h6{
  color:#f5f8fa; }

.bp3-label .bp3-menu{
  margin-top:5px; }
.bp3-navbar{
  background-color:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  height:50px;
  padding:0 15px;
  position:relative;
  width:100%;
  z-index:10; }
  .bp3-navbar.bp3-dark,
  .bp3-dark .bp3-navbar{
    background-color:#394b59; }
  .bp3-navbar.bp3-dark{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-navbar{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-navbar.bp3-fixed-top{
    left:0;
    position:fixed;
    right:0;
    top:0; }

.bp3-navbar-heading{
  font-size:16px;
  margin-right:15px; }

.bp3-navbar-group{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:50px; }
  .bp3-navbar-group.bp3-align-left{
    float:left; }
  .bp3-navbar-group.bp3-align-right{
    float:right; }

.bp3-navbar-divider{
  border-left:1px solid rgba(16, 22, 26, 0.15);
  height:20px;
  margin:0 10px; }
  .bp3-dark .bp3-navbar-divider{
    border-left-color:rgba(255, 255, 255, 0.15); }
.bp3-non-ideal-state{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  height:100%;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  text-align:center;
  width:100%; }
  .bp3-non-ideal-state > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-non-ideal-state > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-non-ideal-state::before,
  .bp3-non-ideal-state > *{
    margin-bottom:20px; }
  .bp3-non-ideal-state:empty::before,
  .bp3-non-ideal-state > :last-child{
    margin-bottom:0; }
  .bp3-non-ideal-state > *{
    max-width:400px; }

.bp3-non-ideal-state-visual{
  color:rgba(92, 112, 128, 0.6);
  font-size:60px; }
  .bp3-dark .bp3-non-ideal-state-visual{
    color:rgba(167, 182, 194, 0.6); }

.bp3-overflow-list{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:nowrap;
      flex-wrap:nowrap;
  min-width:0; }

.bp3-overflow-list-spacer{
  -ms-flex-negative:1;
      flex-shrink:1;
  width:1px; }

body.bp3-overlay-open{
  overflow:hidden; }

.bp3-overlay{
  bottom:0;
  left:0;
  position:static;
  right:0;
  top:0;
  z-index:20; }
  .bp3-overlay:not(.bp3-overlay-open){
    pointer-events:none; }
  .bp3-overlay.bp3-overlay-container{
    overflow:hidden;
    position:fixed; }
    .bp3-overlay.bp3-overlay-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-scroll-container{
    overflow:auto;
    position:fixed; }
    .bp3-overlay.bp3-overlay-scroll-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-inline{
    display:inline;
    overflow:visible; }

.bp3-overlay-content{
  position:fixed;
  z-index:20; }
  .bp3-overlay-inline .bp3-overlay-content,
  .bp3-overlay-scroll-container .bp3-overlay-content{
    position:absolute; }

.bp3-overlay-backdrop{
  bottom:0;
  left:0;
  position:fixed;
  right:0;
  top:0;
  opacity:1;
  background-color:rgba(16, 22, 26, 0.7);
  overflow:auto;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  z-index:20; }
  .bp3-overlay-backdrop.bp3-overlay-enter, .bp3-overlay-backdrop.bp3-overlay-appear{
    opacity:0; }
  .bp3-overlay-backdrop.bp3-overlay-enter-active, .bp3-overlay-backdrop.bp3-overlay-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop.bp3-overlay-exit{
    opacity:1; }
  .bp3-overlay-backdrop.bp3-overlay-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop:focus{
    outline:none; }
  .bp3-overlay-inline .bp3-overlay-backdrop{
    position:absolute; }
.bp3-panel-stack{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-view{
    background-color:#30404d; }
  .bp3-panel-stack-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack-push .bp3-panel-stack-enter, .bp3-panel-stack-push .bp3-panel-stack-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack-push .bp3-panel-stack-enter-active, .bp3-panel-stack-push .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-push .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-push .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-enter, .bp3-panel-stack-pop .bp3-panel-stack-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack-pop .bp3-panel-stack-enter-active, .bp3-panel-stack-pop .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-pop .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-popover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1);
  border-radius:3px;
  display:inline-block;
  z-index:20; }
  .bp3-popover .bp3-popover-arrow{
    height:30px;
    position:absolute;
    width:30px; }
    .bp3-popover .bp3-popover-arrow::before{
      height:20px;
      margin:5px;
      width:20px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover{
    margin-bottom:17px;
    margin-top:-17px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
      bottom:-11px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover{
    margin-left:17px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
      left:-11px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover{
    margin-top:17px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
      top:-11px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover{
    margin-left:-17px;
    margin-right:17px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
      right:-11px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-popover > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-popover > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
    top:-0.3934px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
    right:-0.3934px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
    left:-0.3934px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
    bottom:-0.3934px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-popover .bp3-popover-content{
    background:#ffffff;
    color:inherit; }
  .bp3-popover .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-popover .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-popover .bp3-popover-arrow-fill{
    fill:#ffffff; }
  .bp3-popover-enter > .bp3-popover, .bp3-popover-appear > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3); }
  .bp3-popover-enter-active > .bp3-popover, .bp3-popover-appear-active > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover-exit > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover .bp3-popover-content{
    border-radius:3px;
    position:relative; }
  .bp3-popover.bp3-popover-content-sizing .bp3-popover-content{
    max-width:350px;
    padding:20px; }
  .bp3-popover-target + .bp3-overlay .bp3-popover.bp3-popover-content-sizing{
    width:350px; }
  .bp3-popover.bp3-minimal{
    margin:0 !important; }
    .bp3-popover.bp3-minimal .bp3-popover-arrow{
      display:none; }
    .bp3-popover.bp3-minimal.bp3-popover{
      -webkit-transform:scale(1);
              transform:scale(1); }
      .bp3-popover-enter > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-enter-active > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
      .bp3-popover-exit > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-exit-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover.bp3-dark,
  .bp3-dark .bp3-popover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-popover .bp3-popover-content{
      background:#30404d;
      color:inherit; }
    .bp3-popover.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-popover .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-popover .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-popover.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-popover .bp3-popover-arrow-fill{
      fill:#30404d; }

.bp3-popover-arrow::before{
  border-radius:2px;
  content:"";
  display:block;
  position:absolute;
  -webkit-transform:rotate(45deg);
          transform:rotate(45deg); }

.bp3-tether-pinned .bp3-popover-arrow{
  display:none; }

.bp3-popover-backdrop{
  background:rgba(255, 255, 255, 0); }

.bp3-transition-container{
  opacity:1;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  z-index:20; }
  .bp3-transition-container.bp3-popover-enter, .bp3-transition-container.bp3-popover-appear{
    opacity:0; }
  .bp3-transition-container.bp3-popover-enter-active, .bp3-transition-container.bp3-popover-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container.bp3-popover-exit{
    opacity:1; }
  .bp3-transition-container.bp3-popover-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container:focus{
    outline:none; }
  .bp3-transition-container.bp3-popover-leave .bp3-popover-content{
    pointer-events:none; }
  .bp3-transition-container[data-x-out-of-boundaries]{
    display:none; }

span.bp3-popover-target{
  display:inline-block; }

.bp3-popover-wrapper.bp3-fill{
  width:100%; }

.bp3-portal{
  left:0;
  position:absolute;
  right:0;
  top:0; }
@-webkit-keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }
@keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }

.bp3-progress-bar{
  background:rgba(92, 112, 128, 0.2);
  border-radius:40px;
  display:block;
  height:8px;
  overflow:hidden;
  position:relative;
  width:100%; }
  .bp3-progress-bar .bp3-progress-meter{
    background:linear-gradient(-45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%);
    background-color:rgba(92, 112, 128, 0.8);
    background-size:30px 30px;
    border-radius:40px;
    height:100%;
    position:absolute;
    -webkit-transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:100%; }
  .bp3-progress-bar:not(.bp3-no-animation):not(.bp3-no-stripes) .bp3-progress-meter{
    animation:linear-progress-bar-stripes 300ms linear infinite reverse; }
  .bp3-progress-bar.bp3-no-stripes .bp3-progress-meter{
    background-image:none; }

.bp3-dark .bp3-progress-bar{
  background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-progress-bar .bp3-progress-meter{
    background-color:#8a9ba8; }

.bp3-progress-bar.bp3-intent-primary .bp3-progress-meter{
  background-color:#137cbd; }

.bp3-progress-bar.bp3-intent-success .bp3-progress-meter{
  background-color:#0f9960; }

.bp3-progress-bar.bp3-intent-warning .bp3-progress-meter{
  background-color:#d9822b; }

.bp3-progress-bar.bp3-intent-danger .bp3-progress-meter{
  background-color:#db3737; }
@-webkit-keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
@keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
.bp3-skeleton{
  -webkit-animation:1000ms linear infinite alternate skeleton-glow;
          animation:1000ms linear infinite alternate skeleton-glow;
  background:rgba(206, 217, 224, 0.2);
  background-clip:padding-box !important;
  border-color:rgba(206, 217, 224, 0.2) !important;
  border-radius:2px;
  -webkit-box-shadow:none !important;
          box-shadow:none !important;
  color:transparent !important;
  cursor:default;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-skeleton::before, .bp3-skeleton::after,
  .bp3-skeleton *{
    visibility:hidden !important; }
.bp3-slider{
  height:40px;
  min-width:150px;
  width:100%;
  cursor:default;
  outline:none;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-slider:hover{
    cursor:pointer; }
  .bp3-slider:active{
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-slider.bp3-disabled{
    cursor:not-allowed;
    opacity:0.5; }
  .bp3-slider.bp3-slider-unlabeled{
    height:16px; }

.bp3-slider-track,
.bp3-slider-progress{
  height:6px;
  left:0;
  right:0;
  top:5px;
  position:absolute; }

.bp3-slider-track{
  border-radius:3px;
  overflow:hidden; }

.bp3-slider-progress{
  background:rgba(92, 112, 128, 0.2); }
  .bp3-dark .bp3-slider-progress{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-slider-progress.bp3-intent-primary{
    background-color:#137cbd; }
  .bp3-slider-progress.bp3-intent-success{
    background-color:#0f9960; }
  .bp3-slider-progress.bp3-intent-warning{
    background-color:#d9822b; }
  .bp3-slider-progress.bp3-intent-danger{
    background-color:#db3737; }

.bp3-slider-handle{
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
  cursor:pointer;
  height:16px;
  left:0;
  position:absolute;
  top:0;
  width:16px; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-slider-handle:active, .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-slider-handle:disabled, .bp3-slider-handle.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-slider-handle:disabled.bp3-active, .bp3-slider-handle:disabled.bp3-active:hover, .bp3-slider-handle.bp3-disabled.bp3-active, .bp3-slider-handle.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }
  .bp3-slider-handle:focus{
    z-index:1; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
    cursor:-webkit-grab;
    cursor:grab;
    z-index:2; }
  .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-disabled .bp3-slider-handle{
    background:#bfccd6;
    -webkit-box-shadow:none;
            box-shadow:none;
    pointer-events:none; }
  .bp3-dark .bp3-slider-handle{
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover, .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-slider-handle:disabled, .bp3-dark .bp3-slider-handle.bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-slider-handle:disabled.bp3-active, .bp3-dark .bp3-slider-handle.bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-slider-handle .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-slider-handle, .bp3-dark .bp3-slider-handle:hover{
      background-color:#394b59; }
    .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#293742; }
  .bp3-dark .bp3-disabled .bp3-slider-handle{
    background:#5c7080;
    border-color:#5c7080;
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-slider-handle .bp3-slider-label{
    background:#394b59;
    border-radius:3px;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
    color:#f5f8fa;
    margin-left:8px; }
    .bp3-dark .bp3-slider-handle .bp3-slider-label{
      background:#e1e8ed;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
      color:#394b59; }
    .bp3-disabled .bp3-slider-handle .bp3-slider-label{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-slider-handle.bp3-start, .bp3-slider-handle.bp3-end{
    width:8px; }
  .bp3-slider-handle.bp3-start{
    border-bottom-right-radius:0;
    border-top-right-radius:0; }
  .bp3-slider-handle.bp3-end{
    border-bottom-left-radius:0;
    border-top-left-radius:0;
    margin-left:8px; }
    .bp3-slider-handle.bp3-end .bp3-slider-label{
      margin-left:0; }

.bp3-slider-label{
  -webkit-transform:translate(-50%, 20px);
          transform:translate(-50%, 20px);
  display:inline-block;
  font-size:12px;
  line-height:1;
  padding:2px 5px;
  position:absolute;
  vertical-align:top; }

.bp3-slider.bp3-vertical{
  height:150px;
  min-width:40px;
  width:40px; }
  .bp3-slider.bp3-vertical .bp3-slider-track,
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    bottom:0;
    height:auto;
    left:5px;
    top:0;
    width:6px; }
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    top:auto; }
  .bp3-slider.bp3-vertical .bp3-slider-label{
    -webkit-transform:translate(20px, 50%);
            transform:translate(20px, 50%); }
  .bp3-slider.bp3-vertical .bp3-slider-handle{
    top:auto; }
    .bp3-slider.bp3-vertical .bp3-slider-handle .bp3-slider-label{
      margin-left:0;
      margin-top:-8px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end, .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      height:8px;
      margin-left:0;
      width:16px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      border-bottom-right-radius:3px;
      border-top-left-radius:0; }
      .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start .bp3-slider-label{
        -webkit-transform:translate(20px);
                transform:translate(20px); }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end{
      border-bottom-left-radius:0;
      border-bottom-right-radius:0;
      border-top-left-radius:3px;
      margin-bottom:8px; }

@-webkit-keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

@keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

.bp3-spinner{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  overflow:visible;
  vertical-align:middle; }
  .bp3-spinner svg{
    display:block; }
  .bp3-spinner path{
    fill-opacity:0; }
  .bp3-spinner .bp3-spinner-head{
    stroke:rgba(92, 112, 128, 0.8);
    stroke-linecap:round;
    -webkit-transform-origin:center;
            transform-origin:center;
    -webkit-transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-spinner .bp3-spinner-track{
    stroke:rgba(92, 112, 128, 0.2); }

.bp3-spinner-animation{
  -webkit-animation:pt-spinner-animation 500ms linear infinite;
          animation:pt-spinner-animation 500ms linear infinite; }
  .bp3-no-spin > .bp3-spinner-animation{
    -webkit-animation:none;
            animation:none; }

.bp3-dark .bp3-spinner .bp3-spinner-head{
  stroke:#8a9ba8; }

.bp3-dark .bp3-spinner .bp3-spinner-track{
  stroke:rgba(16, 22, 26, 0.5); }

.bp3-spinner.bp3-intent-primary .bp3-spinner-head{
  stroke:#137cbd; }

.bp3-spinner.bp3-intent-success .bp3-spinner-head{
  stroke:#0f9960; }

.bp3-spinner.bp3-intent-warning .bp3-spinner-head{
  stroke:#d9822b; }

.bp3-spinner.bp3-intent-danger .bp3-spinner-head{
  stroke:#db3737; }
.bp3-tabs.bp3-vertical{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-tabs.bp3-vertical > .bp3-tab-list{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab{
      border-radius:3px;
      padding:0 10px;
      width:100%; }
      .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab[aria-selected="true"]{
        background-color:rgba(19, 124, 189, 0.2);
        -webkit-box-shadow:none;
                box-shadow:none; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab-indicator-wrapper .bp3-tab-indicator{
      background-color:rgba(19, 124, 189, 0.2);
      border-radius:3px;
      bottom:0;
      height:auto;
      left:0;
      right:0;
      top:0; }
  .bp3-tabs.bp3-vertical > .bp3-tab-panel{
    margin-top:0;
    padding-left:20px; }

.bp3-tab-list{
  -webkit-box-align:end;
      -ms-flex-align:end;
          align-items:flex-end;
  border:none;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  list-style:none;
  margin:0;
  padding:0;
  position:relative; }
  .bp3-tab-list > *:not(:last-child){
    margin-right:20px; }

.bp3-tab{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:#182026;
  cursor:pointer;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  font-size:14px;
  line-height:30px;
  max-width:100%;
  position:relative;
  vertical-align:top; }
  .bp3-tab a{
    color:inherit;
    display:block;
    text-decoration:none; }
  .bp3-tab-indicator-wrapper ~ .bp3-tab{
    background-color:transparent !important;
    -webkit-box-shadow:none !important;
            box-shadow:none !important; }
  .bp3-tab[aria-disabled="true"]{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-tab[aria-selected="true"]{
    border-radius:0;
    -webkit-box-shadow:inset 0 -3px 0 #106ba3;
            box-shadow:inset 0 -3px 0 #106ba3; }
  .bp3-tab[aria-selected="true"], .bp3-tab:not([aria-disabled="true"]):hover{
    color:#106ba3; }
  .bp3-tab:focus{
    -moz-outline-radius:0; }
  .bp3-large > .bp3-tab{
    font-size:16px;
    line-height:40px; }

.bp3-tab-panel{
  margin-top:20px; }
  .bp3-tab-panel[aria-hidden="true"]{
    display:none; }

.bp3-tab-indicator-wrapper{
  left:0;
  pointer-events:none;
  position:absolute;
  top:0;
  -webkit-transform:translateX(0), translateY(0);
          transform:translateX(0), translateY(0);
  -webkit-transition:height, width, -webkit-transform;
  transition:height, width, -webkit-transform;
  transition:height, transform, width;
  transition:height, transform, width, -webkit-transform;
  -webkit-transition-duration:200ms;
          transition-duration:200ms;
  -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
          transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tab-indicator-wrapper .bp3-tab-indicator{
    background-color:#106ba3;
    bottom:0;
    height:3px;
    left:0;
    position:absolute;
    right:0; }
  .bp3-tab-indicator-wrapper.bp3-no-animation{
    -webkit-transition:none;
    transition:none; }

.bp3-dark .bp3-tab{
  color:#f5f8fa; }
  .bp3-dark .bp3-tab[aria-disabled="true"]{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tab[aria-selected="true"]{
    -webkit-box-shadow:inset 0 -3px 0 #48aff0;
            box-shadow:inset 0 -3px 0 #48aff0; }
  .bp3-dark .bp3-tab[aria-selected="true"], .bp3-dark .bp3-tab:not([aria-disabled="true"]):hover{
    color:#48aff0; }

.bp3-dark .bp3-tab-indicator{
  background-color:#48aff0; }

.bp3-flex-expander{
  -webkit-box-flex:1;
      -ms-flex:1 1;
          flex:1 1; }
.bp3-tag{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#5c7080;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:none;
          box-shadow:none;
  color:#f5f8fa;
  font-size:12px;
  line-height:16px;
  max-width:100%;
  min-height:20px;
  min-width:20px;
  padding:2px 6px;
  position:relative; }
  .bp3-tag.bp3-interactive{
    cursor:pointer; }
    .bp3-tag.bp3-interactive:hover{
      background-color:rgba(92, 112, 128, 0.85); }
    .bp3-tag.bp3-interactive.bp3-active, .bp3-tag.bp3-interactive:active{
      background-color:rgba(92, 112, 128, 0.7); }
  .bp3-tag > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag::before,
  .bp3-tag > *{
    margin-right:4px; }
  .bp3-tag:empty::before,
  .bp3-tag > :last-child{
    margin-right:0; }
  .bp3-tag:focus{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:0;
    -moz-outline-radius:6px; }
  .bp3-tag.bp3-round{
    border-radius:30px;
    padding-left:8px;
    padding-right:8px; }
  .bp3-dark .bp3-tag{
    background-color:#bfccd6;
    color:#182026; }
    .bp3-dark .bp3-tag.bp3-interactive{
      cursor:pointer; }
      .bp3-dark .bp3-tag.bp3-interactive:hover{
        background-color:rgba(191, 204, 214, 0.85); }
      .bp3-dark .bp3-tag.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-interactive:active{
        background-color:rgba(191, 204, 214, 0.7); }
    .bp3-dark .bp3-tag > .bp3-icon, .bp3-dark .bp3-tag .bp3-icon-standard, .bp3-dark .bp3-tag .bp3-icon-large{
      fill:currentColor; }
  .bp3-tag > .bp3-icon, .bp3-tag .bp3-icon-standard, .bp3-tag .bp3-icon-large{
    fill:#ffffff; }
  .bp3-tag.bp3-large,
  .bp3-large .bp3-tag{
    font-size:14px;
    line-height:20px;
    min-height:30px;
    min-width:30px;
    padding:5px 10px; }
    .bp3-tag.bp3-large::before,
    .bp3-tag.bp3-large > *,
    .bp3-large .bp3-tag::before,
    .bp3-large .bp3-tag > *{
      margin-right:7px; }
    .bp3-tag.bp3-large:empty::before,
    .bp3-tag.bp3-large > :last-child,
    .bp3-large .bp3-tag:empty::before,
    .bp3-large .bp3-tag > :last-child{
      margin-right:0; }
    .bp3-tag.bp3-large.bp3-round,
    .bp3-large .bp3-tag.bp3-round{
      padding-left:12px;
      padding-right:12px; }
  .bp3-tag.bp3-intent-primary{
    background:#137cbd;
    color:#ffffff; }
    .bp3-tag.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.85); }
      .bp3-tag.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.7); }
  .bp3-tag.bp3-intent-success{
    background:#0f9960;
    color:#ffffff; }
    .bp3-tag.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.85); }
      .bp3-tag.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.7); }
  .bp3-tag.bp3-intent-warning{
    background:#d9822b;
    color:#ffffff; }
    .bp3-tag.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.85); }
      .bp3-tag.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.7); }
  .bp3-tag.bp3-intent-danger{
    background:#db3737;
    color:#ffffff; }
    .bp3-tag.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.85); }
      .bp3-tag.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.7); }
  .bp3-tag.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-tag.bp3-minimal > .bp3-icon, .bp3-tag.bp3-minimal .bp3-icon-standard, .bp3-tag.bp3-minimal .bp3-icon-large{
    fill:#5c7080; }
  .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
    background-color:rgba(138, 155, 168, 0.2);
    color:#182026; }
    .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
        background-color:rgba(92, 112, 128, 0.3); }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
        background-color:rgba(92, 112, 128, 0.4); }
    .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
      color:#f5f8fa; }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
          background-color:rgba(191, 204, 214, 0.3); }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
          background-color:rgba(191, 204, 214, 0.4); }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) > .bp3-icon, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-large{
        fill:#a7b6c2; }
  .bp3-tag.bp3-minimal.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15);
    color:#106ba3; }
    .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-primary > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-large{
      fill:#137cbd; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25);
      color:#48aff0; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
          background-color:rgba(19, 124, 189, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
          background-color:rgba(19, 124, 189, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15);
    color:#0d8050; }
    .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-success > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-large{
      fill:#0f9960; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25);
      color:#3dcc91; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
          background-color:rgba(15, 153, 96, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
          background-color:rgba(15, 153, 96, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15);
    color:#bf7326; }
    .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-warning > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-large{
      fill:#d9822b; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25);
      color:#ffb366; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
          background-color:rgba(217, 130, 43, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
          background-color:rgba(217, 130, 43, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15);
    color:#c23030; }
    .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-danger > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-large{
      fill:#db3737; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25);
      color:#ff7373; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
          background-color:rgba(219, 55, 55, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
          background-color:rgba(219, 55, 55, 0.45); }

.bp3-tag-remove{
  background:none;
  border:none;
  color:inherit;
  cursor:pointer;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin-bottom:-2px;
  margin-right:-6px !important;
  margin-top:-2px;
  opacity:0.5;
  padding:2px;
  padding-left:0; }
  .bp3-tag-remove:hover{
    background:none;
    opacity:0.8;
    text-decoration:none; }
  .bp3-tag-remove:active{
    opacity:1; }
  .bp3-tag-remove:empty::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    content:""; }
  .bp3-large .bp3-tag-remove{
    margin-right:-10px !important;
    padding:5px;
    padding-left:0; }
    .bp3-large .bp3-tag-remove:empty::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1; }
.bp3-tag-input{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  cursor:text;
  height:auto;
  line-height:inherit;
  min-height:30px;
  padding-left:5px;
  padding-right:0; }
  .bp3-tag-input > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag-input > .bp3-tag-input-values{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag-input .bp3-tag-input-icon{
    color:#5c7080;
    margin-left:2px;
    margin-right:7px;
    margin-top:7px; }
  .bp3-tag-input .bp3-tag-input-values{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    -ms-flex-item-align:stretch;
        align-self:stretch;
    -ms-flex-wrap:wrap;
        flex-wrap:wrap;
    margin-right:7px;
    margin-top:5px;
    min-width:0; }
    .bp3-tag-input .bp3-tag-input-values > *{
      -webkit-box-flex:0;
          -ms-flex-positive:0;
              flex-grow:0;
      -ms-flex-negative:0;
          flex-shrink:0; }
    .bp3-tag-input .bp3-tag-input-values > .bp3-fill{
      -webkit-box-flex:1;
          -ms-flex-positive:1;
              flex-grow:1;
      -ms-flex-negative:1;
          flex-shrink:1; }
    .bp3-tag-input .bp3-tag-input-values::before,
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-right:5px; }
    .bp3-tag-input .bp3-tag-input-values:empty::before,
    .bp3-tag-input .bp3-tag-input-values > :last-child{
      margin-right:0; }
    .bp3-tag-input .bp3-tag-input-values:first-child .bp3-input-ghost:first-child{
      padding-left:5px; }
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-bottom:5px; }
  .bp3-tag-input .bp3-tag{
    overflow-wrap:break-word; }
    .bp3-tag-input .bp3-tag.bp3-active{
      outline:rgba(19, 124, 189, 0.6) auto 2px;
      outline-offset:0;
      -moz-outline-radius:6px; }
  .bp3-tag-input .bp3-input-ghost{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:20px;
    width:80px; }
    .bp3-tag-input .bp3-input-ghost:disabled, .bp3-tag-input .bp3-input-ghost.bp3-disabled{
      cursor:not-allowed; }
  .bp3-tag-input .bp3-button,
  .bp3-tag-input .bp3-spinner{
    margin:3px;
    margin-left:0; }
  .bp3-tag-input .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-tag-input.bp3-large{
    height:auto;
    min-height:40px; }
    .bp3-tag-input.bp3-large::before,
    .bp3-tag-input.bp3-large > *{
      margin-right:10px; }
    .bp3-tag-input.bp3-large:empty::before,
    .bp3-tag-input.bp3-large > :last-child{
      margin-right:0; }
    .bp3-tag-input.bp3-large .bp3-tag-input-icon{
      margin-left:5px;
      margin-top:10px; }
    .bp3-tag-input.bp3-large .bp3-input-ghost{
      line-height:30px; }
    .bp3-tag-input.bp3-large .bp3-button{
      min-height:30px;
      min-width:30px;
      padding:5px 10px;
      margin:5px;
      margin-left:0; }
    .bp3-tag-input.bp3-large .bp3-spinner{
      margin:8px;
      margin-left:0; }
  .bp3-tag-input.bp3-active{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-tag-input .bp3-tag-input-icon, .bp3-tag-input.bp3-dark .bp3-tag-input-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-tag-input .bp3-input-ghost, .bp3-tag-input.bp3-dark .bp3-input-ghost{
    color:#f5f8fa; }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-webkit-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-moz-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost:-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::placeholder{
      color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tag-input.bp3-active, .bp3-tag-input.bp3-dark.bp3-active{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-primary, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-success, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-warning, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-danger, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-input-ghost{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0; }
  .bp3-input-ghost::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:focus{
    outline:none !important; }
.bp3-toast{
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:20px 0 0;
  max-width:500px;
  min-width:300px;
  pointer-events:all;
  position:relative !important; }
  .bp3-toast.bp3-toast-enter, .bp3-toast.bp3-toast-appear{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active, .bp3-toast.bp3-toast-appear-active{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-enter ~ .bp3-toast, .bp3-toast.bp3-toast-appear ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active ~ .bp3-toast, .bp3-toast.bp3-toast-appear-active ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-exit{
    opacity:1;
    -webkit-filter:blur(0);
            filter:blur(0); }
  .bp3-toast.bp3-toast-exit-active{
    opacity:0;
    -webkit-filter:blur(10px);
            filter:blur(10px);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:opacity, filter;
    transition-property:opacity, filter, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast.bp3-toast-exit ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0); }
  .bp3-toast.bp3-toast-exit-active ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px);
    -webkit-transition-delay:50ms;
            transition-delay:50ms;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast .bp3-button-group{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    padding:5px;
    padding-left:0; }
  .bp3-toast > .bp3-icon{
    color:#5c7080;
    margin:12px;
    margin-right:0; }
  .bp3-toast.bp3-dark,
  .bp3-dark .bp3-toast{
    background-color:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-toast.bp3-dark > .bp3-icon,
    .bp3-dark .bp3-toast > .bp3-icon{
      color:#a7b6c2; }
  .bp3-toast[class*="bp3-intent-"] a{
    color:rgba(255, 255, 255, 0.7); }
    .bp3-toast[class*="bp3-intent-"] a:hover{
      color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] > .bp3-icon{
    color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button, .bp3-toast[class*="bp3-intent-"] .bp3-button::before,
  .bp3-toast[class*="bp3-intent-"] .bp3-button .bp3-icon, .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    color:rgba(255, 255, 255, 0.7) !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:focus{
    outline-color:rgba(255, 255, 255, 0.5); }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:hover{
    background-color:rgba(255, 255, 255, 0.15) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    background-color:rgba(255, 255, 255, 0.3) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button::after{
    background:rgba(255, 255, 255, 0.3) !important; }
  .bp3-toast.bp3-intent-primary{
    background-color:#137cbd;
    color:#ffffff; }
  .bp3-toast.bp3-intent-success{
    background-color:#0f9960;
    color:#ffffff; }
  .bp3-toast.bp3-intent-warning{
    background-color:#d9822b;
    color:#ffffff; }
  .bp3-toast.bp3-intent-danger{
    background-color:#db3737;
    color:#ffffff; }

.bp3-toast-message{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  padding:11px;
  word-break:break-word; }

.bp3-toast-container{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box !important;
  display:-ms-flexbox !important;
  display:flex !important;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  left:0;
  overflow:hidden;
  padding:0 20px 20px;
  pointer-events:none;
  position:fixed;
  right:0;
  z-index:40; }
  .bp3-toast-container.bp3-toast-container-top{
    top:0; }
  .bp3-toast-container.bp3-toast-container-bottom{
    bottom:0;
    -webkit-box-orient:vertical;
    -webkit-box-direction:reverse;
        -ms-flex-direction:column-reverse;
            flex-direction:column-reverse;
    top:auto; }
  .bp3-toast-container.bp3-toast-container-left{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
  .bp3-toast-container.bp3-toast-container-right{
    -webkit-box-align:end;
        -ms-flex-align:end;
            align-items:flex-end; }

.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active) ~ .bp3-toast, .bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active) ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-exit-active ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-leave-active ~ .bp3-toast{
  -webkit-transform:translateY(60px);
          transform:translateY(60px); }
.bp3-tooltip{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1); }
  .bp3-tooltip .bp3-popover-arrow{
    height:22px;
    position:absolute;
    width:22px; }
    .bp3-tooltip .bp3-popover-arrow::before{
      height:14px;
      margin:4px;
      width:14px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip{
    margin-bottom:11px;
    margin-top:-11px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
      bottom:-8px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip{
    margin-left:11px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
      left:-8px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip{
    margin-top:11px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
      top:-8px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip{
    margin-left:-11px;
    margin-right:11px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
      right:-8px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-tooltip > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-tooltip > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
    top:-0.22183px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
    right:-0.22183px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
    left:-0.22183px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
    bottom:-0.22183px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-tooltip .bp3-popover-content{
    background:#394b59;
    color:#f5f8fa; }
  .bp3-tooltip .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-tooltip .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-tooltip .bp3-popover-arrow-fill{
    fill:#394b59; }
  .bp3-popover-enter > .bp3-tooltip, .bp3-popover-appear > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8); }
  .bp3-popover-enter-active > .bp3-tooltip, .bp3-popover-appear-active > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover-exit > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tooltip .bp3-popover-content{
    padding:10px 12px; }
  .bp3-tooltip.bp3-dark,
  .bp3-dark .bp3-tooltip{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-tooltip .bp3-popover-content{
      background:#e1e8ed;
      color:#394b59; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-fill{
      fill:#e1e8ed; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-content{
    background:#137cbd;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-arrow-fill{
    fill:#137cbd; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-content{
    background:#0f9960;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-arrow-fill{
    fill:#0f9960; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-content{
    background:#d9822b;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-arrow-fill{
    fill:#d9822b; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-content{
    background:#db3737;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-arrow-fill{
    fill:#db3737; }

.bp3-tooltip-indicator{
  border-bottom:dotted 1px;
  cursor:help; }
.bp3-tree .bp3-icon, .bp3-tree .bp3-icon-standard, .bp3-tree .bp3-icon-large{
  color:#5c7080; }
  .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-tree .bp3-icon.bp3-intent-success, .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-tree-node-list{
  list-style:none;
  margin:0;
  padding-left:0; }

.bp3-tree-root{
  background-color:transparent;
  cursor:default;
  padding-left:0;
  position:relative; }

.bp3-tree-node-content-0{
  padding-left:0px; }

.bp3-tree-node-content-1{
  padding-left:23px; }

.bp3-tree-node-content-2{
  padding-left:46px; }

.bp3-tree-node-content-3{
  padding-left:69px; }

.bp3-tree-node-content-4{
  padding-left:92px; }

.bp3-tree-node-content-5{
  padding-left:115px; }

.bp3-tree-node-content-6{
  padding-left:138px; }

.bp3-tree-node-content-7{
  padding-left:161px; }

.bp3-tree-node-content-8{
  padding-left:184px; }

.bp3-tree-node-content-9{
  padding-left:207px; }

.bp3-tree-node-content-10{
  padding-left:230px; }

.bp3-tree-node-content-11{
  padding-left:253px; }

.bp3-tree-node-content-12{
  padding-left:276px; }

.bp3-tree-node-content-13{
  padding-left:299px; }

.bp3-tree-node-content-14{
  padding-left:322px; }

.bp3-tree-node-content-15{
  padding-left:345px; }

.bp3-tree-node-content-16{
  padding-left:368px; }

.bp3-tree-node-content-17{
  padding-left:391px; }

.bp3-tree-node-content-18{
  padding-left:414px; }

.bp3-tree-node-content-19{
  padding-left:437px; }

.bp3-tree-node-content-20{
  padding-left:460px; }

.bp3-tree-node-content{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:30px;
  padding-right:5px;
  width:100%; }
  .bp3-tree-node-content:hover{
    background-color:rgba(191, 204, 214, 0.4); }

.bp3-tree-node-caret,
.bp3-tree-node-caret-none{
  min-width:30px; }

.bp3-tree-node-caret{
  color:#5c7080;
  cursor:pointer;
  padding:7px;
  -webkit-transform:rotate(0deg);
          transform:rotate(0deg);
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tree-node-caret:hover{
    color:#182026; }
  .bp3-dark .bp3-tree-node-caret{
    color:#a7b6c2; }
    .bp3-dark .bp3-tree-node-caret:hover{
      color:#f5f8fa; }
  .bp3-tree-node-caret.bp3-tree-node-caret-open{
    -webkit-transform:rotate(90deg);
            transform:rotate(90deg); }
  .bp3-tree-node-caret.bp3-icon-standard::before{
    content:""; }

.bp3-tree-node-icon{
  margin-right:7px;
  position:relative; }

.bp3-tree-node-label{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-label span{
    display:inline; }

.bp3-tree-node-secondary-label{
  padding:0 5px;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-secondary-label .bp3-popover-wrapper,
  .bp3-tree-node-secondary-label .bp3-popover-target{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-content{
  background-color:inherit;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-caret,
.bp3-tree-node.bp3-disabled .bp3-tree-node-icon{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content,
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-standard, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-large{
    color:#ffffff; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret::before{
    color:rgba(255, 255, 255, 0.7); }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret:hover::before{
    color:#ffffff; }

.bp3-dark .bp3-tree-node-content:hover{
  background-color:rgba(92, 112, 128, 0.3); }

.bp3-dark .bp3-tree .bp3-icon, .bp3-dark .bp3-tree .bp3-icon-standard, .bp3-dark .bp3-tree .bp3-icon-large{
  color:#a7b6c2; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-dark .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }</style><style>.bp3-omnibar{
  -webkit-filter:blur(0);
          filter:blur(0);
  opacity:1;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  left:calc(50% - 250px);
  top:20vh;
  width:500px;
  z-index:21; }
  .bp3-omnibar.bp3-overlay-enter, .bp3-omnibar.bp3-overlay-appear{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2; }
  .bp3-omnibar.bp3-overlay-enter-active, .bp3-omnibar.bp3-overlay-appear-active{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar.bp3-overlay-exit{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1; }
  .bp3-omnibar.bp3-overlay-exit-active{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar .bp3-input{
    background-color:transparent;
    border-radius:0; }
    .bp3-omnibar .bp3-input, .bp3-omnibar .bp3-input:focus{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-omnibar .bp3-menu{
    background-color:transparent;
    border-radius:0;
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
    max-height:calc(60vh - 40px);
    overflow:auto; }
    .bp3-omnibar .bp3-menu:empty{
      display:none; }
  .bp3-dark .bp3-omnibar, .bp3-omnibar.bp3-dark{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-omnibar-overlay .bp3-overlay-backdrop{
  background-color:rgba(16, 22, 26, 0.2); }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }

.bp3-multi-select{
  min-width:150px; }

.bp3-multi-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto; }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-bug: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M20 8h-2.81c-.45-.78-1.07-1.45-1.82-1.96L17 4.41 15.59 3l-2.17 2.17C12.96 5.06 12.49 5 12 5c-.49 0-.96.06-1.41.17L8.41 3 7 4.41l1.62 1.63C7.88 6.55 7.26 7.22 6.81 8H4v2h2.09c-.05.33-.09.66-.09 1v1H4v2h2v1c0 .34.04.67.09 1H4v2h2.81c1.04 1.79 2.97 3 5.19 3s4.15-1.21 5.19-3H20v-2h-2.09c.05-.33.09-.66.09-1v-1h2v-2h-2v-1c0-.34-.04-.67-.09-1H20V8zm-6 8h-4v-2h4v2zm0-4h-4v-2h4v2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-build: url("data:image/svg+xml,%3Csvg width='16' viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M14.9 17.45C16.25 17.45 17.35 16.35 17.35 15C17.35 13.65 16.25 12.55 14.9 12.55C13.54 12.55 12.45 13.65 12.45 15C12.45 16.35 13.54 17.45 14.9 17.45ZM20.1 15.68L21.58 16.84C21.71 16.95 21.75 17.13 21.66 17.29L20.26 19.71C20.17 19.86 20 19.92 19.83 19.86L18.09 19.16C17.73 19.44 17.33 19.67 16.91 19.85L16.64 21.7C16.62 21.87 16.47 22 16.3 22H13.5C13.32 22 13.18 21.87 13.15 21.7L12.89 19.85C12.46 19.67 12.07 19.44 11.71 19.16L9.96002 19.86C9.81002 19.92 9.62002 19.86 9.54002 19.71L8.14002 17.29C8.05002 17.13 8.09002 16.95 8.22002 16.84L9.70002 15.68L9.65001 15L9.70002 14.31L8.22002 13.16C8.09002 13.05 8.05002 12.86 8.14002 12.71L9.54002 10.29C9.62002 10.13 9.81002 10.07 9.96002 10.13L11.71 10.84C12.07 10.56 12.46 10.32 12.89 10.15L13.15 8.28998C13.18 8.12998 13.32 7.99998 13.5 7.99998H16.3C16.47 7.99998 16.62 8.12998 16.64 8.28998L16.91 10.15C17.33 10.32 17.73 10.56 18.09 10.84L19.83 10.13C20 10.07 20.17 10.13 20.26 10.29L21.66 12.71C21.75 12.86 21.71 13.05 21.58 13.16L20.1 14.31L20.15 15L20.1 15.68Z'/%3E %3Cpath d='M7.32966 7.44454C8.0831 7.00954 8.33932 6.05332 7.90432 5.29988C7.46932 4.54643 6.5081 4.28156 5.75466 4.71656C5.39176 4.92608 5.12695 5.27118 5.01849 5.67594C4.91004 6.08071 4.96682 6.51198 5.17634 6.87488C5.61134 7.62832 6.57622 7.87954 7.32966 7.44454ZM9.65718 4.79593L10.8672 4.95179C10.9628 4.97741 11.0402 5.07133 11.0382 5.18793L11.0388 6.98893C11.0455 7.10054 10.9616 7.19518 10.855 7.21054L9.66001 7.38083L9.23915 8.13188L9.66961 9.25745C9.70729 9.36271 9.66934 9.47699 9.57408 9.53199L8.01523 10.432C7.91131 10.492 7.79337 10.4677 7.72105 10.3824L6.98748 9.43188L6.10931 9.43083L5.34704 10.3905C5.28909 10.4702 5.17383 10.4905 5.07187 10.4339L3.51245 9.53293C3.41049 9.47633 3.37647 9.35741 3.41075 9.25679L3.86347 8.14093L3.61749 7.77488L3.42347 7.37883L2.23075 7.21297C2.12647 7.19235 2.04049 7.10342 2.04245 6.98682L2.04187 5.18582C2.04383 5.06922 2.11909 4.97958 2.21704 4.96922L3.42065 4.79393L3.86749 4.02788L3.41105 2.91731C3.37337 2.81204 3.41131 2.69776 3.51523 2.63776L5.07408 1.73776C5.16934 1.68276 5.28729 1.70704 5.35961 1.79231L6.11915 2.72788L6.98001 2.73893L7.72496 1.78922C7.79156 1.70458 7.91548 1.67922 8.00879 1.74082L9.56821 2.64182C9.67017 2.69842 9.71285 2.81234 9.68723 2.90797L9.21718 4.03383L9.46316 4.39988L9.65718 4.79593Z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-caret-down-empty-thin: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 20 20'%3E %3Cg class='jp-icon3' fill='%23616161' shape-rendering='geometricPrecision'%3E %3Cpolygon class='st1' points='9.9,13.6 3.6,7.4 4.4,6.6 9.9,12.2 15.4,6.7 16.1,7.4 '/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-caret-down-empty: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 18 18'%3E %3Cg class='jp-icon3' fill='%23616161' shape-rendering='geometricPrecision'%3E %3Cpath d='M5.2,5.9L9,9.7l3.8-3.8l1.2,1.2l-4.9,5l-4.9-5L5.2,5.9z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-caret-down: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 18 18'%3E %3Cg class='jp-icon3' fill='%23616161' shape-rendering='geometricPrecision'%3E %3Cpath d='M5.2,7.5L9,11.2l3.8-3.8H5.2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-caret-left: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 18 18'%3E %3Cg class='jp-icon3' fill='%23616161' shape-rendering='geometricPrecision'%3E %3Cpath d='M10.8,12.8L7.1,9l3.8-3.8l0,7.6H10.8z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-caret-right: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 18 18'%3E %3Cg class='jp-icon3' fill='%23616161' shape-rendering='geometricPrecision'%3E %3Cpath d='M7.2,5.2L10.9,9l-3.8,3.8V5.2H7.2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-caret-up-empty-thin: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 20 20'%3E %3Cg class='jp-icon3' fill='%23616161' shape-rendering='geometricPrecision'%3E %3Cpolygon class='st1' points='15.4,13.3 9.9,7.7 4.4,13.2 3.6,12.5 9.9,6.3 16.1,12.6 '/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-caret-up: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 18 18'%3E %3Cg class='jp-icon3' fill='%23616161' shape-rendering='geometricPrecision'%3E %3Cpath d='M5.2,10.5L9,6.8l3.8,3.8H5.2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-case-sensitive: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 20 20'%3E %3Cg class='jp-icon2' fill='%23414141'%3E %3Crect x='2' y='2' width='16' height='16'/%3E %3C/g%3E %3Cg class='jp-icon-accent2' fill='%23FFF'%3E %3Cpath d='M7.6,8h0.9l3.5,8h-1.1L10,14H6l-0.9,2H4L7.6,8z M8,9.1L6.4,13h3.2L8,9.1z'/%3E %3Cpath d='M16.6,9.8c-0.2,0.1-0.4,0.1-0.7,0.1c-0.2,0-0.4-0.1-0.6-0.2c-0.1-0.1-0.2-0.4-0.2-0.7 c-0.3,0.3-0.6,0.5-0.9,0.7c-0.3,0.1-0.7,0.2-1.1,0.2c-0.3,0-0.5,0-0.7-0.1c-0.2-0.1-0.4-0.2-0.6-0.3c-0.2-0.1-0.3-0.3-0.4-0.5 c-0.1-0.2-0.1-0.4-0.1-0.7c0-0.3,0.1-0.6,0.2-0.8c0.1-0.2,0.3-0.4,0.4-0.5C12,7,12.2,6.9,12.5,6.8c0.2-0.1,0.5-0.1,0.7-0.2 c0.3-0.1,0.5-0.1,0.7-0.1c0.2,0,0.4-0.1,0.6-0.1c0.2,0,0.3-0.1,0.4-0.2c0.1-0.1,0.2-0.2,0.2-0.4c0-1-1.1-1-1.3-1 c-0.4,0-1.4,0-1.4,1.2h-0.9c0-0.4,0.1-0.7,0.2-1c0.1-0.2,0.3-0.4,0.5-0.6c0.2-0.2,0.5-0.3,0.8-0.3C13.3,4,13.6,4,13.9,4 c0.3,0,0.5,0,0.8,0.1c0.3,0,0.5,0.1,0.7,0.2c0.2,0.1,0.4,0.3,0.5,0.5C16,5,16,5.2,16,5.6v2.9c0,0.2,0,0.4,0,0.5 c0,0.1,0.1,0.2,0.3,0.2c0.1,0,0.2,0,0.3,0V9.8z M15.2,6.9c-1.2,0.6-3.1,0.2-3.1,1.4c0,1.4,3.1,1,3.1-0.5V6.9z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-check: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-circle-empty: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-circle: url("data:image/svg+xml,%3Csvg viewBox='0 0 18 18' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Ccircle cx='9' cy='9' r='8'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-clear: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cmask id='donutHole'%3E %3Crect width='24' height='24' fill='white' /%3E %3Ccircle cx='12' cy='12' r='8' fill='black'/%3E %3C/mask%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Crect height='18' width='2' x='11' y='3' transform='rotate(315, 12, 12)'/%3E %3Ccircle cx='12' cy='12' r='10' mask='url(%23donutHole)'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-close: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon-none jp-icon-selectable-inverse jp-icon3-hover' fill='none'%3E %3Ccircle cx='12' cy='12' r='11'/%3E %3C/g%3E %3Cg class='jp-icon3 jp-icon-selectable jp-icon-accent2-hover' fill='%23616161'%3E %3Cpath d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'/%3E %3C/g%3E %3Cg class='jp-icon-none jp-icon-busy' fill='none'%3E %3Ccircle cx='12' cy='12' r='7'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-console: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 200 200'%3E %3Cg class='jp-icon-brand1 jp-icon-selectable' fill='%230288D1'%3E %3Cpath d='M20 19.8h160v159.9H20z'/%3E %3C/g%3E %3Cg class='jp-icon-selectable-inverse' fill='%23fff'%3E %3Cpath d='M105 127.3h40v12.8h-40zM51.1 77L74 99.9l-23.3 23.3 10.5 10.5 23.3-23.3L95 99.9 84.5 89.4 61.6 66.5z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-copy: url("data:image/svg+xml,%3Csvg viewBox='0 0 18 18' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M11.9,1H3.2C2.4,1,1.7,1.7,1.7,2.5v10.2h1.5V2.5h8.7V1z M14.1,3.9h-8c-0.8,0-1.5,0.7-1.5,1.5v10.2c0,0.8,0.7,1.5,1.5,1.5h8 c0.8,0,1.5-0.7,1.5-1.5V5.4C15.5,4.6,14.9,3.9,14.1,3.9z M14.1,15.5h-8V5.4h8V15.5z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-cut: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M9.64 7.64c.23-.5.36-1.05.36-1.64 0-2.21-1.79-4-4-4S2 3.79 2 6s1.79 4 4 4c.59 0 1.14-.13 1.64-.36L10 12l-2.36 2.36C7.14 14.13 6.59 14 6 14c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4c0-.59-.13-1.14-.36-1.64L12 14l7 7h3v-1L9.64 7.64zM6 8c-1.1 0-2-.89-2-2s.9-2 2-2 2 .89 2 2-.9 2-2 2zm0 12c-1.1 0-2-.89-2-2s.9-2 2-2 2 .89 2 2-.9 2-2 2zm6-7.5c-.28 0-.5-.22-.5-.5s.22-.5.5-.5.5.22.5.5-.22.5-.5.5zM19 3l-6 6 2 2 7-7V3z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-download: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-edit: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-ellipses: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Ccircle cx='5' cy='12' r='2'/%3E %3Ccircle cx='12' cy='12' r='2'/%3E %3Ccircle cx='19' cy='12' r='2'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-extension: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M20.5 11H19V7c0-1.1-.9-2-2-2h-4V3.5C13 2.12 11.88 1 10.5 1S8 2.12 8 3.5V5H4c-1.1 0-1.99.9-1.99 2v3.8H3.5c1.49 0 2.7 1.21 2.7 2.7s-1.21 2.7-2.7 2.7H2V20c0 1.1.9 2 2 2h3.8v-1.5c0-1.49 1.21-2.7 2.7-2.7 1.49 0 2.7 1.21 2.7 2.7V22H17c1.1 0 2-.9 2-2v-4h1.5c1.38 0 2.5-1.12 2.5-2.5S21.88 11 20.5 11z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-fast-forward: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M4 18l8.5-6L4 6v12zm9-12v12l8.5-6L13 6z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-file-upload: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M9 16h6v-6h4l-7-7-7 7h4zm-4 2h14v2H5z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-file: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cpath class='jp-icon3 jp-icon-selectable' fill='%23616161' d='M19.3 8.2l-5.5-5.5c-.3-.3-.7-.5-1.2-.5H3.9c-.8.1-1.6.9-1.6 1.8v14.1c0 .9.7 1.6 1.6 1.6h14.2c.9 0 1.6-.7 1.6-1.6V9.4c.1-.5-.1-.9-.4-1.2zm-5.8-3.3l3.4 3.6h-3.4V4.9zm3.9 12.7H4.7c-.1 0-.2 0-.2-.2V4.7c0-.2.1-.3.2-.3h7.2v4.4s0 .8.3 1.1c.3.3 1.1.3 1.1.3h4.3v7.2s-.1.2-.2.2z'/%3E %3C/svg%3E");
  --jp-icon-filter-list: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-folder: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon3 jp-icon-selectable' fill='%23616161' d='M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z'/%3E %3C/svg%3E");
  --jp-icon-html5: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 512 512'%3E %3Cpath class='jp-icon0 jp-icon-selectable' fill='%23000' d='M108.4 0h23v22.8h21.2V0h23v69h-23V46h-21v23h-23.2M206 23h-20.3V0h63.7v23H229v46h-23m53.5-69h24.1l14.8 24.3L313.2 0h24.1v69h-23V34.8l-16.1 24.8-16.1-24.8V69h-22.6m89.2-69h23v46.2h32.6V69h-55.6'/%3E %3Cpath class='jp-icon-selectable' fill='%23e44d26' d='M107.6 471l-33-370.4h362.8l-33 370.2L255.7 512'/%3E %3Cpath class='jp-icon-selectable' fill='%23f16529' d='M256 480.5V131h148.3L376 447'/%3E %3Cpath class='jp-icon-selectable-inverse' fill='%23ebebeb' d='M142 176.3h114v45.4h-64.2l4.2 46.5h60v45.3H154.4m2 22.8H202l3.2 36.3 50.8 13.6v47.4l-93.2-26'/%3E %3Cpath class='jp-icon-selectable-inverse' fill='%23fff' d='M369.6 176.3H255.8v45.4h109.6m-4.1 46.5H255.8v45.4h56l-5.3 59-50.7 13.6v47.2l93-25.8'/%3E %3C/svg%3E");
  --jp-icon-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cpath class='jp-icon-brand4 jp-icon-selectable-inverse' fill='%23FFF' d='M2.2 2.2h17.5v17.5H2.2z'/%3E %3Cpath class='jp-icon-brand0 jp-icon-selectable' fill='%233F51B5' d='M2.2 2.2v17.5h17.5l.1-17.5H2.2zm12.1 2.2c1.2 0 2.2 1 2.2 2.2s-1 2.2-2.2 2.2-2.2-1-2.2-2.2 1-2.2 2.2-2.2zM4.4 17.6l3.3-8.8 3.3 6.6 2.2-3.2 4.4 5.4H4.4z'/%3E %3C/svg%3E");
  --jp-icon-inspector: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon3 jp-icon-selectable' fill='%23616161' d='M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-5 14H4v-4h11v4zm0-5H4V9h11v4zm5 5h-4V9h4v9z'/%3E %3C/svg%3E");
  --jp-icon-json: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cg class='jp-icon-warn1 jp-icon-selectable' fill='%23F9A825'%3E %3Cpath d='M20.2 11.8c-1.6 0-1.7.5-1.7 1 0 .4.1.9.1 1.3.1.5.1.9.1 1.3 0 1.7-1.4 2.3-3.5 2.3h-.9v-1.9h.5c1.1 0 1.4 0 1.4-.8 0-.3 0-.6-.1-1 0-.4-.1-.8-.1-1.2 0-1.3 0-1.8 1.3-2-1.3-.2-1.3-.7-1.3-2 0-.4.1-.8.1-1.2.1-.4.1-.7.1-1 0-.8-.4-.7-1.4-.8h-.5V4.1h.9c2.2 0 3.5.7 3.5 2.3 0 .4-.1.9-.1 1.3-.1.5-.1.9-.1 1.3 0 .5.2 1 1.7 1v1.8zM1.8 10.1c1.6 0 1.7-.5 1.7-1 0-.4-.1-.9-.1-1.3-.1-.5-.1-.9-.1-1.3 0-1.6 1.4-2.3 3.5-2.3h.9v1.9h-.5c-1 0-1.4 0-1.4.8 0 .3 0 .6.1 1 0 .2.1.6.1 1 0 1.3 0 1.8-1.3 2C6 11.2 6 11.7 6 13c0 .4-.1.8-.1 1.2-.1.3-.1.7-.1 1 0 .8.3.8 1.4.8h.5v1.9h-.9c-2.1 0-3.5-.6-3.5-2.3 0-.4.1-.9.1-1.3.1-.5.1-.9.1-1.3 0-.5-.2-1-1.7-1v-1.9z'/%3E %3Ccircle cx='11' cy='13.8' r='2.1'/%3E %3Ccircle cx='11' cy='8.2' r='2.1'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-jupyter-favicon: url("data:image/svg+xml,%3Csvg width='152' height='165' viewBox='0 0 152 165' version='1.1' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon-warn0' fill='%23F37726'%3E %3Cpath transform='translate(0.078947, 110.582927)' d='M75.9422842,29.5804561 C43.3023947,29.5804561 14.7967832,17.6534634 0,0 C5.51083211,15.8406829 15.7815389,29.5667732 29.3904947,39.2784171 C42.9997,48.9898537 59.2737,54.2067805 75.9605789,54.2067805 C92.6474579,54.2067805 108.921458,48.9898537 122.530663,39.2784171 C136.139453,29.5667732 146.410284,15.8406829 151.921158,0 C137.087868,17.6534634 108.582589,29.5804561 75.9422842,29.5804561 L75.9422842,29.5804561 Z' /%3E %3Cpath transform='translate(0.037368, 0.704878)' d='M75.9784579,24.6264073 C108.618763,24.6264073 137.124458,36.5534415 151.921158,54.2067805 C146.410284,38.366222 136.139453,24.6401317 122.530663,14.9284878 C108.921458,5.2168439 92.6474579,0 75.9605789,0 C59.2737,0 42.9997,5.2168439 29.3904947,14.9284878 C15.7815389,24.6401317 5.51083211,38.366222 0,54.2067805 C14.8330816,36.5899293 43.3385684,24.6264073 75.9784579,24.6264073 L75.9784579,24.6264073 Z' /%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-jupyter: url("data:image/svg+xml,%3Csvg width='39' height='51' viewBox='0 0 39 51' xmlns='http://www.w3.org/2000/svg'%3E %3Cg transform='translate(-1638 -2281)'%3E %3Cg class='jp-icon-warn0' fill='%23F37726'%3E %3Cpath transform='translate(1639.74 2311.98)' d='M 18.2646 7.13411C 10.4145 7.13411 3.55872 4.2576 0 0C 1.32539 3.8204 3.79556 7.13081 7.0686 9.47303C 10.3417 11.8152 14.2557 13.0734 18.269 13.0734C 22.2823 13.0734 26.1963 11.8152 29.4694 9.47303C 32.7424 7.13081 35.2126 3.8204 36.538 0C 32.9705 4.2576 26.1148 7.13411 18.2646 7.13411Z'/%3E %3Cpath transform='translate(1639.73 2285.48)' d='M 18.2733 5.93931C 26.1235 5.93931 32.9793 8.81583 36.538 13.0734C 35.2126 9.25303 32.7424 5.94262 29.4694 3.6004C 26.1963 1.25818 22.2823 0 18.269 0C 14.2557 0 10.3417 1.25818 7.0686 3.6004C 3.79556 5.94262 1.32539 9.25303 0 13.0734C 3.56745 8.82463 10.4232 5.93931 18.2733 5.93931Z'/%3E %3C/g%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath transform='translate(1669.3 2281.31)' d='M 5.89353 2.844C 5.91889 3.43165 5.77085 4.01367 5.46815 4.51645C 5.16545 5.01922 4.72168 5.42015 4.19299 5.66851C 3.6643 5.91688 3.07444 6.00151 2.49805 5.91171C 1.92166 5.8219 1.38463 5.5617 0.954898 5.16401C 0.52517 4.76633 0.222056 4.24903 0.0839037 3.67757C -0.0542483 3.10611 -0.02123 2.50617 0.178781 1.95364C 0.378793 1.4011 0.736809 0.920817 1.20754 0.573538C 1.67826 0.226259 2.24055 0.0275919 2.82326 0.00267229C 3.60389 -0.0307115 4.36573 0.249789 4.94142 0.782551C 5.51711 1.31531 5.85956 2.05676 5.89353 2.844Z'/%3E %3Cpath transform='translate(1639.8 2323.81)' d='M 7.42789 3.58338C 7.46008 4.3243 7.27355 5.05819 6.89193 5.69213C 6.51031 6.32607 5.95075 6.83156 5.28411 7.1446C 4.61747 7.45763 3.87371 7.56414 3.14702 7.45063C 2.42032 7.33712 1.74336 7.0087 1.20184 6.50695C 0.660328 6.0052 0.27861 5.35268 0.105017 4.63202C -0.0685757 3.91135 -0.0262361 3.15494 0.226675 2.45856C 0.479587 1.76217 0.931697 1.15713 1.52576 0.720033C 2.11983 0.282935 2.82914 0.0334395 3.56389 0.00313344C 4.54667 -0.0374033 5.50529 0.316706 6.22961 0.987835C 6.95393 1.65896 7.38484 2.59235 7.42789 3.58338L 7.42789 3.58338Z'/%3E %3Cpath transform='translate(1638.36 2286.06)' d='M 2.27471 4.39629C 1.84363 4.41508 1.41671 4.30445 1.04799 4.07843C 0.679268 3.8524 0.385328 3.52114 0.203371 3.12656C 0.0214136 2.73198 -0.0403798 2.29183 0.0258116 1.86181C 0.0920031 1.4318 0.283204 1.03126 0.575213 0.710883C 0.867222 0.39051 1.24691 0.164708 1.66622 0.0620592C 2.08553 -0.0405897 2.52561 -0.0154714 2.93076 0.134235C 3.33591 0.283941 3.68792 0.551505 3.94222 0.90306C 4.19652 1.25462 4.34169 1.67436 4.35935 2.10916C 4.38299 2.69107 4.17678 3.25869 3.78597 3.68746C 3.39516 4.11624 2.85166 4.37116 2.27471 4.39629L 2.27471 4.39629Z'/%3E %3C/g%3E %3C/g%3E%3E %3C/svg%3E");
  --jp-icon-jupyterlab-wordmark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' viewBox='0 0 1860.8 475'%3E %3Cg class='jp-icon2' fill='%234E4E4E' transform='translate(480.136401, 64.271493)'%3E %3Cg transform='translate(0.000000, 58.875566)'%3E %3Cg transform='translate(0.087603, 0.140294)'%3E %3Cpath d='M-426.9,169.8c0,48.7-3.7,64.7-13.6,76.4c-10.8,10-25,15.5-39.7,15.5l3.7,29 c22.8,0.3,44.8-7.9,61.9-23.1c17.8-18.5,24-44.1,24-83.3V0H-427v170.1L-426.9,169.8L-426.9,169.8z'/%3E %3C/g%3E %3C/g%3E %3Cg transform='translate(155.045296, 56.837104)'%3E %3Cg transform='translate(1.562453, 1.799842)'%3E %3Cpath d='M-312,148c0,21,0,39.5,1.7,55.4h-31.8l-2.1-33.3h-0.8c-6.7,11.6-16.4,21.3-28,27.9 c-11.6,6.6-24.8,10-38.2,9.8c-31.4,0-69-17.7-69-89V0h36.4v112.7c0,38.7,11.6,64.7,44.6,64.7c10.3-0.2,20.4-3.5,28.9-9.4 c8.5-5.9,15.1-14.3,18.9-23.9c2.2-6.1,3.3-12.5,3.3-18.9V0.2h36.4V148H-312L-312,148z'/%3E %3C/g%3E %3C/g%3E %3Cg transform='translate(390.013322, 53.479638)'%3E %3Cg transform='translate(1.706458, 0.231425)'%3E %3Cpath d='M-478.6,71.4c0-26-0.8-47-1.7-66.7h32.7l1.7,34.8h0.8c7.1-12.5,17.5-22.8,30.1-29.7 c12.5-7,26.7-10.3,41-9.8c48.3,0,84.7,41.7,84.7,103.3c0,73.1-43.7,109.2-91,109.2c-12.1,0.5-24.2-2.2-35-7.8 c-10.8-5.6-19.9-13.9-26.6-24.2h-0.8V291h-36v-220L-478.6,71.4L-478.6,71.4z M-442.6,125.6c0.1,5.1,0.6,10.1,1.7,15.1 c3,12.3,9.9,23.3,19.8,31.1c9.9,7.8,22.1,12.1,34.7,12.1c38.5,0,60.7-31.9,60.7-78.5c0-40.7-21.1-75.6-59.5-75.6 c-12.9,0.4-25.3,5.1-35.3,13.4c-9.9,8.3-16.9,19.7-19.6,32.4c-1.5,4.9-2.3,10-2.5,15.1V125.6L-442.6,125.6L-442.6,125.6z'/%3E %3C/g%3E %3C/g%3E %3Cg transform='translate(606.740726, 56.837104)'%3E %3Cg transform='translate(0.751226, 1.989299)'%3E %3Cpath d='M-440.8,0l43.7,120.1c4.5,13.4,9.5,29.4,12.8,41.7h0.8c3.7-12.2,7.9-27.7,12.8-42.4 l39.7-119.2h38.5L-346.9,145c-26,69.7-43.7,105.4-68.6,127.2c-12.5,11.7-27.9,20-44.6,23.9l-9.1-31.1 c11.7-3.9,22.5-10.1,31.8-18.1c13.2-11.1,23.7-25.2,30.6-41.2c1.5-2.8,2.5-5.7,2.9-8.8c-0.3-3.3-1.2-6.6-2.5-9.7L-480.2,0.1 h39.7L-440.8,0L-440.8,0z'/%3E %3C/g%3E %3C/g%3E %3Cg transform='translate(822.748104, 0.000000)'%3E %3Cg transform='translate(1.464050, 0.378914)'%3E %3Cpath d='M-413.7,0v58.3h52v28.2h-52V196c0,25,7,39.5,27.3,39.5c7.1,0.1,14.2-0.7,21.1-2.5 l1.7,27.7c-10.3,3.7-21.3,5.4-32.2,5c-7.3,0.4-14.6-0.7-21.3-3.4c-6.8-2.7-12.9-6.8-17.9-12.1c-10.3-10.9-14.1-29-14.1-52.9 V86.5h-31V58.3h31V9.6L-413.7,0L-413.7,0z'/%3E %3C/g%3E %3C/g%3E %3Cg transform='translate(974.433286, 53.479638)'%3E %3Cg transform='translate(0.990034, 0.610339)'%3E %3Cpath d='M-445.8,113c0.8,50,32.2,70.6,68.6,70.6c19,0.6,37.9-3,55.3-10.5l6.2,26.4 c-20.9,8.9-43.5,13.1-66.2,12.6c-61.5,0-98.3-41.2-98.3-102.5C-480.2,48.2-444.7,0-386.5,0c65.2,0,82.7,58.3,82.7,95.7 c-0.1,5.8-0.5,11.5-1.2,17.2h-140.6H-445.8L-445.8,113z M-339.2,86.6c0.4-23.5-9.5-60.1-50.4-60.1 c-36.8,0-52.8,34.4-55.7,60.1H-339.2L-339.2,86.6L-339.2,86.6z'/%3E %3C/g%3E %3C/g%3E %3Cg transform='translate(1201.961058, 53.479638)'%3E %3Cg transform='translate(1.179640, 0.705068)'%3E %3Cpath d='M-478.6,68c0-23.9-0.4-44.5-1.7-63.4h31.8l1.2,39.9h1.7c9.1-27.3,31-44.5,55.3-44.5 c3.5-0.1,7,0.4,10.3,1.2v34.8c-4.1-0.9-8.2-1.3-12.4-1.2c-25.6,0-43.7,19.7-48.7,47.4c-1,5.7-1.6,11.5-1.7,17.2v108.3h-36V68 L-478.6,68z'/%3E %3C/g%3E %3C/g%3E %3C/g%3E %3Cg class='jp-icon-warn0' fill='%23F37726'%3E %3Cpath d='M1352.3,326.2h37V28h-37V326.2z M1604.8,326.2c-2.5-13.9-3.4-31.1-3.4-48.7v-76 c0-40.7-15.1-83.1-77.3-83.1c-25.6,0-50,7.1-66.8,18.1l8.4,24.4c14.3-9.2,34-15.1,53-15.1c41.6,0,46.2,30.2,46.2,47v4.2 c-78.6-0.4-122.3,26.5-122.3,75.6c0,29.4,21,58.4,62.2,58.4c29,0,50.9-14.3,62.2-30.2h1.3l2.9,25.6H1604.8z M1565.7,257.7 c0,3.8-0.8,8-2.1,11.8c-5.9,17.2-22.7,34-49.2,34c-18.9,0-34.9-11.3-34.9-35.3c0-39.5,45.8-46.6,86.2-45.8V257.7z M1698.5,326.2 l1.7-33.6h1.3c15.1,26.9,38.7,38.2,68.1,38.2c45.4,0,91.2-36.1,91.2-108.8c0.4-61.7-35.3-103.7-85.7-103.7 c-32.8,0-56.3,14.7-69.3,37.4h-0.8V28h-36.6v245.7c0,18.1-0.8,38.6-1.7,52.5H1698.5z M1704.8,208.2c0-5.9,1.3-10.9,2.1-15.1 c7.6-28.1,31.1-45.4,56.3-45.4c39.5,0,60.5,34.9,60.5,75.6c0,46.6-23.1,78.1-61.8,78.1c-26.9,0-48.3-17.6-55.5-43.3 c-0.8-4.2-1.7-8.8-1.7-13.4V208.2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-kernel: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon2' fill='%23616161' d='M15 9H9v6h6V9zm-2 4h-2v-2h2v2zm8-2V9h-2V7c0-1.1-.9-2-2-2h-2V3h-2v2h-2V3H9v2H7c-1.1 0-2 .9-2 2v2H3v2h2v2H3v2h2v2c0 1.1.9 2 2 2h2v2h2v-2h2v2h2v-2h2c1.1 0 2-.9 2-2v-2h2v-2h-2v-2h2zm-4 6H7V7h10v10z'/%3E %3C/svg%3E");
  --jp-icon-keyboard: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon3 jp-icon-selectable' fill='%23616161' d='M20 5H4c-1.1 0-1.99.9-1.99 2L2 17c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm-9 3h2v2h-2V8zm0 3h2v2h-2v-2zM8 8h2v2H8V8zm0 3h2v2H8v-2zm-1 2H5v-2h2v2zm0-3H5V8h2v2zm9 7H8v-2h8v2zm0-4h-2v-2h2v2zm0-3h-2V8h2v2zm3 3h-2v-2h2v2zm0-3h-2V8h2v2z'/%3E %3C/svg%3E");
  --jp-icon-launcher: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon3 jp-icon-selectable' fill='%23616161' d='M19 19H5V5h7V3H5a2 2 0 00-2 2v14a2 2 0 002 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z'/%3E %3C/svg%3E");
  --jp-icon-line-form: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath fill='white' d='M5.88 4.12L13.76 12l-7.88 7.88L8 22l10-10L8 2z'/%3E %3C/svg%3E");
  --jp-icon-link: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-list: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon2 jp-icon-selectable' fill='%23616161' d='M19 5v14H5V5h14m1.1-2H3.9c-.5 0-.9.4-.9.9v16.2c0 .4.4.9.9.9h16.2c.4 0 .9-.5.9-.9V3.9c0-.5-.5-.9-.9-.9zM11 7h6v2h-6V7zm0 4h6v2h-6v-2zm0 4h6v2h-6zM7 7h2v2H7zm0 4h2v2H7zm0 4h2v2H7z'/%3E %3C/svg%3E");
  --jp-icon-listings-info: url("data:image/svg+xml,%3C?xml version='1.0' encoding='iso-8859-1'?%3E %3Csvg version='1.1' id='Capa_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 50.978 50.978' style='enable-background:new 0 0 50.978 50.978;' xml:space='preserve'%3E %3Cg%3E %3Cg%3E %3Cg%3E %3Cpath style='fill:%23010002;' d='M43.52,7.458C38.711,2.648,32.307,0,25.489,0C18.67,0,12.266,2.648,7.458,7.458 c-9.943,9.941-9.943,26.119,0,36.062c4.809,4.809,11.212,7.456,18.031,7.458c0,0,0.001,0,0.002,0 c6.816,0,13.221-2.648,18.029-7.458c4.809-4.809,7.457-11.212,7.457-18.03C50.977,18.67,48.328,12.266,43.52,7.458z M42.106,42.105c-4.432,4.431-10.332,6.872-16.615,6.872h-0.002c-6.285-0.001-12.187-2.441-16.617-6.872 c-9.162-9.163-9.162-24.071,0-33.233C13.303,4.44,19.204,2,25.489,2c6.284,0,12.186,2.44,16.617,6.872 c4.431,4.431,6.871,10.332,6.871,16.617C48.977,31.772,46.536,37.675,42.106,42.105z'/%3E %3C/g%3E %3Cg%3E %3Cpath style='fill:%23010002;' d='M23.578,32.218c-0.023-1.734,0.143-3.059,0.496-3.972c0.353-0.913,1.11-1.997,2.272-3.253 c0.468-0.536,0.923-1.062,1.367-1.575c0.626-0.753,1.104-1.478,1.436-2.175c0.331-0.707,0.495-1.541,0.495-2.5 c0-1.096-0.26-2.088-0.779-2.979c-0.565-0.879-1.501-1.336-2.806-1.369c-1.802,0.057-2.985,0.667-3.55,1.832 c-0.301,0.535-0.503,1.141-0.607,1.814c-0.139,0.707-0.207,1.432-0.207,2.174h-2.937c-0.091-2.208,0.407-4.114,1.493-5.719 c1.062-1.64,2.855-2.481,5.378-2.527c2.16,0.023,3.874,0.608,5.141,1.758c1.278,1.16,1.929,2.764,1.95,4.811 c0,1.142-0.137,2.111-0.41,2.911c-0.309,0.845-0.731,1.593-1.268,2.243c-0.492,0.65-1.068,1.318-1.73,2.002 c-0.65,0.697-1.313,1.479-1.987,2.346c-0.239,0.377-0.429,0.777-0.565,1.199c-0.16,0.959-0.217,1.951-0.171,2.979 C26.589,32.218,23.578,32.218,23.578,32.218z M23.578,38.22v-3.484h3.076v3.484H23.578z'/%3E %3C/g%3E %3C/g%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3Cg%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-markdown: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cpath class='jp-icon-contrast0 jp-icon-selectable' fill='%237B1FA2' d='M5 14.9h12l-6.1 6zm9.4-6.8c0-1.3-.1-2.9-.1-4.5-.4 1.4-.9 2.9-1.3 4.3l-1.3 4.3h-2L8.5 7.9c-.4-1.3-.7-2.9-1-4.3-.1 1.6-.1 3.2-.2 4.6L7 12.4H4.8l.7-11h3.3L10 5c.4 1.2.7 2.7 1 3.9.3-1.2.7-2.6 1-3.9l1.2-3.7h3.3l.6 11h-2.4l-.3-4.2z'/%3E %3C/svg%3E");
  --jp-icon-new-folder: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M20 6h-8l-2-2H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-1 8h-3v3h-2v-3h-3v-2h3V9h2v3h3v2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-not-trusted: url("data:image/svg+xml,%3Csvg fill='none' xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 25 25'%3E %3Cpath class='jp-icon2' stroke='%23333333' stroke-width='2' transform='translate(3 3)' d='M1.86094 11.4409C0.826448 8.77027 0.863779 6.05764 1.24907 4.19932C2.48206 3.93347 4.08068 3.40347 5.60102 2.8449C7.23549 2.2444 8.85666 1.5815 9.9876 1.09539C11.0597 1.58341 12.6094 2.2444 14.218 2.84339C15.7503 3.41394 17.3995 3.95258 18.7539 4.21385C19.1364 6.07177 19.1709 8.77722 18.139 11.4409C17.0303 14.3032 14.6668 17.1844 9.99999 18.9354C5.33319 17.1844 2.96968 14.3032 1.86094 11.4409Z'/%3E %3Cpath class='jp-icon2' stroke='%23333333' stroke-width='2' transform='translate(9.31592 9.32031)' d='M7.36842 0L0 7.36479'/%3E %3Cpath class='jp-icon2' stroke='%23333333' stroke-width='2' transform='translate(9.31592 16.6836) scale(1 -1)' d='M7.36842 0L0 7.36479'/%3E %3C/svg%3E");
  --jp-icon-notebook: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cg class='jp-icon-warn0 jp-icon-selectable' fill='%23EF6C00'%3E %3Cpath d='M18.7 3.3v15.4H3.3V3.3h15.4m1.5-1.5H1.8v18.3h18.3l.1-18.3z'/%3E %3Cpath d='M16.5 16.5l-5.4-4.3-5.6 4.3v-11h11z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-palette: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M18 13V20H4V6H9.02C9.07 5.29 9.24 4.62 9.5 4H4C2.9 4 2 4.9 2 6V20C2 21.1 2.9 22 4 22H18C19.1 22 20 21.1 20 20V15L18 13ZM19.3 8.89C19.74 8.19 20 7.38 20 6.5C20 4.01 17.99 2 15.5 2C13.01 2 11 4.01 11 6.5C11 8.99 13.01 11 15.49 11C16.37 11 17.19 10.74 17.88 10.3L21 13.42L22.42 12L19.3 8.89ZM15.5 9C14.12 9 13 7.88 13 6.5C13 5.12 14.12 4 15.5 4C16.88 4 18 5.12 18 6.5C18 7.88 16.88 9 15.5 9Z'/%3E %3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M4 6H9.01894C9.00639 6.16502 9 6.33176 9 6.5C9 8.81577 10.211 10.8487 12.0343 12H9V14H16V12.9811C16.5703 12.9377 17.12 12.8207 17.6396 12.6396L18 13V20H4V6ZM8 8H6V10H8V8ZM6 12H8V14H6V12ZM8 16H6V18H8V16ZM9 16H16V18H9V16Z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-paste: url("data:image/svg+xml,%3Csvg height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M19 2h-4.18C14.4.84 13.3 0 12 0c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm7 18H5V4h2v3h10V4h2v16z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-python: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cg class='jp-icon-brand0 jp-icon-selectable' fill='%230D47A1'%3E %3Cpath d='M11.1 6.9V5.8H6.9c0-.5 0-1.3.2-1.6.4-.7.8-1.1 1.7-1.4 1.7-.3 2.5-.3 3.9-.1 1 .1 1.9.9 1.9 1.9v4.2c0 .5-.9 1.6-2 1.6H8.8c-1.5 0-2.4 1.4-2.4 2.8v2.2H4.7C3.5 15.1 3 14 3 13.1V9c-.1-1 .6-2 1.8-2 1.5-.1 6.3-.1 6.3-.1z'/%3E %3Cpath d='M10.9 15.1v1.1h4.2c0 .5 0 1.3-.2 1.6-.4.7-.8 1.1-1.7 1.4-1.7.3-2.5.3-3.9.1-1-.1-1.9-.9-1.9-1.9v-4.2c0-.5.9-1.6 2-1.6h3.8c1.5 0 2.4-1.4 2.4-2.8V6.6h1.7C18.5 6.9 19 8 19 8.9V13c0 1-.7 2.1-1.9 2.1h-6.2z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-r-kernel: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cpath class='jp-icon-contrast3 jp-icon-selectable' fill='%232196F3' d='M4.4 2.5c1.2-.1 2.9-.3 4.9-.3 2.5 0 4.1.4 5.2 1.3 1 .7 1.5 1.9 1.5 3.5 0 2-1.4 3.5-2.9 4.1 1.2.4 1.7 1.6 2.2 3 .6 1.9 1 3.9 1.3 4.6h-3.8c-.3-.4-.8-1.7-1.2-3.7s-1.2-2.6-2.6-2.6h-.9v6.4H4.4V2.5zm3.7 6.9h1.4c1.9 0 2.9-.9 2.9-2.3s-1-2.3-2.8-2.3c-.7 0-1.3 0-1.6.2v4.5h.1v-.1z'/%3E %3C/svg%3E");
  --jp-icon-react: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='150 150 541.9 295.3'%3E %3Cg class='jp-icon-brand2 jp-icon-selectable' fill='%2361DAFB'%3E %3Cpath d='M666.3 296.5c0-32.5-40.7-63.3-103.1-82.4 14.4-63.6 8-114.2-20.2-130.4-6.5-3.8-14.1-5.6-22.4-5.6v22.3c4.6 0 8.3.9 11.4 2.6 13.6 7.8 19.5 37.5 14.9 75.7-1.1 9.4-2.9 19.3-5.1 29.4-19.6-4.8-41-8.5-63.5-10.9-13.5-18.5-27.5-35.3-41.6-50 32.6-30.3 63.2-46.9 84-46.9V78c-27.5 0-63.5 19.6-99.9 53.6-36.4-33.8-72.4-53.2-99.9-53.2v22.3c20.7 0 51.4 16.5 84 46.6-14 14.7-28 31.4-41.3 49.9-22.6 2.4-44 6.1-63.6 11-2.3-10-4-19.7-5.2-29-4.7-38.2 1.1-67.9 14.6-75.8 3-1.8 6.9-2.6 11.5-2.6V78.5c-8.4 0-16 1.8-22.6 5.6-28.1 16.2-34.4 66.7-19.9 130.1-62.2 19.2-102.7 49.9-102.7 82.3 0 32.5 40.7 63.3 103.1 82.4-14.4 63.6-8 114.2 20.2 130.4 6.5 3.8 14.1 5.6 22.5 5.6 27.5 0 63.5-19.6 99.9-53.6 36.4 33.8 72.4 53.2 99.9 53.2 8.4 0 16-1.8 22.6-5.6 28.1-16.2 34.4-66.7 19.9-130.1 62-19.1 102.5-49.9 102.5-82.3zm-130.2-66.7c-3.7 12.9-8.3 26.2-13.5 39.5-4.1-8-8.4-16-13.1-24-4.6-8-9.5-15.8-14.4-23.4 14.2 2.1 27.9 4.7 41 7.9zm-45.8 106.5c-7.8 13.5-15.8 26.3-24.1 38.2-14.9 1.3-30 2-45.2 2-15.1 0-30.2-.7-45-1.9-8.3-11.9-16.4-24.6-24.2-38-7.6-13.1-14.5-26.4-20.8-39.8 6.2-13.4 13.2-26.8 20.7-39.9 7.8-13.5 15.8-26.3 24.1-38.2 14.9-1.3 30-2 45.2-2 15.1 0 30.2.7 45 1.9 8.3 11.9 16.4 24.6 24.2 38 7.6 13.1 14.5 26.4 20.8 39.8-6.3 13.4-13.2 26.8-20.7 39.9zm32.3-13c5.4 13.4 10 26.8 13.8 39.8-13.1 3.2-26.9 5.9-41.2 8 4.9-7.7 9.8-15.6 14.4-23.7 4.6-8 8.9-16.1 13-24.1zM421.2 430c-9.3-9.6-18.6-20.3-27.8-32 9 .4 18.2.7 27.5.7 9.4 0 18.7-.2 27.8-.7-9 11.7-18.3 22.4-27.5 32zm-74.4-58.9c-14.2-2.1-27.9-4.7-41-7.9 3.7-12.9 8.3-26.2 13.5-39.5 4.1 8 8.4 16 13.1 24 4.7 8 9.5 15.8 14.4 23.4zM420.7 163c9.3 9.6 18.6 20.3 27.8 32-9-.4-18.2-.7-27.5-.7-9.4 0-18.7.2-27.8.7 9-11.7 18.3-22.4 27.5-32zm-74 58.9c-4.9 7.7-9.8 15.6-14.4 23.7-4.6 8-8.9 16-13 24-5.4-13.4-10-26.8-13.8-39.8 13.1-3.1 26.9-5.8 41.2-7.9zm-90.5 125.2c-35.4-15.1-58.3-34.9-58.3-50.6 0-15.7 22.9-35.6 58.3-50.6 8.6-3.7 18-7 27.7-10.1 5.7 19.6 13.2 40 22.5 60.9-9.2 20.8-16.6 41.1-22.2 60.6-9.9-3.1-19.3-6.5-28-10.2zM310 490c-13.6-7.8-19.5-37.5-14.9-75.7 1.1-9.4 2.9-19.3 5.1-29.4 19.6 4.8 41 8.5 63.5 10.9 13.5 18.5 27.5 35.3 41.6 50-32.6 30.3-63.2 46.9-84 46.9-4.5-.1-8.3-1-11.3-2.7zm237.2-76.2c4.7 38.2-1.1 67.9-14.6 75.8-3 1.8-6.9 2.6-11.5 2.6-20.7 0-51.4-16.5-84-46.6 14-14.7 28-31.4 41.3-49.9 22.6-2.4 44-6.1 63.6-11 2.3 10.1 4.1 19.8 5.2 29.1zm38.5-66.7c-8.6 3.7-18 7-27.7 10.1-5.7-19.6-13.2-40-22.5-60.9 9.2-20.8 16.6-41.1 22.2-60.6 9.9 3.1 19.3 6.5 28.1 10.2 35.4 15.1 58.3 34.9 58.3 50.6-.1 15.7-23 35.6-58.4 50.6zM320.8 78.4z'/%3E %3Ccircle cx='420.9' cy='296.5' r='45.7'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-redo: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='24' viewBox='0 0 24 24' width='16'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M0 0h24v24H0z' fill='none'/%3E%3Cpath d='M18.4 10.6C16.55 8.99 14.15 8 11.5 8c-4.65 0-8.58 3.03-9.96 7.22L3.9 16c1.05-3.19 4.05-5.5 7.6-5.5 1.95 0 3.73.72 5.12 1.88L13 16h9V7l-3.6 3.6z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-refresh: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 18 18'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M9 13.5c-2.49 0-4.5-2.01-4.5-4.5S6.51 4.5 9 4.5c1.24 0 2.36.52 3.17 1.33L10 8h5V3l-1.76 1.76C12.15 3.68 10.66 3 9 3 5.69 3 3.01 5.69 3.01 9S5.69 15 9 15c2.97 0 5.43-2.16 5.9-5h-1.52c-.46 2-2.24 3.5-4.38 3.5z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-regex: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 20 20'%3E %3Cg class='jp-icon2' fill='%23414141'%3E %3Crect x='2' y='2' width='16' height='16'/%3E %3C/g%3E %3Cg class='jp-icon-accent2' fill='%23FFF'%3E %3Ccircle class='st2' cx='5.5' cy='14.5' r='1.5'/%3E %3Crect x='12' y='4' class='st2' width='1' height='8'/%3E %3Crect x='8.5' y='7.5' transform='matrix(0.866 -0.5 0.5 0.866 -2.3255 7.3219)' class='st2' width='8' height='1'/%3E %3Crect x='12' y='4' transform='matrix(0.5 -0.866 0.866 0.5 -0.6779 14.8252)' class='st2' width='1' height='8'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-run: url("data:image/svg+xml,%3Csvg height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M8 5v14l11-7z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-running: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 512 512'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm96 328c0 8.8-7.2 16-16 16H176c-8.8 0-16-7.2-16-16V176c0-8.8 7.2-16 16-16h160c8.8 0 16 7.2 16 16v160z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-save: url("data:image/svg+xml,%3Csvg height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M17 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V7l-4-4zm-5 16c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-10H5V5h10v4z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-search: url("data:image/svg+xml,%3Csvg viewBox='0 0 18 18' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M12.1,10.9h-0.7l-0.2-0.2c0.8-0.9,1.3-2.2,1.3-3.5c0-3-2.4-5.4-5.4-5.4S1.8,4.2,1.8,7.1s2.4,5.4,5.4,5.4 c1.3,0,2.5-0.5,3.5-1.3l0.2,0.2v0.7l4.1,4.1l1.2-1.2L12.1,10.9z M7.1,10.9c-2.1,0-3.7-1.7-3.7-3.7s1.7-3.7,3.7-3.7s3.7,1.7,3.7,3.7 S9.2,10.9,7.1,10.9z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-settings: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon3 jp-icon-selectable' fill='%23616161' d='M19.43 12.98c.04-.32.07-.64.07-.98s-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65A.488.488 0 0014 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.23-.09-.49 0-.61.22l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.12.22.39.3.61.22l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.23.09.49 0 .61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5 3.5 1.57 3.5 3.5-1.57 3.5-3.5 3.5z'/%3E %3C/svg%3E");
  --jp-icon-spreadsheet: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cpath class='jp-icon-contrast1 jp-icon-selectable' fill='%234CAF50' d='M2.2 2.2v17.6h17.6V2.2H2.2zm15.4 7.7h-5.5V4.4h5.5v5.5zM9.9 4.4v5.5H4.4V4.4h5.5zm-5.5 7.7h5.5v5.5H4.4v-5.5zm7.7 5.5v-5.5h5.5v5.5h-5.5z'/%3E %3C/svg%3E");
  --jp-icon-stop: url("data:image/svg+xml,%3Csvg height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M0 0h24v24H0z' fill='none'/%3E %3Cpath d='M6 6h12v12H6z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-tab: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h10v4h8v10z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-terminal: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24' %3E %3Crect class='jp-icon2 jp-icon-selectable' width='20' height='20' transform='translate(2 2)' fill='%23333333'/%3E %3Cpath class='jp-icon-accent2 jp-icon-selectable-inverse' d='M5.05664 8.76172C5.05664 8.59766 5.03125 8.45312 4.98047 8.32812C4.93359 8.19922 4.85547 8.08203 4.74609 7.97656C4.64062 7.87109 4.5 7.77539 4.32422 7.68945C4.15234 7.59961 3.94336 7.51172 3.69727 7.42578C3.30273 7.28516 2.94336 7.13672 2.61914 6.98047C2.29492 6.82422 2.01758 6.64258 1.78711 6.43555C1.56055 6.22852 1.38477 5.98828 1.25977 5.71484C1.13477 5.4375 1.07227 5.10938 1.07227 4.73047C1.07227 4.39844 1.12891 4.0957 1.24219 3.82227C1.35547 3.54492 1.51562 3.30469 1.72266 3.10156C1.92969 2.89844 2.17969 2.73437 2.47266 2.60938C2.76562 2.48438 3.0918 2.4043 3.45117 2.36914V1.10938H4.38867V2.38086C4.74023 2.42773 5.05664 2.52344 5.33789 2.66797C5.61914 2.8125 5.85742 3.00195 6.05273 3.23633C6.25195 3.4668 6.4043 3.74023 6.50977 4.05664C6.61914 4.36914 6.67383 4.7207 6.67383 5.11133H5.04492C5.04492 4.63867 4.9375 4.28125 4.72266 4.03906C4.50781 3.79297 4.2168 3.66992 3.84961 3.66992C3.65039 3.66992 3.47656 3.69727 3.32812 3.75195C3.18359 3.80273 3.06445 3.87695 2.9707 3.97461C2.87695 4.06836 2.80664 4.17969 2.75977 4.30859C2.7168 4.4375 2.69531 4.57812 2.69531 4.73047C2.69531 4.88281 2.7168 5.01953 2.75977 5.14062C2.80664 5.25781 2.88281 5.36719 2.98828 5.46875C3.09766 5.57031 3.24023 5.66797 3.41602 5.76172C3.5918 5.85156 3.81055 5.94336 4.07227 6.03711C4.4668 6.18555 4.82422 6.33984 5.14453 6.5C5.46484 6.65625 5.73828 6.83984 5.96484 7.05078C6.19531 7.25781 6.37109 7.5 6.49219 7.77734C6.61719 8.05078 6.67969 8.375 6.67969 8.75C6.67969 9.09375 6.62305 9.4043 6.50977 9.68164C6.39648 9.95508 6.23438 10.1914 6.02344 10.3906C5.8125 10.5898 5.55859 10.75 5.26172 10.8711C4.96484 10.9883 4.63281 11.0645 4.26562 11.0996V12.248H3.33398V11.0996C3.00195 11.0684 2.67969 10.9961 2.36719 10.8828C2.05469 10.7656 1.77734 10.5977 1.53516 10.3789C1.29688 10.1602 1.10547 9.88477 0.960938 9.55273C0.816406 9.2168 0.744141 8.81445 0.744141 8.3457H2.37891C2.37891 8.62695 2.41992 8.86328 2.50195 9.05469C2.58398 9.24219 2.68945 9.39258 2.81836 9.50586C2.95117 9.61523 3.10156 9.69336 3.26953 9.74023C3.4375 9.78711 3.60938 9.81055 3.78516 9.81055C4.20312 9.81055 4.51953 9.71289 4.73438 9.51758C4.94922 9.32227 5.05664 9.07031 5.05664 8.76172ZM13.418 12.2715H8.07422V11H13.418V12.2715Z' transform='translate(3.95264 6)' fill='white'/%3E %3C/svg%3E");
  --jp-icon-text-editor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 24'%3E %3Cpath class='jp-icon3 jp-icon-selectable' fill='%23616161' d='M15 15H3v2h12v-2zm0-8H3v2h12V7zM3 13h18v-2H3v2zm0 8h18v-2H3v2zM3 3v2h18V3H3z'/%3E %3C/svg%3E");
  --jp-icon-trusted: url("data:image/svg+xml,%3Csvg fill='none' xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 24 25'%3E %3Cpath class='jp-icon2' stroke='%23333333' stroke-width='2' transform='translate(2 3)' d='M1.86094 11.4409C0.826448 8.77027 0.863779 6.05764 1.24907 4.19932C2.48206 3.93347 4.08068 3.40347 5.60102 2.8449C7.23549 2.2444 8.85666 1.5815 9.9876 1.09539C11.0597 1.58341 12.6094 2.2444 14.218 2.84339C15.7503 3.41394 17.3995 3.95258 18.7539 4.21385C19.1364 6.07177 19.1709 8.77722 18.139 11.4409C17.0303 14.3032 14.6668 17.1844 9.99999 18.9354C5.3332 17.1844 2.96968 14.3032 1.86094 11.4409Z'/%3E %3Cpath class='jp-icon2' fill='%23333333' stroke='%23333333' transform='translate(8 9.86719)' d='M2.86015 4.86535L0.726549 2.99959L0 3.63045L2.86015 6.13157L8 0.630872L7.27857 0L2.86015 4.86535Z'/%3E %3C/svg%3E");
  --jp-icon-undo: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M12.5 8c-2.65 0-5.05.99-6.9 2.6L2 7v9h9l-3.62-3.62c1.39-1.16 3.16-1.88 5.12-1.88 3.54 0 6.55 2.31 7.6 5.5l2.37-.78C21.08 11.03 17.15 8 12.5 8z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-vega: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cg class='jp-icon1 jp-icon-selectable' fill='%23212121'%3E %3Cpath d='M10.6 5.4l2.2-3.2H2.2v7.3l4-6.6z'/%3E %3Cpath d='M15.8 2.2l-4.4 6.6L7 6.3l-4.8 8v5.5h17.6V2.2h-4zm-7 15.4H5.5v-4.4h3.3v4.4zm4.4 0H9.8V9.8h3.4v7.8zm4.4 0h-3.4V6.5h3.4v11.1z'/%3E %3C/g%3E %3C/svg%3E");
  --jp-icon-yaml: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' viewBox='0 0 22 22'%3E %3Cg class='jp-icon-contrast2 jp-icon-selectable' fill='%23D81B60'%3E %3Cpath d='M7.2 18.6v-5.4L3 5.6h3.3l1.4 3.1c.3.9.6 1.6 1 2.5.3-.8.6-1.6 1-2.5l1.4-3.1h3.4l-4.4 7.6v5.5l-2.9-.1z'/%3E %3Ccircle class='st0' cx='17.6' cy='16.5' r='2.1'/%3E %3Ccircle class='st0' cx='17.6' cy='11' r='2.1'/%3E %3C/g%3E %3C/svg%3E");
}

/* Icon CSS class declarations */

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}
.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}
.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}
.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}
.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}
.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}
.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}
.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}
.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}
.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}
.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}
.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}
.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}
.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}
.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}
.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}
.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}
.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}
.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}
.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}
.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}
.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}
.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}
.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}
.jp-FileIcon {
  background-image: var(--jp-icon-file);
}
.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}
.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}
.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}
.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}
.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}
.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}
.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}
.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}
.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}
.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}
.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}
.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}
.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}
.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}
.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}
.jp-ListIcon {
  background-image: var(--jp-icon-list);
}
.jp-ListingsInfoIcon {
  background-image: var(--jp-icon-listings-info);
}
.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}
.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}
.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}
.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}
.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}
.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}
.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}
.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}
.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}
.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}
.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}
.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}
.jp-RunIcon {
  background-image: var(--jp-icon-run);
}
.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}
.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}
.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}
.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}
.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}
.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}
.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}
.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}
.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}
.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}
.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}
.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}
.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

:root {
  --jp-icon-search-white: url("data:image/svg+xml,%3Csvg viewBox='0 0 18 18' width='16' xmlns='http://www.w3.org/2000/svg'%3E %3Cg class='jp-icon3' fill='%23616161'%3E %3Cpath d='M12.1,10.9h-0.7l-0.2-0.2c0.8-0.9,1.3-2.2,1.3-3.5c0-3-2.4-5.4-5.4-5.4S1.8,4.2,1.8,7.1s2.4,5.4,5.4,5.4 c1.3,0,2.5-0.5,3.5-1.3l0.2,0.2v0.7l4.1,4.1l1.2-1.2L12.1,10.9z M7.1,10.9c-2.1,0-3.7-1.7-3.7-3.7s1.7-3.7,3.7-3.7s3.7,1.7,3.7,3.7 S9.2,10.9,7.1,10.9z'/%3E %3C/g%3E %3C/svg%3E");
}

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}
/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}
/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}
.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}
.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}
.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}
.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}
.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}
.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}
.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}
.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}
/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}
.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}
.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}
.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}
.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}
.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}
.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}
/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

/* CSS for icons in selected items in the settings editor */
#setting-editor .jp-PluginList .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
#setting-editor
  .jp-PluginList
  .jp-mod-selected
  .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected tabs in the sidebar tab manager */
#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable[fill] {
  fill: #fff;
}

#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable[fill] {
  fill: var(--jp-brand-color1);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable-inverse[fill] {
  fill: #fff;
}

/**
 * TODO: come up with non css-hack solution for showing the busy icon on top
 *  of the close icon
 * CSS for complex behavior of close icon of tabs in the sidebar tab manager
 */
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-dirty.jp-mod-active
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: #fff;
}

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) svg {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

/* Override Blueprint's _reset.scss styles */
html {
  box-sizing: unset;
}

*,
*::before,
*::after {
  box-sizing: unset;
}

body {
  color: unset;
  font-family: var(--jp-ui-font-family);
}

p {
  margin-top: unset;
  margin-bottom: unset;
}

small {
  font-size: unset;
}

strong {
  font-weight: unset;
}

/* Override Blueprint's _typography.scss styles */
a {
  text-decoration: unset;
  color: unset;
}
a:hover {
  text-decoration: unset;
  color: unset;
}

/* Override Blueprint's _accessibility.scss styles */
:focus {
  outline: unset;
  outline-offset: unset;
  -moz-outline-radius: unset;
}

/* Styles for ui-components */
.jp-Button {
  border-radius: var(--jp-border-radius);
  padding: 0px 12px;
  font-size: var(--jp-ui-font-size1);
}

/* Use our own theme for hover styles */
button.jp-Button.bp3-button.bp3-minimal:hover {
  background-color: var(--jp-layout-color2);
}
.jp-Button.minimal {
  color: unset !important;
}

.jp-Button.jp-ToolbarButtonComponent {
  text-transform: none;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color3);
}

.jp-BPIcon {
  display: inline-block;
  vertical-align: middle;
  margin: auto;
}

/* Stop blueprint futzing with our icon fills */
.bp3-icon.jp-BPIcon > svg:not([fill]) {
  fill: var(--jp-inverse-layout-color3);
}

.jp-InputGroupAction {
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

/* Use our own theme for hover and option styles */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}
select {
  box-sizing: border-box;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*!
 * Font Awesome Free 5.14.0 by @fontawesome - https://fontawesome.com
 * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
 */
.fa,.fab,.fad,.fal,.far,.fas{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;display:inline-block;font-style:normal;font-variant:normal;text-rendering:auto;line-height:1}.fa-lg{font-size:1.33333em;line-height:.75em;vertical-align:-.0667em}.fa-xs{font-size:.75em}.fa-sm{font-size:.875em}.fa-1x{font-size:1em}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-6x{font-size:6em}.fa-7x{font-size:7em}.fa-8x{font-size:8em}.fa-9x{font-size:9em}.fa-10x{font-size:10em}.fa-fw{text-align:center;width:1.25em}.fa-ul{list-style-type:none;margin-left:2.5em;padding-left:0}.fa-ul>li{position:relative}.fa-li{left:-2em;position:absolute;text-align:center;width:2em;line-height:inherit}.fa-border{border:.08em solid #eee;border-radius:.1em;padding:.2em .25em .15em}.fa-pull-left{float:left}.fa-pull-right{float:right}.fa.fa-pull-left,.fab.fa-pull-left,.fal.fa-pull-left,.far.fa-pull-left,.fas.fa-pull-left{margin-right:.3em}.fa.fa-pull-right,.fab.fa-pull-right,.fal.fa-pull-right,.far.fa-pull-right,.fas.fa-pull-right{margin-left:.3em}.fa-spin{-webkit-animation:fa-spin 2s linear infinite;animation:fa-spin 2s linear infinite}.fa-pulse{-webkit-animation:fa-spin 1s steps(8) infinite;animation:fa-spin 1s steps(8) infinite}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}.fa-rotate-90{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";-webkit-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";-webkit-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";-webkit-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";-webkit-transform:scaleX(-1);transform:scaleX(-1)}.fa-flip-vertical{-webkit-transform:scaleY(-1);transform:scaleY(-1)}.fa-flip-both,.fa-flip-horizontal.fa-flip-vertical,.fa-flip-vertical{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)"}.fa-flip-both,.fa-flip-horizontal.fa-flip-vertical{-webkit-transform:scale(-1);transform:scale(-1)}:root .fa-flip-both,:root .fa-flip-horizontal,:root .fa-flip-vertical,:root .fa-rotate-90,:root .fa-rotate-180,:root .fa-rotate-270{-webkit-filter:none;filter:none}.fa-stack{display:inline-block;height:2em;line-height:2em;position:relative;vertical-align:middle;width:2.5em}.fa-stack-1x,.fa-stack-2x{left:0;position:absolute;text-align:center;width:100%}.fa-stack-1x{line-height:inherit}.fa-stack-2x{font-size:2em}.fa-inverse{color:#fff}.fa-500px:before{content:"\f26e"}.fa-accessible-icon:before{content:"\f368"}.fa-accusoft:before{content:"\f369"}.fa-acquisitions-incorporated:before{content:"\f6af"}.fa-ad:before{content:"\f641"}.fa-address-book:before{content:"\f2b9"}.fa-address-card:before{content:"\f2bb"}.fa-adjust:before{content:"\f042"}.fa-adn:before{content:"\f170"}.fa-adobe:before{content:"\f778"}.fa-adversal:before{content:"\f36a"}.fa-affiliatetheme:before{content:"\f36b"}.fa-air-freshener:before{content:"\f5d0"}.fa-airbnb:before{content:"\f834"}.fa-algolia:before{content:"\f36c"}.fa-align-center:before{content:"\f037"}.fa-align-justify:before{content:"\f039"}.fa-align-left:before{content:"\f036"}.fa-align-right:before{content:"\f038"}.fa-alipay:before{content:"\f642"}.fa-allergies:before{content:"\f461"}.fa-amazon:before{content:"\f270"}.fa-amazon-pay:before{content:"\f42c"}.fa-ambulance:before{content:"\f0f9"}.fa-american-sign-language-interpreting:before{content:"\f2a3"}.fa-amilia:before{content:"\f36d"}.fa-anchor:before{content:"\f13d"}.fa-android:before{content:"\f17b"}.fa-angellist:before{content:"\f209"}.fa-angle-double-down:before{content:"\f103"}.fa-angle-double-left:before{content:"\f100"}.fa-angle-double-right:before{content:"\f101"}.fa-angle-double-up:before{content:"\f102"}.fa-angle-down:before{content:"\f107"}.fa-angle-left:before{content:"\f104"}.fa-angle-right:before{content:"\f105"}.fa-angle-up:before{content:"\f106"}.fa-angry:before{content:"\f556"}.fa-angrycreative:before{content:"\f36e"}.fa-angular:before{content:"\f420"}.fa-ankh:before{content:"\f644"}.fa-app-store:before{content:"\f36f"}.fa-app-store-ios:before{content:"\f370"}.fa-apper:before{content:"\f371"}.fa-apple:before{content:"\f179"}.fa-apple-alt:before{content:"\f5d1"}.fa-apple-pay:before{content:"\f415"}.fa-archive:before{content:"\f187"}.fa-archway:before{content:"\f557"}.fa-arrow-alt-circle-down:before{content:"\f358"}.fa-arrow-alt-circle-left:before{content:"\f359"}.fa-arrow-alt-circle-right:before{content:"\f35a"}.fa-arrow-alt-circle-up:before{content:"\f35b"}.fa-arrow-circle-down:before{content:"\f0ab"}.fa-arrow-circle-left:before{content:"\f0a8"}.fa-arrow-circle-right:before{content:"\f0a9"}.fa-arrow-circle-up:before{content:"\f0aa"}.fa-arrow-down:before{content:"\f063"}.fa-arrow-left:before{content:"\f060"}.fa-arrow-right:before{content:"\f061"}.fa-arrow-up:before{content:"\f062"}.fa-arrows-alt:before{content:"\f0b2"}.fa-arrows-alt-h:before{content:"\f337"}.fa-arrows-alt-v:before{content:"\f338"}.fa-artstation:before{content:"\f77a"}.fa-assistive-listening-systems:before{content:"\f2a2"}.fa-asterisk:before{content:"\f069"}.fa-asymmetrik:before{content:"\f372"}.fa-at:before{content:"\f1fa"}.fa-atlas:before{content:"\f558"}.fa-atlassian:before{content:"\f77b"}.fa-atom:before{content:"\f5d2"}.fa-audible:before{content:"\f373"}.fa-audio-description:before{content:"\f29e"}.fa-autoprefixer:before{content:"\f41c"}.fa-avianex:before{content:"\f374"}.fa-aviato:before{content:"\f421"}.fa-award:before{content:"\f559"}.fa-aws:before{content:"\f375"}.fa-baby:before{content:"\f77c"}.fa-baby-carriage:before{content:"\f77d"}.fa-backspace:before{content:"\f55a"}.fa-backward:before{content:"\f04a"}.fa-bacon:before{content:"\f7e5"}.fa-bacteria:before{content:"\e059"}.fa-bacterium:before{content:"\e05a"}.fa-bahai:before{content:"\f666"}.fa-balance-scale:before{content:"\f24e"}.fa-balance-scale-left:before{content:"\f515"}.fa-balance-scale-right:before{content:"\f516"}.fa-ban:before{content:"\f05e"}.fa-band-aid:before{content:"\f462"}.fa-bandcamp:before{content:"\f2d5"}.fa-barcode:before{content:"\f02a"}.fa-bars:before{content:"\f0c9"}.fa-baseball-ball:before{content:"\f433"}.fa-basketball-ball:before{content:"\f434"}.fa-bath:before{content:"\f2cd"}.fa-battery-empty:before{content:"\f244"}.fa-battery-full:before{content:"\f240"}.fa-battery-half:before{content:"\f242"}.fa-battery-quarter:before{content:"\f243"}.fa-battery-three-quarters:before{content:"\f241"}.fa-battle-net:before{content:"\f835"}.fa-bed:before{content:"\f236"}.fa-beer:before{content:"\f0fc"}.fa-behance:before{content:"\f1b4"}.fa-behance-square:before{content:"\f1b5"}.fa-bell:before{content:"\f0f3"}.fa-bell-slash:before{content:"\f1f6"}.fa-bezier-curve:before{content:"\f55b"}.fa-bible:before{content:"\f647"}.fa-bicycle:before{content:"\f206"}.fa-biking:before{content:"\f84a"}.fa-bimobject:before{content:"\f378"}.fa-binoculars:before{content:"\f1e5"}.fa-biohazard:before{content:"\f780"}.fa-birthday-cake:before{content:"\f1fd"}.fa-bitbucket:before{content:"\f171"}.fa-bitcoin:before{content:"\f379"}.fa-bity:before{content:"\f37a"}.fa-black-tie:before{content:"\f27e"}.fa-blackberry:before{content:"\f37b"}.fa-blender:before{content:"\f517"}.fa-blender-phone:before{content:"\f6b6"}.fa-blind:before{content:"\f29d"}.fa-blog:before{content:"\f781"}.fa-blogger:before{content:"\f37c"}.fa-blogger-b:before{content:"\f37d"}.fa-bluetooth:before{content:"\f293"}.fa-bluetooth-b:before{content:"\f294"}.fa-bold:before{content:"\f032"}.fa-bolt:before{content:"\f0e7"}.fa-bomb:before{content:"\f1e2"}.fa-bone:before{content:"\f5d7"}.fa-bong:before{content:"\f55c"}.fa-book:before{content:"\f02d"}.fa-book-dead:before{content:"\f6b7"}.fa-book-medical:before{content:"\f7e6"}.fa-book-open:before{content:"\f518"}.fa-book-reader:before{content:"\f5da"}.fa-bookmark:before{content:"\f02e"}.fa-bootstrap:before{content:"\f836"}.fa-border-all:before{content:"\f84c"}.fa-border-none:before{content:"\f850"}.fa-border-style:before{content:"\f853"}.fa-bowling-ball:before{content:"\f436"}.fa-box:before{content:"\f466"}.fa-box-open:before{content:"\f49e"}.fa-box-tissue:before{content:"\e05b"}.fa-boxes:before{content:"\f468"}.fa-braille:before{content:"\f2a1"}.fa-brain:before{content:"\f5dc"}.fa-bread-slice:before{content:"\f7ec"}.fa-briefcase:before{content:"\f0b1"}.fa-briefcase-medical:before{content:"\f469"}.fa-broadcast-tower:before{content:"\f519"}.fa-broom:before{content:"\f51a"}.fa-brush:before{content:"\f55d"}.fa-btc:before{content:"\f15a"}.fa-buffer:before{content:"\f837"}.fa-bug:before{content:"\f188"}.fa-building:before{content:"\f1ad"}.fa-bullhorn:before{content:"\f0a1"}.fa-bullseye:before{content:"\f140"}.fa-burn:before{content:"\f46a"}.fa-buromobelexperte:before{content:"\f37f"}.fa-bus:before{content:"\f207"}.fa-bus-alt:before{content:"\f55e"}.fa-business-time:before{content:"\f64a"}.fa-buy-n-large:before{content:"\f8a6"}.fa-buysellads:before{content:"\f20d"}.fa-calculator:before{content:"\f1ec"}.fa-calendar:before{content:"\f133"}.fa-calendar-alt:before{content:"\f073"}.fa-calendar-check:before{content:"\f274"}.fa-calendar-day:before{content:"\f783"}.fa-calendar-minus:before{content:"\f272"}.fa-calendar-plus:before{content:"\f271"}.fa-calendar-times:before{content:"\f273"}.fa-calendar-week:before{content:"\f784"}.fa-camera:before{content:"\f030"}.fa-camera-retro:before{content:"\f083"}.fa-campground:before{content:"\f6bb"}.fa-canadian-maple-leaf:before{content:"\f785"}.fa-candy-cane:before{content:"\f786"}.fa-cannabis:before{content:"\f55f"}.fa-capsules:before{content:"\f46b"}.fa-car:before{content:"\f1b9"}.fa-car-alt:before{content:"\f5de"}.fa-car-battery:before{content:"\f5df"}.fa-car-crash:before{content:"\f5e1"}.fa-car-side:before{content:"\f5e4"}.fa-caravan:before{content:"\f8ff"}.fa-caret-down:before{content:"\f0d7"}.fa-caret-left:before{content:"\f0d9"}.fa-caret-right:before{content:"\f0da"}.fa-caret-square-down:before{content:"\f150"}.fa-caret-square-left:before{content:"\f191"}.fa-caret-square-right:before{content:"\f152"}.fa-caret-square-up:before{content:"\f151"}.fa-caret-up:before{content:"\f0d8"}.fa-carrot:before{content:"\f787"}.fa-cart-arrow-down:before{content:"\f218"}.fa-cart-plus:before{content:"\f217"}.fa-cash-register:before{content:"\f788"}.fa-cat:before{content:"\f6be"}.fa-cc-amazon-pay:before{content:"\f42d"}.fa-cc-amex:before{content:"\f1f3"}.fa-cc-apple-pay:before{content:"\f416"}.fa-cc-diners-club:before{content:"\f24c"}.fa-cc-discover:before{content:"\f1f2"}.fa-cc-jcb:before{content:"\f24b"}.fa-cc-mastercard:before{content:"\f1f1"}.fa-cc-paypal:before{content:"\f1f4"}.fa-cc-stripe:before{content:"\f1f5"}.fa-cc-visa:before{content:"\f1f0"}.fa-centercode:before{content:"\f380"}.fa-centos:before{content:"\f789"}.fa-certificate:before{content:"\f0a3"}.fa-chair:before{content:"\f6c0"}.fa-chalkboard:before{content:"\f51b"}.fa-chalkboard-teacher:before{content:"\f51c"}.fa-charging-station:before{content:"\f5e7"}.fa-chart-area:before{content:"\f1fe"}.fa-chart-bar:before{content:"\f080"}.fa-chart-line:before{content:"\f201"}.fa-chart-pie:before{content:"\f200"}.fa-check:before{content:"\f00c"}.fa-check-circle:before{content:"\f058"}.fa-check-double:before{content:"\f560"}.fa-check-square:before{content:"\f14a"}.fa-cheese:before{content:"\f7ef"}.fa-chess:before{content:"\f439"}.fa-chess-bishop:before{content:"\f43a"}.fa-chess-board:before{content:"\f43c"}.fa-chess-king:before{content:"\f43f"}.fa-chess-knight:before{content:"\f441"}.fa-chess-pawn:before{content:"\f443"}.fa-chess-queen:before{content:"\f445"}.fa-chess-rook:before{content:"\f447"}.fa-chevron-circle-down:before{content:"\f13a"}.fa-chevron-circle-left:before{content:"\f137"}.fa-chevron-circle-right:before{content:"\f138"}.fa-chevron-circle-up:before{content:"\f139"}.fa-chevron-down:before{content:"\f078"}.fa-chevron-left:before{content:"\f053"}.fa-chevron-right:before{content:"\f054"}.fa-chevron-up:before{content:"\f077"}.fa-child:before{content:"\f1ae"}.fa-chrome:before{content:"\f268"}.fa-chromecast:before{content:"\f838"}.fa-church:before{content:"\f51d"}.fa-circle:before{content:"\f111"}.fa-circle-notch:before{content:"\f1ce"}.fa-city:before{content:"\f64f"}.fa-clinic-medical:before{content:"\f7f2"}.fa-clipboard:before{content:"\f328"}.fa-clipboard-check:before{content:"\f46c"}.fa-clipboard-list:before{content:"\f46d"}.fa-clock:before{content:"\f017"}.fa-clone:before{content:"\f24d"}.fa-closed-captioning:before{content:"\f20a"}.fa-cloud:before{content:"\f0c2"}.fa-cloud-download-alt:before{content:"\f381"}.fa-cloud-meatball:before{content:"\f73b"}.fa-cloud-moon:before{content:"\f6c3"}.fa-cloud-moon-rain:before{content:"\f73c"}.fa-cloud-rain:before{content:"\f73d"}.fa-cloud-showers-heavy:before{content:"\f740"}.fa-cloud-sun:before{content:"\f6c4"}.fa-cloud-sun-rain:before{content:"\f743"}.fa-cloud-upload-alt:before{content:"\f382"}.fa-cloudscale:before{content:"\f383"}.fa-cloudsmith:before{content:"\f384"}.fa-cloudversify:before{content:"\f385"}.fa-cocktail:before{content:"\f561"}.fa-code:before{content:"\f121"}.fa-code-branch:before{content:"\f126"}.fa-codepen:before{content:"\f1cb"}.fa-codiepie:before{content:"\f284"}.fa-coffee:before{content:"\f0f4"}.fa-cog:before{content:"\f013"}.fa-cogs:before{content:"\f085"}.fa-coins:before{content:"\f51e"}.fa-columns:before{content:"\f0db"}.fa-comment:before{content:"\f075"}.fa-comment-alt:before{content:"\f27a"}.fa-comment-dollar:before{content:"\f651"}.fa-comment-dots:before{content:"\f4ad"}.fa-comment-medical:before{content:"\f7f5"}.fa-comment-slash:before{content:"\f4b3"}.fa-comments:before{content:"\f086"}.fa-comments-dollar:before{content:"\f653"}.fa-compact-disc:before{content:"\f51f"}.fa-compass:before{content:"\f14e"}.fa-compress:before{content:"\f066"}.fa-compress-alt:before{content:"\f422"}.fa-compress-arrows-alt:before{content:"\f78c"}.fa-concierge-bell:before{content:"\f562"}.fa-confluence:before{content:"\f78d"}.fa-connectdevelop:before{content:"\f20e"}.fa-contao:before{content:"\f26d"}.fa-cookie:before{content:"\f563"}.fa-cookie-bite:before{content:"\f564"}.fa-copy:before{content:"\f0c5"}.fa-copyright:before{content:"\f1f9"}.fa-cotton-bureau:before{content:"\f89e"}.fa-couch:before{content:"\f4b8"}.fa-cpanel:before{content:"\f388"}.fa-creative-commons:before{content:"\f25e"}.fa-creative-commons-by:before{content:"\f4e7"}.fa-creative-commons-nc:before{content:"\f4e8"}.fa-creative-commons-nc-eu:before{content:"\f4e9"}.fa-creative-commons-nc-jp:before{content:"\f4ea"}.fa-creative-commons-nd:before{content:"\f4eb"}.fa-creative-commons-pd:before{content:"\f4ec"}.fa-creative-commons-pd-alt:before{content:"\f4ed"}.fa-creative-commons-remix:before{content:"\f4ee"}.fa-creative-commons-sa:before{content:"\f4ef"}.fa-creative-commons-sampling:before{content:"\f4f0"}.fa-creative-commons-sampling-plus:before{content:"\f4f1"}.fa-creative-commons-share:before{content:"\f4f2"}.fa-creative-commons-zero:before{content:"\f4f3"}.fa-credit-card:before{content:"\f09d"}.fa-critical-role:before{content:"\f6c9"}.fa-crop:before{content:"\f125"}.fa-crop-alt:before{content:"\f565"}.fa-cross:before{content:"\f654"}.fa-crosshairs:before{content:"\f05b"}.fa-crow:before{content:"\f520"}.fa-crown:before{content:"\f521"}.fa-crutch:before{content:"\f7f7"}.fa-css3:before{content:"\f13c"}.fa-css3-alt:before{content:"\f38b"}.fa-cube:before{content:"\f1b2"}.fa-cubes:before{content:"\f1b3"}.fa-cut:before{content:"\f0c4"}.fa-cuttlefish:before{content:"\f38c"}.fa-d-and-d:before{content:"\f38d"}.fa-d-and-d-beyond:before{content:"\f6ca"}.fa-dailymotion:before{content:"\e052"}.fa-dashcube:before{content:"\f210"}.fa-database:before{content:"\f1c0"}.fa-deaf:before{content:"\f2a4"}.fa-deezer:before{content:"\e077"}.fa-delicious:before{content:"\f1a5"}.fa-democrat:before{content:"\f747"}.fa-deploydog:before{content:"\f38e"}.fa-deskpro:before{content:"\f38f"}.fa-desktop:before{content:"\f108"}.fa-dev:before{content:"\f6cc"}.fa-deviantart:before{content:"\f1bd"}.fa-dharmachakra:before{content:"\f655"}.fa-dhl:before{content:"\f790"}.fa-diagnoses:before{content:"\f470"}.fa-diaspora:before{content:"\f791"}.fa-dice:before{content:"\f522"}.fa-dice-d20:before{content:"\f6cf"}.fa-dice-d6:before{content:"\f6d1"}.fa-dice-five:before{content:"\f523"}.fa-dice-four:before{content:"\f524"}.fa-dice-one:before{content:"\f525"}.fa-dice-six:before{content:"\f526"}.fa-dice-three:before{content:"\f527"}.fa-dice-two:before{content:"\f528"}.fa-digg:before{content:"\f1a6"}.fa-digital-ocean:before{content:"\f391"}.fa-digital-tachograph:before{content:"\f566"}.fa-directions:before{content:"\f5eb"}.fa-discord:before{content:"\f392"}.fa-discourse:before{content:"\f393"}.fa-disease:before{content:"\f7fa"}.fa-divide:before{content:"\f529"}.fa-dizzy:before{content:"\f567"}.fa-dna:before{content:"\f471"}.fa-dochub:before{content:"\f394"}.fa-docker:before{content:"\f395"}.fa-dog:before{content:"\f6d3"}.fa-dollar-sign:before{content:"\f155"}.fa-dolly:before{content:"\f472"}.fa-dolly-flatbed:before{content:"\f474"}.fa-donate:before{content:"\f4b9"}.fa-door-closed:before{content:"\f52a"}.fa-door-open:before{content:"\f52b"}.fa-dot-circle:before{content:"\f192"}.fa-dove:before{content:"\f4ba"}.fa-download:before{content:"\f019"}.fa-draft2digital:before{content:"\f396"}.fa-drafting-compass:before{content:"\f568"}.fa-dragon:before{content:"\f6d5"}.fa-draw-polygon:before{content:"\f5ee"}.fa-dribbble:before{content:"\f17d"}.fa-dribbble-square:before{content:"\f397"}.fa-dropbox:before{content:"\f16b"}.fa-drum:before{content:"\f569"}.fa-drum-steelpan:before{content:"\f56a"}.fa-drumstick-bite:before{content:"\f6d7"}.fa-drupal:before{content:"\f1a9"}.fa-dumbbell:before{content:"\f44b"}.fa-dumpster:before{content:"\f793"}.fa-dumpster-fire:before{content:"\f794"}.fa-dungeon:before{content:"\f6d9"}.fa-dyalog:before{content:"\f399"}.fa-earlybirds:before{content:"\f39a"}.fa-ebay:before{content:"\f4f4"}.fa-edge:before{content:"\f282"}.fa-edge-legacy:before{content:"\e078"}.fa-edit:before{content:"\f044"}.fa-egg:before{content:"\f7fb"}.fa-eject:before{content:"\f052"}.fa-elementor:before{content:"\f430"}.fa-ellipsis-h:before{content:"\f141"}.fa-ellipsis-v:before{content:"\f142"}.fa-ello:before{content:"\f5f1"}.fa-ember:before{content:"\f423"}.fa-empire:before{content:"\f1d1"}.fa-envelope:before{content:"\f0e0"}.fa-envelope-open:before{content:"\f2b6"}.fa-envelope-open-text:before{content:"\f658"}.fa-envelope-square:before{content:"\f199"}.fa-envira:before{content:"\f299"}.fa-equals:before{content:"\f52c"}.fa-eraser:before{content:"\f12d"}.fa-erlang:before{content:"\f39d"}.fa-ethereum:before{content:"\f42e"}.fa-ethernet:before{content:"\f796"}.fa-etsy:before{content:"\f2d7"}.fa-euro-sign:before{content:"\f153"}.fa-evernote:before{content:"\f839"}.fa-exchange-alt:before{content:"\f362"}.fa-exclamation:before{content:"\f12a"}.fa-exclamation-circle:before{content:"\f06a"}.fa-exclamation-triangle:before{content:"\f071"}.fa-expand:before{content:"\f065"}.fa-expand-alt:before{content:"\f424"}.fa-expand-arrows-alt:before{content:"\f31e"}.fa-expeditedssl:before{content:"\f23e"}.fa-external-link-alt:before{content:"\f35d"}.fa-external-link-square-alt:before{content:"\f360"}.fa-eye:before{content:"\f06e"}.fa-eye-dropper:before{content:"\f1fb"}.fa-eye-slash:before{content:"\f070"}.fa-facebook:before{content:"\f09a"}.fa-facebook-f:before{content:"\f39e"}.fa-facebook-messenger:before{content:"\f39f"}.fa-facebook-square:before{content:"\f082"}.fa-fan:before{content:"\f863"}.fa-fantasy-flight-games:before{content:"\f6dc"}.fa-fast-backward:before{content:"\f049"}.fa-fast-forward:before{content:"\f050"}.fa-faucet:before{content:"\e005"}.fa-fax:before{content:"\f1ac"}.fa-feather:before{content:"\f52d"}.fa-feather-alt:before{content:"\f56b"}.fa-fedex:before{content:"\f797"}.fa-fedora:before{content:"\f798"}.fa-female:before{content:"\f182"}.fa-fighter-jet:before{content:"\f0fb"}.fa-figma:before{content:"\f799"}.fa-file:before{content:"\f15b"}.fa-file-alt:before{content:"\f15c"}.fa-file-archive:before{content:"\f1c6"}.fa-file-audio:before{content:"\f1c7"}.fa-file-code:before{content:"\f1c9"}.fa-file-contract:before{content:"\f56c"}.fa-file-csv:before{content:"\f6dd"}.fa-file-download:before{content:"\f56d"}.fa-file-excel:before{content:"\f1c3"}.fa-file-export:before{content:"\f56e"}.fa-file-image:before{content:"\f1c5"}.fa-file-import:before{content:"\f56f"}.fa-file-invoice:before{content:"\f570"}.fa-file-invoice-dollar:before{content:"\f571"}.fa-file-medical:before{content:"\f477"}.fa-file-medical-alt:before{content:"\f478"}.fa-file-pdf:before{content:"\f1c1"}.fa-file-powerpoint:before{content:"\f1c4"}.fa-file-prescription:before{content:"\f572"}.fa-file-signature:before{content:"\f573"}.fa-file-upload:before{content:"\f574"}.fa-file-video:before{content:"\f1c8"}.fa-file-word:before{content:"\f1c2"}.fa-fill:before{content:"\f575"}.fa-fill-drip:before{content:"\f576"}.fa-film:before{content:"\f008"}.fa-filter:before{content:"\f0b0"}.fa-fingerprint:before{content:"\f577"}.fa-fire:before{content:"\f06d"}.fa-fire-alt:before{content:"\f7e4"}.fa-fire-extinguisher:before{content:"\f134"}.fa-firefox:before{content:"\f269"}.fa-firefox-browser:before{content:"\e007"}.fa-first-aid:before{content:"\f479"}.fa-first-order:before{content:"\f2b0"}.fa-first-order-alt:before{content:"\f50a"}.fa-firstdraft:before{content:"\f3a1"}.fa-fish:before{content:"\f578"}.fa-fist-raised:before{content:"\f6de"}.fa-flag:before{content:"\f024"}.fa-flag-checkered:before{content:"\f11e"}.fa-flag-usa:before{content:"\f74d"}.fa-flask:before{content:"\f0c3"}.fa-flickr:before{content:"\f16e"}.fa-flipboard:before{content:"\f44d"}.fa-flushed:before{content:"\f579"}.fa-fly:before{content:"\f417"}.fa-folder:before{content:"\f07b"}.fa-folder-minus:before{content:"\f65d"}.fa-folder-open:before{content:"\f07c"}.fa-folder-plus:before{content:"\f65e"}.fa-font:before{content:"\f031"}.fa-font-awesome:before{content:"\f2b4"}.fa-font-awesome-alt:before{content:"\f35c"}.fa-font-awesome-flag:before{content:"\f425"}.fa-font-awesome-logo-full:before{content:"\f4e6"}.fa-fonticons:before{content:"\f280"}.fa-fonticons-fi:before{content:"\f3a2"}.fa-football-ball:before{content:"\f44e"}.fa-fort-awesome:before{content:"\f286"}.fa-fort-awesome-alt:before{content:"\f3a3"}.fa-forumbee:before{content:"\f211"}.fa-forward:before{content:"\f04e"}.fa-foursquare:before{content:"\f180"}.fa-free-code-camp:before{content:"\f2c5"}.fa-freebsd:before{content:"\f3a4"}.fa-frog:before{content:"\f52e"}.fa-frown:before{content:"\f119"}.fa-frown-open:before{content:"\f57a"}.fa-fulcrum:before{content:"\f50b"}.fa-funnel-dollar:before{content:"\f662"}.fa-futbol:before{content:"\f1e3"}.fa-galactic-republic:before{content:"\f50c"}.fa-galactic-senate:before{content:"\f50d"}.fa-gamepad:before{content:"\f11b"}.fa-gas-pump:before{content:"\f52f"}.fa-gavel:before{content:"\f0e3"}.fa-gem:before{content:"\f3a5"}.fa-genderless:before{content:"\f22d"}.fa-get-pocket:before{content:"\f265"}.fa-gg:before{content:"\f260"}.fa-gg-circle:before{content:"\f261"}.fa-ghost:before{content:"\f6e2"}.fa-gift:before{content:"\f06b"}.fa-gifts:before{content:"\f79c"}.fa-git:before{content:"\f1d3"}.fa-git-alt:before{content:"\f841"}.fa-git-square:before{content:"\f1d2"}.fa-github:before{content:"\f09b"}.fa-github-alt:before{content:"\f113"}.fa-github-square:before{content:"\f092"}.fa-gitkraken:before{content:"\f3a6"}.fa-gitlab:before{content:"\f296"}.fa-gitter:before{content:"\f426"}.fa-glass-cheers:before{content:"\f79f"}.fa-glass-martini:before{content:"\f000"}.fa-glass-martini-alt:before{content:"\f57b"}.fa-glass-whiskey:before{content:"\f7a0"}.fa-glasses:before{content:"\f530"}.fa-glide:before{content:"\f2a5"}.fa-glide-g:before{content:"\f2a6"}.fa-globe:before{content:"\f0ac"}.fa-globe-africa:before{content:"\f57c"}.fa-globe-americas:before{content:"\f57d"}.fa-globe-asia:before{content:"\f57e"}.fa-globe-europe:before{content:"\f7a2"}.fa-gofore:before{content:"\f3a7"}.fa-golf-ball:before{content:"\f450"}.fa-goodreads:before{content:"\f3a8"}.fa-goodreads-g:before{content:"\f3a9"}.fa-google:before{content:"\f1a0"}.fa-google-drive:before{content:"\f3aa"}.fa-google-pay:before{content:"\e079"}.fa-google-play:before{content:"\f3ab"}.fa-google-plus:before{content:"\f2b3"}.fa-google-plus-g:before{content:"\f0d5"}.fa-google-plus-square:before{content:"\f0d4"}.fa-google-wallet:before{content:"\f1ee"}.fa-gopuram:before{content:"\f664"}.fa-graduation-cap:before{content:"\f19d"}.fa-gratipay:before{content:"\f184"}.fa-grav:before{content:"\f2d6"}.fa-greater-than:before{content:"\f531"}.fa-greater-than-equal:before{content:"\f532"}.fa-grimace:before{content:"\f57f"}.fa-grin:before{content:"\f580"}.fa-grin-alt:before{content:"\f581"}.fa-grin-beam:before{content:"\f582"}.fa-grin-beam-sweat:before{content:"\f583"}.fa-grin-hearts:before{content:"\f584"}.fa-grin-squint:before{content:"\f585"}.fa-grin-squint-tears:before{content:"\f586"}.fa-grin-stars:before{content:"\f587"}.fa-grin-tears:before{content:"\f588"}.fa-grin-tongue:before{content:"\f589"}.fa-grin-tongue-squint:before{content:"\f58a"}.fa-grin-tongue-wink:before{content:"\f58b"}.fa-grin-wink:before{content:"\f58c"}.fa-grip-horizontal:before{content:"\f58d"}.fa-grip-lines:before{content:"\f7a4"}.fa-grip-lines-vertical:before{content:"\f7a5"}.fa-grip-vertical:before{content:"\f58e"}.fa-gripfire:before{content:"\f3ac"}.fa-grunt:before{content:"\f3ad"}.fa-guitar:before{content:"\f7a6"}.fa-gulp:before{content:"\f3ae"}.fa-h-square:before{content:"\f0fd"}.fa-hacker-news:before{content:"\f1d4"}.fa-hacker-news-square:before{content:"\f3af"}.fa-hackerrank:before{content:"\f5f7"}.fa-hamburger:before{content:"\f805"}.fa-hammer:before{content:"\f6e3"}.fa-hamsa:before{content:"\f665"}.fa-hand-holding:before{content:"\f4bd"}.fa-hand-holding-heart:before{content:"\f4be"}.fa-hand-holding-medical:before{content:"\e05c"}.fa-hand-holding-usd:before{content:"\f4c0"}.fa-hand-holding-water:before{content:"\f4c1"}.fa-hand-lizard:before{content:"\f258"}.fa-hand-middle-finger:before{content:"\f806"}.fa-hand-paper:before{content:"\f256"}.fa-hand-peace:before{content:"\f25b"}.fa-hand-point-down:before{content:"\f0a7"}.fa-hand-point-left:before{content:"\f0a5"}.fa-hand-point-right:before{content:"\f0a4"}.fa-hand-point-up:before{content:"\f0a6"}.fa-hand-pointer:before{content:"\f25a"}.fa-hand-rock:before{content:"\f255"}.fa-hand-scissors:before{content:"\f257"}.fa-hand-sparkles:before{content:"\e05d"}.fa-hand-spock:before{content:"\f259"}.fa-hands:before{content:"\f4c2"}.fa-hands-helping:before{content:"\f4c4"}.fa-hands-wash:before{content:"\e05e"}.fa-handshake:before{content:"\f2b5"}.fa-handshake-alt-slash:before{content:"\e05f"}.fa-handshake-slash:before{content:"\e060"}.fa-hanukiah:before{content:"\f6e6"}.fa-hard-hat:before{content:"\f807"}.fa-hashtag:before{content:"\f292"}.fa-hat-cowboy:before{content:"\f8c0"}.fa-hat-cowboy-side:before{content:"\f8c1"}.fa-hat-wizard:before{content:"\f6e8"}.fa-hdd:before{content:"\f0a0"}.fa-head-side-cough:before{content:"\e061"}.fa-head-side-cough-slash:before{content:"\e062"}.fa-head-side-mask:before{content:"\e063"}.fa-head-side-virus:before{content:"\e064"}.fa-heading:before{content:"\f1dc"}.fa-headphones:before{content:"\f025"}.fa-headphones-alt:before{content:"\f58f"}.fa-headset:before{content:"\f590"}.fa-heart:before{content:"\f004"}.fa-heart-broken:before{content:"\f7a9"}.fa-heartbeat:before{content:"\f21e"}.fa-helicopter:before{content:"\f533"}.fa-highlighter:before{content:"\f591"}.fa-hiking:before{content:"\f6ec"}.fa-hippo:before{content:"\f6ed"}.fa-hips:before{content:"\f452"}.fa-hire-a-helper:before{content:"\f3b0"}.fa-history:before{content:"\f1da"}.fa-hockey-puck:before{content:"\f453"}.fa-holly-berry:before{content:"\f7aa"}.fa-home:before{content:"\f015"}.fa-hooli:before{content:"\f427"}.fa-hornbill:before{content:"\f592"}.fa-horse:before{content:"\f6f0"}.fa-horse-head:before{content:"\f7ab"}.fa-hospital:before{content:"\f0f8"}.fa-hospital-alt:before{content:"\f47d"}.fa-hospital-symbol:before{content:"\f47e"}.fa-hospital-user:before{content:"\f80d"}.fa-hot-tub:before{content:"\f593"}.fa-hotdog:before{content:"\f80f"}.fa-hotel:before{content:"\f594"}.fa-hotjar:before{content:"\f3b1"}.fa-hourglass:before{content:"\f254"}.fa-hourglass-end:before{content:"\f253"}.fa-hourglass-half:before{content:"\f252"}.fa-hourglass-start:before{content:"\f251"}.fa-house-damage:before{content:"\f6f1"}.fa-house-user:before{content:"\e065"}.fa-houzz:before{content:"\f27c"}.fa-hryvnia:before{content:"\f6f2"}.fa-html5:before{content:"\f13b"}.fa-hubspot:before{content:"\f3b2"}.fa-i-cursor:before{content:"\f246"}.fa-ice-cream:before{content:"\f810"}.fa-icicles:before{content:"\f7ad"}.fa-icons:before{content:"\f86d"}.fa-id-badge:before{content:"\f2c1"}.fa-id-card:before{content:"\f2c2"}.fa-id-card-alt:before{content:"\f47f"}.fa-ideal:before{content:"\e013"}.fa-igloo:before{content:"\f7ae"}.fa-image:before{content:"\f03e"}.fa-images:before{content:"\f302"}.fa-imdb:before{content:"\f2d8"}.fa-inbox:before{content:"\f01c"}.fa-indent:before{content:"\f03c"}.fa-industry:before{content:"\f275"}.fa-infinity:before{content:"\f534"}.fa-info:before{content:"\f129"}.fa-info-circle:before{content:"\f05a"}.fa-instagram:before{content:"\f16d"}.fa-instagram-square:before{content:"\e055"}.fa-intercom:before{content:"\f7af"}.fa-internet-explorer:before{content:"\f26b"}.fa-invision:before{content:"\f7b0"}.fa-ioxhost:before{content:"\f208"}.fa-italic:before{content:"\f033"}.fa-itch-io:before{content:"\f83a"}.fa-itunes:before{content:"\f3b4"}.fa-itunes-note:before{content:"\f3b5"}.fa-java:before{content:"\f4e4"}.fa-jedi:before{content:"\f669"}.fa-jedi-order:before{content:"\f50e"}.fa-jenkins:before{content:"\f3b6"}.fa-jira:before{content:"\f7b1"}.fa-joget:before{content:"\f3b7"}.fa-joint:before{content:"\f595"}.fa-joomla:before{content:"\f1aa"}.fa-journal-whills:before{content:"\f66a"}.fa-js:before{content:"\f3b8"}.fa-js-square:before{content:"\f3b9"}.fa-jsfiddle:before{content:"\f1cc"}.fa-kaaba:before{content:"\f66b"}.fa-kaggle:before{content:"\f5fa"}.fa-key:before{content:"\f084"}.fa-keybase:before{content:"\f4f5"}.fa-keyboard:before{content:"\f11c"}.fa-keycdn:before{content:"\f3ba"}.fa-khanda:before{content:"\f66d"}.fa-kickstarter:before{content:"\f3bb"}.fa-kickstarter-k:before{content:"\f3bc"}.fa-kiss:before{content:"\f596"}.fa-kiss-beam:before{content:"\f597"}.fa-kiss-wink-heart:before{content:"\f598"}.fa-kiwi-bird:before{content:"\f535"}.fa-korvue:before{content:"\f42f"}.fa-landmark:before{content:"\f66f"}.fa-language:before{content:"\f1ab"}.fa-laptop:before{content:"\f109"}.fa-laptop-code:before{content:"\f5fc"}.fa-laptop-house:before{content:"\e066"}.fa-laptop-medical:before{content:"\f812"}.fa-laravel:before{content:"\f3bd"}.fa-lastfm:before{content:"\f202"}.fa-lastfm-square:before{content:"\f203"}.fa-laugh:before{content:"\f599"}.fa-laugh-beam:before{content:"\f59a"}.fa-laugh-squint:before{content:"\f59b"}.fa-laugh-wink:before{content:"\f59c"}.fa-layer-group:before{content:"\f5fd"}.fa-leaf:before{content:"\f06c"}.fa-leanpub:before{content:"\f212"}.fa-lemon:before{content:"\f094"}.fa-less:before{content:"\f41d"}.fa-less-than:before{content:"\f536"}.fa-less-than-equal:before{content:"\f537"}.fa-level-down-alt:before{content:"\f3be"}.fa-level-up-alt:before{content:"\f3bf"}.fa-life-ring:before{content:"\f1cd"}.fa-lightbulb:before{content:"\f0eb"}.fa-line:before{content:"\f3c0"}.fa-link:before{content:"\f0c1"}.fa-linkedin:before{content:"\f08c"}.fa-linkedin-in:before{content:"\f0e1"}.fa-linode:before{content:"\f2b8"}.fa-linux:before{content:"\f17c"}.fa-lira-sign:before{content:"\f195"}.fa-list:before{content:"\f03a"}.fa-list-alt:before{content:"\f022"}.fa-list-ol:before{content:"\f0cb"}.fa-list-ul:before{content:"\f0ca"}.fa-location-arrow:before{content:"\f124"}.fa-lock:before{content:"\f023"}.fa-lock-open:before{content:"\f3c1"}.fa-long-arrow-alt-down:before{content:"\f309"}.fa-long-arrow-alt-left:before{content:"\f30a"}.fa-long-arrow-alt-right:before{content:"\f30b"}.fa-long-arrow-alt-up:before{content:"\f30c"}.fa-low-vision:before{content:"\f2a8"}.fa-luggage-cart:before{content:"\f59d"}.fa-lungs:before{content:"\f604"}.fa-lungs-virus:before{content:"\e067"}.fa-lyft:before{content:"\f3c3"}.fa-magento:before{content:"\f3c4"}.fa-magic:before{content:"\f0d0"}.fa-magnet:before{content:"\f076"}.fa-mail-bulk:before{content:"\f674"}.fa-mailchimp:before{content:"\f59e"}.fa-male:before{content:"\f183"}.fa-mandalorian:before{content:"\f50f"}.fa-map:before{content:"\f279"}.fa-map-marked:before{content:"\f59f"}.fa-map-marked-alt:before{content:"\f5a0"}.fa-map-marker:before{content:"\f041"}.fa-map-marker-alt:before{content:"\f3c5"}.fa-map-pin:before{content:"\f276"}.fa-map-signs:before{content:"\f277"}.fa-markdown:before{content:"\f60f"}.fa-marker:before{content:"\f5a1"}.fa-mars:before{content:"\f222"}.fa-mars-double:before{content:"\f227"}.fa-mars-stroke:before{content:"\f229"}.fa-mars-stroke-h:before{content:"\f22b"}.fa-mars-stroke-v:before{content:"\f22a"}.fa-mask:before{content:"\f6fa"}.fa-mastodon:before{content:"\f4f6"}.fa-maxcdn:before{content:"\f136"}.fa-mdb:before{content:"\f8ca"}.fa-medal:before{content:"\f5a2"}.fa-medapps:before{content:"\f3c6"}.fa-medium:before{content:"\f23a"}.fa-medium-m:before{content:"\f3c7"}.fa-medkit:before{content:"\f0fa"}.fa-medrt:before{content:"\f3c8"}.fa-meetup:before{content:"\f2e0"}.fa-megaport:before{content:"\f5a3"}.fa-meh:before{content:"\f11a"}.fa-meh-blank:before{content:"\f5a4"}.fa-meh-rolling-eyes:before{content:"\f5a5"}.fa-memory:before{content:"\f538"}.fa-mendeley:before{content:"\f7b3"}.fa-menorah:before{content:"\f676"}.fa-mercury:before{content:"\f223"}.fa-meteor:before{content:"\f753"}.fa-microblog:before{content:"\e01a"}.fa-microchip:before{content:"\f2db"}.fa-microphone:before{content:"\f130"}.fa-microphone-alt:before{content:"\f3c9"}.fa-microphone-alt-slash:before{content:"\f539"}.fa-microphone-slash:before{content:"\f131"}.fa-microscope:before{content:"\f610"}.fa-microsoft:before{content:"\f3ca"}.fa-minus:before{content:"\f068"}.fa-minus-circle:before{content:"\f056"}.fa-minus-square:before{content:"\f146"}.fa-mitten:before{content:"\f7b5"}.fa-mix:before{content:"\f3cb"}.fa-mixcloud:before{content:"\f289"}.fa-mixer:before{content:"\e056"}.fa-mizuni:before{content:"\f3cc"}.fa-mobile:before{content:"\f10b"}.fa-mobile-alt:before{content:"\f3cd"}.fa-modx:before{content:"\f285"}.fa-monero:before{content:"\f3d0"}.fa-money-bill:before{content:"\f0d6"}.fa-money-bill-alt:before{content:"\f3d1"}.fa-money-bill-wave:before{content:"\f53a"}.fa-money-bill-wave-alt:before{content:"\f53b"}.fa-money-check:before{content:"\f53c"}.fa-money-check-alt:before{content:"\f53d"}.fa-monument:before{content:"\f5a6"}.fa-moon:before{content:"\f186"}.fa-mortar-pestle:before{content:"\f5a7"}.fa-mosque:before{content:"\f678"}.fa-motorcycle:before{content:"\f21c"}.fa-mountain:before{content:"\f6fc"}.fa-mouse:before{content:"\f8cc"}.fa-mouse-pointer:before{content:"\f245"}.fa-mug-hot:before{content:"\f7b6"}.fa-music:before{content:"\f001"}.fa-napster:before{content:"\f3d2"}.fa-neos:before{content:"\f612"}.fa-network-wired:before{content:"\f6ff"}.fa-neuter:before{content:"\f22c"}.fa-newspaper:before{content:"\f1ea"}.fa-nimblr:before{content:"\f5a8"}.fa-node:before{content:"\f419"}.fa-node-js:before{content:"\f3d3"}.fa-not-equal:before{content:"\f53e"}.fa-notes-medical:before{content:"\f481"}.fa-npm:before{content:"\f3d4"}.fa-ns8:before{content:"\f3d5"}.fa-nutritionix:before{content:"\f3d6"}.fa-object-group:before{content:"\f247"}.fa-object-ungroup:before{content:"\f248"}.fa-odnoklassniki:before{content:"\f263"}.fa-odnoklassniki-square:before{content:"\f264"}.fa-oil-can:before{content:"\f613"}.fa-old-republic:before{content:"\f510"}.fa-om:before{content:"\f679"}.fa-opencart:before{content:"\f23d"}.fa-openid:before{content:"\f19b"}.fa-opera:before{content:"\f26a"}.fa-optin-monster:before{content:"\f23c"}.fa-orcid:before{content:"\f8d2"}.fa-osi:before{content:"\f41a"}.fa-otter:before{content:"\f700"}.fa-outdent:before{content:"\f03b"}.fa-page4:before{content:"\f3d7"}.fa-pagelines:before{content:"\f18c"}.fa-pager:before{content:"\f815"}.fa-paint-brush:before{content:"\f1fc"}.fa-paint-roller:before{content:"\f5aa"}.fa-palette:before{content:"\f53f"}.fa-palfed:before{content:"\f3d8"}.fa-pallet:before{content:"\f482"}.fa-paper-plane:before{content:"\f1d8"}.fa-paperclip:before{content:"\f0c6"}.fa-parachute-box:before{content:"\f4cd"}.fa-paragraph:before{content:"\f1dd"}.fa-parking:before{content:"\f540"}.fa-passport:before{content:"\f5ab"}.fa-pastafarianism:before{content:"\f67b"}.fa-paste:before{content:"\f0ea"}.fa-patreon:before{content:"\f3d9"}.fa-pause:before{content:"\f04c"}.fa-pause-circle:before{content:"\f28b"}.fa-paw:before{content:"\f1b0"}.fa-paypal:before{content:"\f1ed"}.fa-peace:before{content:"\f67c"}.fa-pen:before{content:"\f304"}.fa-pen-alt:before{content:"\f305"}.fa-pen-fancy:before{content:"\f5ac"}.fa-pen-nib:before{content:"\f5ad"}.fa-pen-square:before{content:"\f14b"}.fa-pencil-alt:before{content:"\f303"}.fa-pencil-ruler:before{content:"\f5ae"}.fa-penny-arcade:before{content:"\f704"}.fa-people-arrows:before{content:"\e068"}.fa-people-carry:before{content:"\f4ce"}.fa-pepper-hot:before{content:"\f816"}.fa-percent:before{content:"\f295"}.fa-percentage:before{content:"\f541"}.fa-periscope:before{content:"\f3da"}.fa-person-booth:before{content:"\f756"}.fa-phabricator:before{content:"\f3db"}.fa-phoenix-framework:before{content:"\f3dc"}.fa-phoenix-squadron:before{content:"\f511"}.fa-phone:before{content:"\f095"}.fa-phone-alt:before{content:"\f879"}.fa-phone-slash:before{content:"\f3dd"}.fa-phone-square:before{content:"\f098"}.fa-phone-square-alt:before{content:"\f87b"}.fa-phone-volume:before{content:"\f2a0"}.fa-photo-video:before{content:"\f87c"}.fa-php:before{content:"\f457"}.fa-pied-piper:before{content:"\f2ae"}.fa-pied-piper-alt:before{content:"\f1a8"}.fa-pied-piper-hat:before{content:"\f4e5"}.fa-pied-piper-pp:before{content:"\f1a7"}.fa-pied-piper-square:before{content:"\e01e"}.fa-piggy-bank:before{content:"\f4d3"}.fa-pills:before{content:"\f484"}.fa-pinterest:before{content:"\f0d2"}.fa-pinterest-p:before{content:"\f231"}.fa-pinterest-square:before{content:"\f0d3"}.fa-pizza-slice:before{content:"\f818"}.fa-place-of-worship:before{content:"\f67f"}.fa-plane:before{content:"\f072"}.fa-plane-arrival:before{content:"\f5af"}.fa-plane-departure:before{content:"\f5b0"}.fa-plane-slash:before{content:"\e069"}.fa-play:before{content:"\f04b"}.fa-play-circle:before{content:"\f144"}.fa-playstation:before{content:"\f3df"}.fa-plug:before{content:"\f1e6"}.fa-plus:before{content:"\f067"}.fa-plus-circle:before{content:"\f055"}.fa-plus-square:before{content:"\f0fe"}.fa-podcast:before{content:"\f2ce"}.fa-poll:before{content:"\f681"}.fa-poll-h:before{content:"\f682"}.fa-poo:before{content:"\f2fe"}.fa-poo-storm:before{content:"\f75a"}.fa-poop:before{content:"\f619"}.fa-portrait:before{content:"\f3e0"}.fa-pound-sign:before{content:"\f154"}.fa-power-off:before{content:"\f011"}.fa-pray:before{content:"\f683"}.fa-praying-hands:before{content:"\f684"}.fa-prescription:before{content:"\f5b1"}.fa-prescription-bottle:before{content:"\f485"}.fa-prescription-bottle-alt:before{content:"\f486"}.fa-print:before{content:"\f02f"}.fa-procedures:before{content:"\f487"}.fa-product-hunt:before{content:"\f288"}.fa-project-diagram:before{content:"\f542"}.fa-pump-medical:before{content:"\e06a"}.fa-pump-soap:before{content:"\e06b"}.fa-pushed:before{content:"\f3e1"}.fa-puzzle-piece:before{content:"\f12e"}.fa-python:before{content:"\f3e2"}.fa-qq:before{content:"\f1d6"}.fa-qrcode:before{content:"\f029"}.fa-question:before{content:"\f128"}.fa-question-circle:before{content:"\f059"}.fa-quidditch:before{content:"\f458"}.fa-quinscape:before{content:"\f459"}.fa-quora:before{content:"\f2c4"}.fa-quote-left:before{content:"\f10d"}.fa-quote-right:before{content:"\f10e"}.fa-quran:before{content:"\f687"}.fa-r-project:before{content:"\f4f7"}.fa-radiation:before{content:"\f7b9"}.fa-radiation-alt:before{content:"\f7ba"}.fa-rainbow:before{content:"\f75b"}.fa-random:before{content:"\f074"}.fa-raspberry-pi:before{content:"\f7bb"}.fa-ravelry:before{content:"\f2d9"}.fa-react:before{content:"\f41b"}.fa-reacteurope:before{content:"\f75d"}.fa-readme:before{content:"\f4d5"}.fa-rebel:before{content:"\f1d0"}.fa-receipt:before{content:"\f543"}.fa-record-vinyl:before{content:"\f8d9"}.fa-recycle:before{content:"\f1b8"}.fa-red-river:before{content:"\f3e3"}.fa-reddit:before{content:"\f1a1"}.fa-reddit-alien:before{content:"\f281"}.fa-reddit-square:before{content:"\f1a2"}.fa-redhat:before{content:"\f7bc"}.fa-redo:before{content:"\f01e"}.fa-redo-alt:before{content:"\f2f9"}.fa-registered:before{content:"\f25d"}.fa-remove-format:before{content:"\f87d"}.fa-renren:before{content:"\f18b"}.fa-reply:before{content:"\f3e5"}.fa-reply-all:before{content:"\f122"}.fa-replyd:before{content:"\f3e6"}.fa-republican:before{content:"\f75e"}.fa-researchgate:before{content:"\f4f8"}.fa-resolving:before{content:"\f3e7"}.fa-restroom:before{content:"\f7bd"}.fa-retweet:before{content:"\f079"}.fa-rev:before{content:"\f5b2"}.fa-ribbon:before{content:"\f4d6"}.fa-ring:before{content:"\f70b"}.fa-road:before{content:"\f018"}.fa-robot:before{content:"\f544"}.fa-rocket:before{content:"\f135"}.fa-rocketchat:before{content:"\f3e8"}.fa-rockrms:before{content:"\f3e9"}.fa-route:before{content:"\f4d7"}.fa-rss:before{content:"\f09e"}.fa-rss-square:before{content:"\f143"}.fa-ruble-sign:before{content:"\f158"}.fa-ruler:before{content:"\f545"}.fa-ruler-combined:before{content:"\f546"}.fa-ruler-horizontal:before{content:"\f547"}.fa-ruler-vertical:before{content:"\f548"}.fa-running:before{content:"\f70c"}.fa-rupee-sign:before{content:"\f156"}.fa-rust:before{content:"\e07a"}.fa-sad-cry:before{content:"\f5b3"}.fa-sad-tear:before{content:"\f5b4"}.fa-safari:before{content:"\f267"}.fa-salesforce:before{content:"\f83b"}.fa-sass:before{content:"\f41e"}.fa-satellite:before{content:"\f7bf"}.fa-satellite-dish:before{content:"\f7c0"}.fa-save:before{content:"\f0c7"}.fa-schlix:before{content:"\f3ea"}.fa-school:before{content:"\f549"}.fa-screwdriver:before{content:"\f54a"}.fa-scribd:before{content:"\f28a"}.fa-scroll:before{content:"\f70e"}.fa-sd-card:before{content:"\f7c2"}.fa-search:before{content:"\f002"}.fa-search-dollar:before{content:"\f688"}.fa-search-location:before{content:"\f689"}.fa-search-minus:before{content:"\f010"}.fa-search-plus:before{content:"\f00e"}.fa-searchengin:before{content:"\f3eb"}.fa-seedling:before{content:"\f4d8"}.fa-sellcast:before{content:"\f2da"}.fa-sellsy:before{content:"\f213"}.fa-server:before{content:"\f233"}.fa-servicestack:before{content:"\f3ec"}.fa-shapes:before{content:"\f61f"}.fa-share:before{content:"\f064"}.fa-share-alt:before{content:"\f1e0"}.fa-share-alt-square:before{content:"\f1e1"}.fa-share-square:before{content:"\f14d"}.fa-shekel-sign:before{content:"\f20b"}.fa-shield-alt:before{content:"\f3ed"}.fa-shield-virus:before{content:"\e06c"}.fa-ship:before{content:"\f21a"}.fa-shipping-fast:before{content:"\f48b"}.fa-shirtsinbulk:before{content:"\f214"}.fa-shoe-prints:before{content:"\f54b"}.fa-shopify:before{content:"\e057"}.fa-shopping-bag:before{content:"\f290"}.fa-shopping-basket:before{content:"\f291"}.fa-shopping-cart:before{content:"\f07a"}.fa-shopware:before{content:"\f5b5"}.fa-shower:before{content:"\f2cc"}.fa-shuttle-van:before{content:"\f5b6"}.fa-sign:before{content:"\f4d9"}.fa-sign-in-alt:before{content:"\f2f6"}.fa-sign-language:before{content:"\f2a7"}.fa-sign-out-alt:before{content:"\f2f5"}.fa-signal:before{content:"\f012"}.fa-signature:before{content:"\f5b7"}.fa-sim-card:before{content:"\f7c4"}.fa-simplybuilt:before{content:"\f215"}.fa-sink:before{content:"\e06d"}.fa-sistrix:before{content:"\f3ee"}.fa-sitemap:before{content:"\f0e8"}.fa-sith:before{content:"\f512"}.fa-skating:before{content:"\f7c5"}.fa-sketch:before{content:"\f7c6"}.fa-skiing:before{content:"\f7c9"}.fa-skiing-nordic:before{content:"\f7ca"}.fa-skull:before{content:"\f54c"}.fa-skull-crossbones:before{content:"\f714"}.fa-skyatlas:before{content:"\f216"}.fa-skype:before{content:"\f17e"}.fa-slack:before{content:"\f198"}.fa-slack-hash:before{content:"\f3ef"}.fa-slash:before{content:"\f715"}.fa-sleigh:before{content:"\f7cc"}.fa-sliders-h:before{content:"\f1de"}.fa-slideshare:before{content:"\f1e7"}.fa-smile:before{content:"\f118"}.fa-smile-beam:before{content:"\f5b8"}.fa-smile-wink:before{content:"\f4da"}.fa-smog:before{content:"\f75f"}.fa-smoking:before{content:"\f48d"}.fa-smoking-ban:before{content:"\f54d"}.fa-sms:before{content:"\f7cd"}.fa-snapchat:before{content:"\f2ab"}.fa-snapchat-ghost:before{content:"\f2ac"}.fa-snapchat-square:before{content:"\f2ad"}.fa-snowboarding:before{content:"\f7ce"}.fa-snowflake:before{content:"\f2dc"}.fa-snowman:before{content:"\f7d0"}.fa-snowplow:before{content:"\f7d2"}.fa-soap:before{content:"\e06e"}.fa-socks:before{content:"\f696"}.fa-solar-panel:before{content:"\f5ba"}.fa-sort:before{content:"\f0dc"}.fa-sort-alpha-down:before{content:"\f15d"}.fa-sort-alpha-down-alt:before{content:"\f881"}.fa-sort-alpha-up:before{content:"\f15e"}.fa-sort-alpha-up-alt:before{content:"\f882"}.fa-sort-amount-down:before{content:"\f160"}.fa-sort-amount-down-alt:before{content:"\f884"}.fa-sort-amount-up:before{content:"\f161"}.fa-sort-amount-up-alt:before{content:"\f885"}.fa-sort-down:before{content:"\f0dd"}.fa-sort-numeric-down:before{content:"\f162"}.fa-sort-numeric-down-alt:before{content:"\f886"}.fa-sort-numeric-up:before{content:"\f163"}.fa-sort-numeric-up-alt:before{content:"\f887"}.fa-sort-up:before{content:"\f0de"}.fa-soundcloud:before{content:"\f1be"}.fa-sourcetree:before{content:"\f7d3"}.fa-spa:before{content:"\f5bb"}.fa-space-shuttle:before{content:"\f197"}.fa-speakap:before{content:"\f3f3"}.fa-speaker-deck:before{content:"\f83c"}.fa-spell-check:before{content:"\f891"}.fa-spider:before{content:"\f717"}.fa-spinner:before{content:"\f110"}.fa-splotch:before{content:"\f5bc"}.fa-spotify:before{content:"\f1bc"}.fa-spray-can:before{content:"\f5bd"}.fa-square:before{content:"\f0c8"}.fa-square-full:before{content:"\f45c"}.fa-square-root-alt:before{content:"\f698"}.fa-squarespace:before{content:"\f5be"}.fa-stack-exchange:before{content:"\f18d"}.fa-stack-overflow:before{content:"\f16c"}.fa-stackpath:before{content:"\f842"}.fa-stamp:before{content:"\f5bf"}.fa-star:before{content:"\f005"}.fa-star-and-crescent:before{content:"\f699"}.fa-star-half:before{content:"\f089"}.fa-star-half-alt:before{content:"\f5c0"}.fa-star-of-david:before{content:"\f69a"}.fa-star-of-life:before{content:"\f621"}.fa-staylinked:before{content:"\f3f5"}.fa-steam:before{content:"\f1b6"}.fa-steam-square:before{content:"\f1b7"}.fa-steam-symbol:before{content:"\f3f6"}.fa-step-backward:before{content:"\f048"}.fa-step-forward:before{content:"\f051"}.fa-stethoscope:before{content:"\f0f1"}.fa-sticker-mule:before{content:"\f3f7"}.fa-sticky-note:before{content:"\f249"}.fa-stop:before{content:"\f04d"}.fa-stop-circle:before{content:"\f28d"}.fa-stopwatch:before{content:"\f2f2"}.fa-stopwatch-20:before{content:"\e06f"}.fa-store:before{content:"\f54e"}.fa-store-alt:before{content:"\f54f"}.fa-store-alt-slash:before{content:"\e070"}.fa-store-slash:before{content:"\e071"}.fa-strava:before{content:"\f428"}.fa-stream:before{content:"\f550"}.fa-street-view:before{content:"\f21d"}.fa-strikethrough:before{content:"\f0cc"}.fa-stripe:before{content:"\f429"}.fa-stripe-s:before{content:"\f42a"}.fa-stroopwafel:before{content:"\f551"}.fa-studiovinari:before{content:"\f3f8"}.fa-stumbleupon:before{content:"\f1a4"}.fa-stumbleupon-circle:before{content:"\f1a3"}.fa-subscript:before{content:"\f12c"}.fa-subway:before{content:"\f239"}.fa-suitcase:before{content:"\f0f2"}.fa-suitcase-rolling:before{content:"\f5c1"}.fa-sun:before{content:"\f185"}.fa-superpowers:before{content:"\f2dd"}.fa-superscript:before{content:"\f12b"}.fa-supple:before{content:"\f3f9"}.fa-surprise:before{content:"\f5c2"}.fa-suse:before{content:"\f7d6"}.fa-swatchbook:before{content:"\f5c3"}.fa-swift:before{content:"\f8e1"}.fa-swimmer:before{content:"\f5c4"}.fa-swimming-pool:before{content:"\f5c5"}.fa-symfony:before{content:"\f83d"}.fa-synagogue:before{content:"\f69b"}.fa-sync:before{content:"\f021"}.fa-sync-alt:before{content:"\f2f1"}.fa-syringe:before{content:"\f48e"}.fa-table:before{content:"\f0ce"}.fa-table-tennis:before{content:"\f45d"}.fa-tablet:before{content:"\f10a"}.fa-tablet-alt:before{content:"\f3fa"}.fa-tablets:before{content:"\f490"}.fa-tachometer-alt:before{content:"\f3fd"}.fa-tag:before{content:"\f02b"}.fa-tags:before{content:"\f02c"}.fa-tape:before{content:"\f4db"}.fa-tasks:before{content:"\f0ae"}.fa-taxi:before{content:"\f1ba"}.fa-teamspeak:before{content:"\f4f9"}.fa-teeth:before{content:"\f62e"}.fa-teeth-open:before{content:"\f62f"}.fa-telegram:before{content:"\f2c6"}.fa-telegram-plane:before{content:"\f3fe"}.fa-temperature-high:before{content:"\f769"}.fa-temperature-low:before{content:"\f76b"}.fa-tencent-weibo:before{content:"\f1d5"}.fa-tenge:before{content:"\f7d7"}.fa-terminal:before{content:"\f120"}.fa-text-height:before{content:"\f034"}.fa-text-width:before{content:"\f035"}.fa-th:before{content:"\f00a"}.fa-th-large:before{content:"\f009"}.fa-th-list:before{content:"\f00b"}.fa-the-red-yeti:before{content:"\f69d"}.fa-theater-masks:before{content:"\f630"}.fa-themeco:before{content:"\f5c6"}.fa-themeisle:before{content:"\f2b2"}.fa-thermometer:before{content:"\f491"}.fa-thermometer-empty:before{content:"\f2cb"}.fa-thermometer-full:before{content:"\f2c7"}.fa-thermometer-half:before{content:"\f2c9"}.fa-thermometer-quarter:before{content:"\f2ca"}.fa-thermometer-three-quarters:before{content:"\f2c8"}.fa-think-peaks:before{content:"\f731"}.fa-thumbs-down:before{content:"\f165"}.fa-thumbs-up:before{content:"\f164"}.fa-thumbtack:before{content:"\f08d"}.fa-ticket-alt:before{content:"\f3ff"}.fa-tiktok:before{content:"\e07b"}.fa-times:before{content:"\f00d"}.fa-times-circle:before{content:"\f057"}.fa-tint:before{content:"\f043"}.fa-tint-slash:before{content:"\f5c7"}.fa-tired:before{content:"\f5c8"}.fa-toggle-off:before{content:"\f204"}.fa-toggle-on:before{content:"\f205"}.fa-toilet:before{content:"\f7d8"}.fa-toilet-paper:before{content:"\f71e"}.fa-toilet-paper-slash:before{content:"\e072"}.fa-toolbox:before{content:"\f552"}.fa-tools:before{content:"\f7d9"}.fa-tooth:before{content:"\f5c9"}.fa-torah:before{content:"\f6a0"}.fa-torii-gate:before{content:"\f6a1"}.fa-tractor:before{content:"\f722"}.fa-trade-federation:before{content:"\f513"}.fa-trademark:before{content:"\f25c"}.fa-traffic-light:before{content:"\f637"}.fa-trailer:before{content:"\e041"}.fa-train:before{content:"\f238"}.fa-tram:before{content:"\f7da"}.fa-transgender:before{content:"\f224"}.fa-transgender-alt:before{content:"\f225"}.fa-trash:before{content:"\f1f8"}.fa-trash-alt:before{content:"\f2ed"}.fa-trash-restore:before{content:"\f829"}.fa-trash-restore-alt:before{content:"\f82a"}.fa-tree:before{content:"\f1bb"}.fa-trello:before{content:"\f181"}.fa-tripadvisor:before{content:"\f262"}.fa-trophy:before{content:"\f091"}.fa-truck:before{content:"\f0d1"}.fa-truck-loading:before{content:"\f4de"}.fa-truck-monster:before{content:"\f63b"}.fa-truck-moving:before{content:"\f4df"}.fa-truck-pickup:before{content:"\f63c"}.fa-tshirt:before{content:"\f553"}.fa-tty:before{content:"\f1e4"}.fa-tumblr:before{content:"\f173"}.fa-tumblr-square:before{content:"\f174"}.fa-tv:before{content:"\f26c"}.fa-twitch:before{content:"\f1e8"}.fa-twitter:before{content:"\f099"}.fa-twitter-square:before{content:"\f081"}.fa-typo3:before{content:"\f42b"}.fa-uber:before{content:"\f402"}.fa-ubuntu:before{content:"\f7df"}.fa-uikit:before{content:"\f403"}.fa-umbraco:before{content:"\f8e8"}.fa-umbrella:before{content:"\f0e9"}.fa-umbrella-beach:before{content:"\f5ca"}.fa-underline:before{content:"\f0cd"}.fa-undo:before{content:"\f0e2"}.fa-undo-alt:before{content:"\f2ea"}.fa-uniregistry:before{content:"\f404"}.fa-unity:before{content:"\e049"}.fa-universal-access:before{content:"\f29a"}.fa-university:before{content:"\f19c"}.fa-unlink:before{content:"\f127"}.fa-unlock:before{content:"\f09c"}.fa-unlock-alt:before{content:"\f13e"}.fa-unsplash:before{content:"\e07c"}.fa-untappd:before{content:"\f405"}.fa-upload:before{content:"\f093"}.fa-ups:before{content:"\f7e0"}.fa-usb:before{content:"\f287"}.fa-user:before{content:"\f007"}.fa-user-alt:before{content:"\f406"}.fa-user-alt-slash:before{content:"\f4fa"}.fa-user-astronaut:before{content:"\f4fb"}.fa-user-check:before{content:"\f4fc"}.fa-user-circle:before{content:"\f2bd"}.fa-user-clock:before{content:"\f4fd"}.fa-user-cog:before{content:"\f4fe"}.fa-user-edit:before{content:"\f4ff"}.fa-user-friends:before{content:"\f500"}.fa-user-graduate:before{content:"\f501"}.fa-user-injured:before{content:"\f728"}.fa-user-lock:before{content:"\f502"}.fa-user-md:before{content:"\f0f0"}.fa-user-minus:before{content:"\f503"}.fa-user-ninja:before{content:"\f504"}.fa-user-nurse:before{content:"\f82f"}.fa-user-plus:before{content:"\f234"}.fa-user-secret:before{content:"\f21b"}.fa-user-shield:before{content:"\f505"}.fa-user-slash:before{content:"\f506"}.fa-user-tag:before{content:"\f507"}.fa-user-tie:before{content:"\f508"}.fa-user-times:before{content:"\f235"}.fa-users:before{content:"\f0c0"}.fa-users-cog:before{content:"\f509"}.fa-users-slash:before{content:"\e073"}.fa-usps:before{content:"\f7e1"}.fa-ussunnah:before{content:"\f407"}.fa-utensil-spoon:before{content:"\f2e5"}.fa-utensils:before{content:"\f2e7"}.fa-vaadin:before{content:"\f408"}.fa-vector-square:before{content:"\f5cb"}.fa-venus:before{content:"\f221"}.fa-venus-double:before{content:"\f226"}.fa-venus-mars:before{content:"\f228"}.fa-viacoin:before{content:"\f237"}.fa-viadeo:before{content:"\f2a9"}.fa-viadeo-square:before{content:"\f2aa"}.fa-vial:before{content:"\f492"}.fa-vials:before{content:"\f493"}.fa-viber:before{content:"\f409"}.fa-video:before{content:"\f03d"}.fa-video-slash:before{content:"\f4e2"}.fa-vihara:before{content:"\f6a7"}.fa-vimeo:before{content:"\f40a"}.fa-vimeo-square:before{content:"\f194"}.fa-vimeo-v:before{content:"\f27d"}.fa-vine:before{content:"\f1ca"}.fa-virus:before{content:"\e074"}.fa-virus-slash:before{content:"\e075"}.fa-viruses:before{content:"\e076"}.fa-vk:before{content:"\f189"}.fa-vnv:before{content:"\f40b"}.fa-voicemail:before{content:"\f897"}.fa-volleyball-ball:before{content:"\f45f"}.fa-volume-down:before{content:"\f027"}.fa-volume-mute:before{content:"\f6a9"}.fa-volume-off:before{content:"\f026"}.fa-volume-up:before{content:"\f028"}.fa-vote-yea:before{content:"\f772"}.fa-vr-cardboard:before{content:"\f729"}.fa-vuejs:before{content:"\f41f"}.fa-walking:before{content:"\f554"}.fa-wallet:before{content:"\f555"}.fa-warehouse:before{content:"\f494"}.fa-water:before{content:"\f773"}.fa-wave-square:before{content:"\f83e"}.fa-waze:before{content:"\f83f"}.fa-weebly:before{content:"\f5cc"}.fa-weibo:before{content:"\f18a"}.fa-weight:before{content:"\f496"}.fa-weight-hanging:before{content:"\f5cd"}.fa-weixin:before{content:"\f1d7"}.fa-whatsapp:before{content:"\f232"}.fa-whatsapp-square:before{content:"\f40c"}.fa-wheelchair:before{content:"\f193"}.fa-whmcs:before{content:"\f40d"}.fa-wifi:before{content:"\f1eb"}.fa-wikipedia-w:before{content:"\f266"}.fa-wind:before{content:"\f72e"}.fa-window-close:before{content:"\f410"}.fa-window-maximize:before{content:"\f2d0"}.fa-window-minimize:before{content:"\f2d1"}.fa-window-restore:before{content:"\f2d2"}.fa-windows:before{content:"\f17a"}.fa-wine-bottle:before{content:"\f72f"}.fa-wine-glass:before{content:"\f4e3"}.fa-wine-glass-alt:before{content:"\f5ce"}.fa-wix:before{content:"\f5cf"}.fa-wizards-of-the-coast:before{content:"\f730"}.fa-wolf-pack-battalion:before{content:"\f514"}.fa-won-sign:before{content:"\f159"}.fa-wordpress:before{content:"\f19a"}.fa-wordpress-simple:before{content:"\f411"}.fa-wpbeginner:before{content:"\f297"}.fa-wpexplorer:before{content:"\f2de"}.fa-wpforms:before{content:"\f298"}.fa-wpressr:before{content:"\f3e4"}.fa-wrench:before{content:"\f0ad"}.fa-x-ray:before{content:"\f497"}.fa-xbox:before{content:"\f412"}.fa-xing:before{content:"\f168"}.fa-xing-square:before{content:"\f169"}.fa-y-combinator:before{content:"\f23b"}.fa-yahoo:before{content:"\f19e"}.fa-yammer:before{content:"\f840"}.fa-yandex:before{content:"\f413"}.fa-yandex-international:before{content:"\f414"}.fa-yarn:before{content:"\f7e3"}.fa-yelp:before{content:"\f1e9"}.fa-yen-sign:before{content:"\f157"}.fa-yin-yang:before{content:"\f6ad"}.fa-yoast:before{content:"\f2b1"}.fa-youtube:before{content:"\f167"}.fa-youtube-square:before{content:"\f431"}.fa-zhihu:before{content:"\f63f"}.sr-only{border:0;clip:rect(0,0,0,0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.sr-only-focusable:active,.sr-only-focusable:focus{clip:auto;height:auto;margin:0;overflow:visible;position:static;width:auto}@font-face{font-family:"Font Awesome 5 Brands";font-style:normal;font-weight:400;font-display:block;src:url(/static/lab/0fabb6606be4c45acfeedd115d0caca4.eot);src:url(/static/lab/0fabb6606be4c45acfeedd115d0caca4.eot?#iefix) format("embedded-opentype"),url(/static/lab/cac68c831145804808381a7032fdc7c2.woff2) format("woff2"),url(/static/lab/dc0bd022735ed218df547742a1b2f172.woff) format("woff"),url(/static/lab/085b1dd8427dbeff10bd55410915a3f6.ttf) format("truetype"),url(/static/lab/ccfdb9dc442be0c629d331e94497428b.svg#fontawesome) format("svg")}.fab{font-family:"Font Awesome 5 Brands"}@font-face{font-family:"Font Awesome 5 Free";font-style:normal;font-weight:400;font-display:block;src:url(/static/lab/ad3a7c0d77e09602f4ab73db3660ffd8.eot);src:url(/static/lab/ad3a7c0d77e09602f4ab73db3660ffd8.eot?#iefix) format("embedded-opentype"),url(/static/lab/3a3398a6ef60fc64eacf45665958342e.woff2) format("woff2"),url(/static/lab/05b53beb21e3ef13d28244545977152d.woff) format("woff"),url(/static/lab/1a78af4105d4d56e6c34f76dc70bf1bc.ttf) format("truetype"),url(/static/lab/e75dfd904d366a2560c63c23cfc98ef8.svg#fontawesome) format("svg")}.fab,.far{font-weight:400}@font-face{font-family:"Font Awesome 5 Free";font-style:normal;font-weight:900;font-display:block;src:url(/static/lab/89bd2e38475e441a5cd70f663f921d61.eot);src:url(/static/lab/89bd2e38475e441a5cd70f663f921d61.eot?#iefix) format("embedded-opentype"),url(/static/lab/c500da19d776384ba69573ae6fe274e7.woff2) format("woff2"),url(/static/lab/ee09ad7553b8ad3d81150d609d5341a0.woff) format("woff"),url(/static/lab/781e85bb50c8e8301c30de56b31b1f04.ttf) format("truetype"),url(/static/lab/03ba7cb710104df27f1c9c46d64bee4e.svg#fontawesome) format("svg")}.fa,.far,.fas{font-family:"Font Awesome 5 Free"}.fa,.fas{font-weight:900}</style><style>/*!
 * Font Awesome Free 5.14.0 by @fontawesome - https://fontawesome.com
 * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
 */
.fa.fa-glass:before{content:"\f000"}.fa.fa-meetup{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-star-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-star-o:before{content:"\f005"}.fa.fa-close:before,.fa.fa-remove:before{content:"\f00d"}.fa.fa-gear:before{content:"\f013"}.fa.fa-trash-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-trash-o:before{content:"\f2ed"}.fa.fa-file-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-o:before{content:"\f15b"}.fa.fa-clock-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-clock-o:before{content:"\f017"}.fa.fa-arrow-circle-o-down{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-arrow-circle-o-down:before{content:"\f358"}.fa.fa-arrow-circle-o-up{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-arrow-circle-o-up:before{content:"\f35b"}.fa.fa-play-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-play-circle-o:before{content:"\f144"}.fa.fa-repeat:before,.fa.fa-rotate-right:before{content:"\f01e"}.fa.fa-refresh:before{content:"\f021"}.fa.fa-list-alt{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-dedent:before{content:"\f03b"}.fa.fa-video-camera:before{content:"\f03d"}.fa.fa-picture-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-picture-o:before{content:"\f03e"}.fa.fa-photo{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-photo:before{content:"\f03e"}.fa.fa-image{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-image:before{content:"\f03e"}.fa.fa-pencil:before{content:"\f303"}.fa.fa-map-marker:before{content:"\f3c5"}.fa.fa-pencil-square-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-pencil-square-o:before{content:"\f044"}.fa.fa-share-square-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-share-square-o:before{content:"\f14d"}.fa.fa-check-square-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-check-square-o:before{content:"\f14a"}.fa.fa-arrows:before{content:"\f0b2"}.fa.fa-times-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-times-circle-o:before{content:"\f057"}.fa.fa-check-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-check-circle-o:before{content:"\f058"}.fa.fa-mail-forward:before{content:"\f064"}.fa.fa-expand:before{content:"\f424"}.fa.fa-compress:before{content:"\f422"}.fa.fa-eye,.fa.fa-eye-slash{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-warning:before{content:"\f071"}.fa.fa-calendar:before{content:"\f073"}.fa.fa-arrows-v:before{content:"\f338"}.fa.fa-arrows-h:before{content:"\f337"}.fa.fa-bar-chart{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-bar-chart:before{content:"\f080"}.fa.fa-bar-chart-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-bar-chart-o:before{content:"\f080"}.fa.fa-facebook-square,.fa.fa-twitter-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-gears:before{content:"\f085"}.fa.fa-thumbs-o-up{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-thumbs-o-up:before{content:"\f164"}.fa.fa-thumbs-o-down{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-thumbs-o-down:before{content:"\f165"}.fa.fa-heart-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-heart-o:before{content:"\f004"}.fa.fa-sign-out:before{content:"\f2f5"}.fa.fa-linkedin-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-linkedin-square:before{content:"\f08c"}.fa.fa-thumb-tack:before{content:"\f08d"}.fa.fa-external-link:before{content:"\f35d"}.fa.fa-sign-in:before{content:"\f2f6"}.fa.fa-github-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-lemon-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-lemon-o:before{content:"\f094"}.fa.fa-square-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-square-o:before{content:"\f0c8"}.fa.fa-bookmark-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-bookmark-o:before{content:"\f02e"}.fa.fa-facebook,.fa.fa-twitter{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-facebook:before{content:"\f39e"}.fa.fa-facebook-f{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-facebook-f:before{content:"\f39e"}.fa.fa-github{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-credit-card{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-feed:before{content:"\f09e"}.fa.fa-hdd-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hdd-o:before{content:"\f0a0"}.fa.fa-hand-o-right{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-o-right:before{content:"\f0a4"}.fa.fa-hand-o-left{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-o-left:before{content:"\f0a5"}.fa.fa-hand-o-up{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-o-up:before{content:"\f0a6"}.fa.fa-hand-o-down{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-o-down:before{content:"\f0a7"}.fa.fa-arrows-alt:before{content:"\f31e"}.fa.fa-group:before{content:"\f0c0"}.fa.fa-chain:before{content:"\f0c1"}.fa.fa-scissors:before{content:"\f0c4"}.fa.fa-files-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-files-o:before{content:"\f0c5"}.fa.fa-floppy-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-floppy-o:before{content:"\f0c7"}.fa.fa-navicon:before,.fa.fa-reorder:before{content:"\f0c9"}.fa.fa-google-plus,.fa.fa-google-plus-square,.fa.fa-pinterest,.fa.fa-pinterest-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-google-plus:before{content:"\f0d5"}.fa.fa-money{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-money:before{content:"\f3d1"}.fa.fa-unsorted:before{content:"\f0dc"}.fa.fa-sort-desc:before{content:"\f0dd"}.fa.fa-sort-asc:before{content:"\f0de"}.fa.fa-linkedin{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-linkedin:before{content:"\f0e1"}.fa.fa-rotate-left:before{content:"\f0e2"}.fa.fa-legal:before{content:"\f0e3"}.fa.fa-dashboard:before,.fa.fa-tachometer:before{content:"\f3fd"}.fa.fa-comment-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-comment-o:before{content:"\f075"}.fa.fa-comments-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-comments-o:before{content:"\f086"}.fa.fa-flash:before{content:"\f0e7"}.fa.fa-clipboard,.fa.fa-paste{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-paste:before{content:"\f328"}.fa.fa-lightbulb-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-lightbulb-o:before{content:"\f0eb"}.fa.fa-exchange:before{content:"\f362"}.fa.fa-cloud-download:before{content:"\f381"}.fa.fa-cloud-upload:before{content:"\f382"}.fa.fa-bell-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-bell-o:before{content:"\f0f3"}.fa.fa-cutlery:before{content:"\f2e7"}.fa.fa-file-text-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-text-o:before{content:"\f15c"}.fa.fa-building-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-building-o:before{content:"\f1ad"}.fa.fa-hospital-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hospital-o:before{content:"\f0f8"}.fa.fa-tablet:before{content:"\f3fa"}.fa.fa-mobile-phone:before,.fa.fa-mobile:before{content:"\f3cd"}.fa.fa-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-circle-o:before{content:"\f111"}.fa.fa-mail-reply:before{content:"\f3e5"}.fa.fa-github-alt{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-folder-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-folder-o:before{content:"\f07b"}.fa.fa-folder-open-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-folder-open-o:before{content:"\f07c"}.fa.fa-smile-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-smile-o:before{content:"\f118"}.fa.fa-frown-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-frown-o:before{content:"\f119"}.fa.fa-meh-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-meh-o:before{content:"\f11a"}.fa.fa-keyboard-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-keyboard-o:before{content:"\f11c"}.fa.fa-flag-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-flag-o:before{content:"\f024"}.fa.fa-mail-reply-all:before{content:"\f122"}.fa.fa-star-half-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-star-half-o:before{content:"\f089"}.fa.fa-star-half-empty{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-star-half-empty:before{content:"\f089"}.fa.fa-star-half-full{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-star-half-full:before{content:"\f089"}.fa.fa-code-fork:before{content:"\f126"}.fa.fa-chain-broken:before{content:"\f127"}.fa.fa-shield:before{content:"\f3ed"}.fa.fa-calendar-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-calendar-o:before{content:"\f133"}.fa.fa-css3,.fa.fa-html5,.fa.fa-maxcdn{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-ticket:before{content:"\f3ff"}.fa.fa-minus-square-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-minus-square-o:before{content:"\f146"}.fa.fa-level-up:before{content:"\f3bf"}.fa.fa-level-down:before{content:"\f3be"}.fa.fa-pencil-square:before{content:"\f14b"}.fa.fa-external-link-square:before{content:"\f360"}.fa.fa-compass{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-caret-square-o-down{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-caret-square-o-down:before{content:"\f150"}.fa.fa-toggle-down{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-toggle-down:before{content:"\f150"}.fa.fa-caret-square-o-up{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-caret-square-o-up:before{content:"\f151"}.fa.fa-toggle-up{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-toggle-up:before{content:"\f151"}.fa.fa-caret-square-o-right{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-caret-square-o-right:before{content:"\f152"}.fa.fa-toggle-right{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-toggle-right:before{content:"\f152"}.fa.fa-eur:before,.fa.fa-euro:before{content:"\f153"}.fa.fa-gbp:before{content:"\f154"}.fa.fa-dollar:before,.fa.fa-usd:before{content:"\f155"}.fa.fa-inr:before,.fa.fa-rupee:before{content:"\f156"}.fa.fa-cny:before,.fa.fa-jpy:before,.fa.fa-rmb:before,.fa.fa-yen:before{content:"\f157"}.fa.fa-rouble:before,.fa.fa-rub:before,.fa.fa-ruble:before{content:"\f158"}.fa.fa-krw:before,.fa.fa-won:before{content:"\f159"}.fa.fa-bitcoin,.fa.fa-btc{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-bitcoin:before{content:"\f15a"}.fa.fa-file-text:before{content:"\f15c"}.fa.fa-sort-alpha-asc:before{content:"\f15d"}.fa.fa-sort-alpha-desc:before{content:"\f881"}.fa.fa-sort-amount-asc:before{content:"\f160"}.fa.fa-sort-amount-desc:before{content:"\f884"}.fa.fa-sort-numeric-asc:before{content:"\f162"}.fa.fa-sort-numeric-desc:before{content:"\f886"}.fa.fa-xing,.fa.fa-xing-square,.fa.fa-youtube,.fa.fa-youtube-play,.fa.fa-youtube-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-youtube-play:before{content:"\f167"}.fa.fa-adn,.fa.fa-bitbucket,.fa.fa-bitbucket-square,.fa.fa-dropbox,.fa.fa-flickr,.fa.fa-instagram,.fa.fa-stack-overflow{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-bitbucket-square:before{content:"\f171"}.fa.fa-tumblr,.fa.fa-tumblr-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-long-arrow-down:before{content:"\f309"}.fa.fa-long-arrow-up:before{content:"\f30c"}.fa.fa-long-arrow-left:before{content:"\f30a"}.fa.fa-long-arrow-right:before{content:"\f30b"}.fa.fa-android,.fa.fa-apple,.fa.fa-dribbble,.fa.fa-foursquare,.fa.fa-gittip,.fa.fa-gratipay,.fa.fa-linux,.fa.fa-skype,.fa.fa-trello,.fa.fa-windows{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-gittip:before{content:"\f184"}.fa.fa-sun-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-sun-o:before{content:"\f185"}.fa.fa-moon-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-moon-o:before{content:"\f186"}.fa.fa-pagelines,.fa.fa-renren,.fa.fa-stack-exchange,.fa.fa-vk,.fa.fa-weibo{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-arrow-circle-o-right{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-arrow-circle-o-right:before{content:"\f35a"}.fa.fa-arrow-circle-o-left{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-arrow-circle-o-left:before{content:"\f359"}.fa.fa-caret-square-o-left{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-caret-square-o-left:before{content:"\f191"}.fa.fa-toggle-left{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-toggle-left:before{content:"\f191"}.fa.fa-dot-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-dot-circle-o:before{content:"\f192"}.fa.fa-vimeo-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-try:before,.fa.fa-turkish-lira:before{content:"\f195"}.fa.fa-plus-square-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-plus-square-o:before{content:"\f0fe"}.fa.fa-openid,.fa.fa-slack,.fa.fa-wordpress{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-bank:before,.fa.fa-institution:before{content:"\f19c"}.fa.fa-mortar-board:before{content:"\f19d"}.fa.fa-delicious,.fa.fa-digg,.fa.fa-drupal,.fa.fa-google,.fa.fa-joomla,.fa.fa-pied-piper-alt,.fa.fa-pied-piper-pp,.fa.fa-reddit,.fa.fa-reddit-square,.fa.fa-stumbleupon,.fa.fa-stumbleupon-circle,.fa.fa-yahoo{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-spoon:before{content:"\f2e5"}.fa.fa-behance,.fa.fa-behance-square,.fa.fa-steam,.fa.fa-steam-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-automobile:before{content:"\f1b9"}.fa.fa-envelope-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-envelope-o:before{content:"\f0e0"}.fa.fa-deviantart,.fa.fa-soundcloud,.fa.fa-spotify{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-file-pdf-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-pdf-o:before{content:"\f1c1"}.fa.fa-file-word-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-word-o:before{content:"\f1c2"}.fa.fa-file-excel-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-excel-o:before{content:"\f1c3"}.fa.fa-file-powerpoint-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-powerpoint-o:before{content:"\f1c4"}.fa.fa-file-image-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-image-o:before{content:"\f1c5"}.fa.fa-file-photo-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-photo-o:before{content:"\f1c5"}.fa.fa-file-picture-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-picture-o:before{content:"\f1c5"}.fa.fa-file-archive-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-archive-o:before{content:"\f1c6"}.fa.fa-file-zip-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-zip-o:before{content:"\f1c6"}.fa.fa-file-audio-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-audio-o:before{content:"\f1c7"}.fa.fa-file-sound-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-sound-o:before{content:"\f1c7"}.fa.fa-file-video-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-video-o:before{content:"\f1c8"}.fa.fa-file-movie-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-movie-o:before{content:"\f1c8"}.fa.fa-file-code-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-file-code-o:before{content:"\f1c9"}.fa.fa-codepen,.fa.fa-jsfiddle,.fa.fa-vine{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-life-bouy,.fa.fa-life-ring{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-life-bouy:before{content:"\f1cd"}.fa.fa-life-buoy{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-life-buoy:before{content:"\f1cd"}.fa.fa-life-saver{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-life-saver:before{content:"\f1cd"}.fa.fa-support{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-support:before{content:"\f1cd"}.fa.fa-circle-o-notch:before{content:"\f1ce"}.fa.fa-ra,.fa.fa-rebel{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-ra:before{content:"\f1d0"}.fa.fa-resistance{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-resistance:before{content:"\f1d0"}.fa.fa-empire,.fa.fa-ge{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-ge:before{content:"\f1d1"}.fa.fa-git,.fa.fa-git-square,.fa.fa-hacker-news,.fa.fa-y-combinator-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-y-combinator-square:before{content:"\f1d4"}.fa.fa-yc-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-yc-square:before{content:"\f1d4"}.fa.fa-qq,.fa.fa-tencent-weibo,.fa.fa-wechat,.fa.fa-weixin{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-wechat:before{content:"\f1d7"}.fa.fa-send:before{content:"\f1d8"}.fa.fa-paper-plane-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-paper-plane-o:before{content:"\f1d8"}.fa.fa-send-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-send-o:before{content:"\f1d8"}.fa.fa-circle-thin{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-circle-thin:before{content:"\f111"}.fa.fa-header:before{content:"\f1dc"}.fa.fa-sliders:before{content:"\f1de"}.fa.fa-futbol-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-futbol-o:before{content:"\f1e3"}.fa.fa-soccer-ball-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-soccer-ball-o:before{content:"\f1e3"}.fa.fa-slideshare,.fa.fa-twitch,.fa.fa-yelp{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-newspaper-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-newspaper-o:before{content:"\f1ea"}.fa.fa-cc-amex,.fa.fa-cc-discover,.fa.fa-cc-mastercard,.fa.fa-cc-paypal,.fa.fa-cc-stripe,.fa.fa-cc-visa,.fa.fa-google-wallet,.fa.fa-paypal{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-bell-slash-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-bell-slash-o:before{content:"\f1f6"}.fa.fa-trash:before{content:"\f2ed"}.fa.fa-copyright{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-eyedropper:before{content:"\f1fb"}.fa.fa-area-chart:before{content:"\f1fe"}.fa.fa-pie-chart:before{content:"\f200"}.fa.fa-line-chart:before{content:"\f201"}.fa.fa-angellist,.fa.fa-ioxhost,.fa.fa-lastfm,.fa.fa-lastfm-square{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-cc{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-cc:before{content:"\f20a"}.fa.fa-ils:before,.fa.fa-shekel:before,.fa.fa-sheqel:before{content:"\f20b"}.fa.fa-meanpath{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-meanpath:before{content:"\f2b4"}.fa.fa-buysellads,.fa.fa-connectdevelop,.fa.fa-dashcube,.fa.fa-forumbee,.fa.fa-leanpub,.fa.fa-sellsy,.fa.fa-shirtsinbulk,.fa.fa-simplybuilt,.fa.fa-skyatlas{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-diamond{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-diamond:before{content:"\f3a5"}.fa.fa-intersex:before{content:"\f224"}.fa.fa-facebook-official{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-facebook-official:before{content:"\f09a"}.fa.fa-pinterest-p,.fa.fa-whatsapp{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-hotel:before{content:"\f236"}.fa.fa-medium,.fa.fa-viacoin,.fa.fa-y-combinator,.fa.fa-yc{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-yc:before{content:"\f23b"}.fa.fa-expeditedssl,.fa.fa-opencart,.fa.fa-optin-monster{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-battery-4:before,.fa.fa-battery:before{content:"\f240"}.fa.fa-battery-3:before{content:"\f241"}.fa.fa-battery-2:before{content:"\f242"}.fa.fa-battery-1:before{content:"\f243"}.fa.fa-battery-0:before{content:"\f244"}.fa.fa-object-group,.fa.fa-object-ungroup,.fa.fa-sticky-note-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-sticky-note-o:before{content:"\f249"}.fa.fa-cc-diners-club,.fa.fa-cc-jcb{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-clone,.fa.fa-hourglass-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hourglass-o:before{content:"\f254"}.fa.fa-hourglass-1:before{content:"\f251"}.fa.fa-hourglass-2:before{content:"\f252"}.fa.fa-hourglass-3:before{content:"\f253"}.fa.fa-hand-rock-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-rock-o:before{content:"\f255"}.fa.fa-hand-grab-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-grab-o:before{content:"\f255"}.fa.fa-hand-paper-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-paper-o:before{content:"\f256"}.fa.fa-hand-stop-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-stop-o:before{content:"\f256"}.fa.fa-hand-scissors-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-scissors-o:before{content:"\f257"}.fa.fa-hand-lizard-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-lizard-o:before{content:"\f258"}.fa.fa-hand-spock-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-spock-o:before{content:"\f259"}.fa.fa-hand-pointer-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-pointer-o:before{content:"\f25a"}.fa.fa-hand-peace-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-hand-peace-o:before{content:"\f25b"}.fa.fa-registered{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-chrome,.fa.fa-creative-commons,.fa.fa-firefox,.fa.fa-get-pocket,.fa.fa-gg,.fa.fa-gg-circle,.fa.fa-internet-explorer,.fa.fa-odnoklassniki,.fa.fa-odnoklassniki-square,.fa.fa-opera,.fa.fa-safari,.fa.fa-tripadvisor,.fa.fa-wikipedia-w{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-television:before{content:"\f26c"}.fa.fa-500px,.fa.fa-amazon,.fa.fa-contao{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-calendar-plus-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-calendar-plus-o:before{content:"\f271"}.fa.fa-calendar-minus-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-calendar-minus-o:before{content:"\f272"}.fa.fa-calendar-times-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-calendar-times-o:before{content:"\f273"}.fa.fa-calendar-check-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-calendar-check-o:before{content:"\f274"}.fa.fa-map-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-map-o:before{content:"\f279"}.fa.fa-commenting:before{content:"\f4ad"}.fa.fa-commenting-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-commenting-o:before{content:"\f4ad"}.fa.fa-houzz,.fa.fa-vimeo{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-vimeo:before{content:"\f27d"}.fa.fa-black-tie,.fa.fa-edge,.fa.fa-fonticons,.fa.fa-reddit-alien{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-credit-card-alt:before{content:"\f09d"}.fa.fa-codiepie,.fa.fa-fort-awesome,.fa.fa-mixcloud,.fa.fa-modx,.fa.fa-product-hunt,.fa.fa-scribd,.fa.fa-usb{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-pause-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-pause-circle-o:before{content:"\f28b"}.fa.fa-stop-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-stop-circle-o:before{content:"\f28d"}.fa.fa-bluetooth,.fa.fa-bluetooth-b,.fa.fa-envira,.fa.fa-gitlab,.fa.fa-wheelchair-alt,.fa.fa-wpbeginner,.fa.fa-wpforms{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-wheelchair-alt:before{content:"\f368"}.fa.fa-question-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-question-circle-o:before{content:"\f059"}.fa.fa-volume-control-phone:before{content:"\f2a0"}.fa.fa-asl-interpreting:before{content:"\f2a3"}.fa.fa-deafness:before,.fa.fa-hard-of-hearing:before{content:"\f2a4"}.fa.fa-glide,.fa.fa-glide-g{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-signing:before{content:"\f2a7"}.fa.fa-first-order,.fa.fa-google-plus-official,.fa.fa-pied-piper,.fa.fa-snapchat,.fa.fa-snapchat-ghost,.fa.fa-snapchat-square,.fa.fa-themeisle,.fa.fa-viadeo,.fa.fa-viadeo-square,.fa.fa-yoast{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-google-plus-official:before{content:"\f2b3"}.fa.fa-google-plus-circle{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-google-plus-circle:before{content:"\f2b3"}.fa.fa-fa,.fa.fa-font-awesome{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-fa:before{content:"\f2b4"}.fa.fa-handshake-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-handshake-o:before{content:"\f2b5"}.fa.fa-envelope-open-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-envelope-open-o:before{content:"\f2b6"}.fa.fa-linode{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-address-book-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-address-book-o:before{content:"\f2b9"}.fa.fa-vcard:before{content:"\f2bb"}.fa.fa-address-card-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-address-card-o:before{content:"\f2bb"}.fa.fa-vcard-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-vcard-o:before{content:"\f2bb"}.fa.fa-user-circle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-user-circle-o:before{content:"\f2bd"}.fa.fa-user-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-user-o:before{content:"\f007"}.fa.fa-id-badge{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-drivers-license:before{content:"\f2c2"}.fa.fa-id-card-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-id-card-o:before{content:"\f2c2"}.fa.fa-drivers-license-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-drivers-license-o:before{content:"\f2c2"}.fa.fa-free-code-camp,.fa.fa-quora,.fa.fa-telegram{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-thermometer-4:before,.fa.fa-thermometer:before{content:"\f2c7"}.fa.fa-thermometer-3:before{content:"\f2c8"}.fa.fa-thermometer-2:before{content:"\f2c9"}.fa.fa-thermometer-1:before{content:"\f2ca"}.fa.fa-thermometer-0:before{content:"\f2cb"}.fa.fa-bathtub:before,.fa.fa-s15:before{content:"\f2cd"}.fa.fa-window-maximize,.fa.fa-window-restore{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-times-rectangle:before{content:"\f410"}.fa.fa-window-close-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-window-close-o:before{content:"\f410"}.fa.fa-times-rectangle-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-times-rectangle-o:before{content:"\f410"}.fa.fa-bandcamp,.fa.fa-eercast,.fa.fa-etsy,.fa.fa-grav,.fa.fa-imdb,.fa.fa-ravelry{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-eercast:before{content:"\f2da"}.fa.fa-snowflake-o{font-family:"Font Awesome 5 Free";font-weight:400}.fa.fa-snowflake-o:before{content:"\f2dc"}.fa.fa-superpowers,.fa.fa-wpexplorer{font-family:"Font Awesome 5 Brands";font-weight:400}.fa.fa-cab:before{content:"\f1ba"}</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-top: 1px solid var(--jp-border-color2);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-Collapse-header {
  padding: 1px 12px;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size2);
}

.jp-Collapse-header:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Collapse-contents {
  padding: 0px 12px 0px 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0px;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0px 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.lm-CommandPalette-wrapper::after {
  content: ' ';
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  height: 30px;
  width: 10px;
  padding: 0px 10px;
  background-image: var(--jp-icon-search-white);
  background-size: 20px;
  background-repeat: no-repeat;
  background-position: center;
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color3);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0px;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color3);
}

.lm-CommandPalette-item.lm-mod-active {
  background: var(--jp-layout-color3);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  background: var(--jp-layout-color4);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color3);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.4;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty:after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0px 8px;
  color: var(--jp-content-font-color3);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0px;
  left: 0px;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px;
  padding-bottom: 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0px;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

.jp-Dialog-header {
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0px 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

.jp-HoverBox.jp-mod-outofview {
  display: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}
</style><style>/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;

  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;

  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #aa00ff;

  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;

  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;

  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;

  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;

  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;

  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;

  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;

  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;

  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;

  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ffff00;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;

  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;

  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;

  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;

  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;

  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eeeeee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent:before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent:after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0px 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  height: 28px;
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  background-color: var(--jp-layout-color1);
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0px 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  height: 32px;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 1;
  overflow-x: hidden;
}

.jp-Toolbar:hover {
  overflow-x: auto;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px;
  margin: 0px;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px 6px;
  margin: 0px;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent span {
  padding: 0px;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-DataGrid {
  min-width: 64px;
  min-height: 64px;
  border: 1px solid #a0a0a0;
}

.lm-DataGrid-scrollCorner {
  background-color: #f0f0f0;
}

.lm-DataGrid-scrollCorner::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 1px;
  height: 1px;
  background-color: #a0a0a0;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| DockPanel
|----------------------------------------------------------------------------*/

.lm-DockPanel-widget {
  background: var(--jp-layout-color0);
  border-left: var(--jp-border-width) solid var(--jp-border-color1);
  border-right: var(--jp-border-width) solid var(--jp-border-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
}

.lm-DockPanel-overlay {
  background: rgba(33, 150, 243, 0.1);
  border: var(--jp-border-width) dashed var(--jp-brand-color1);
  transition-property: top, left, right, bottom;
  transition-duration: 150ms;
  transition-timing-function: ease;
}

.lm-DockPanel-overlay.lm-mod-root-top,
.lm-DockPanel-overlay.lm-mod-root-left,
.lm-DockPanel-overlay.lm-mod-root-right,
.lm-DockPanel-overlay.lm-mod-root-bottom,
.lm-DockPanel-overlay.lm-mod-root-center {
  border-width: 2px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-menubar-height: 28px;
  --jp-private-menu-item-height: 24px;
}

/*-----------------------------------------------------------------------------
| MenuBar
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  padding-left: 5px;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

.lm-MenuBar-menu {
  transform: translateY(calc(-2 * var(--jp-border-width)));
}

.lm-MenuBar-item {
  padding: 0px 8px;
  border-left: var(--jp-border-width) solid transparent;
  border-right: var(--jp-border-width) solid transparent;
  line-height: var(--jp-private-menubar-height);
}

.lm-MenuBar-item.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-MenuBar.lm-mod-active .lm-MenuBar-item.lm-mod-active {
  z-index: 10001;
  background: var(--jp-layout-color0);
  border-left: var(--jp-border-width) solid var(--jp-border-color1);
  border-right: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-elevation-z6);
}

.lm-MenuBar-item.lm-mod-disabled {
  color: var(--jp-ui-font-color3);
}

.lm-MenuBar-item.lm-type-separator {
  margin: 2px;
  padding: 0;
  border: none;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
}

.lm-MenuBar-itemMnemonic {
  text-decoration: underline;
}

/*-----------------------------------------------------------------------------
| Menu
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  padding: 4px 0px;
  background: var(--jp-layout-color0);
  color: var(--jp-ui-font-color1);
  border: var(--jp-border-width) solid var(--jp-border-color1);
  font-size: var(--jp-ui-font-size1);
  box-shadow: var(--jp-elevation-z6);
}

.lm-Menu-item {
  min-height: var(--jp-private-menu-item-height);
  max-height: var(--jp-private-menu-item-height);
  padding: 0px;
  line-height: var(--jp-private-menu-item-height);
}

.lm-Menu-item.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-Menu-item.lm-mod-disabled {
  color: var(--jp-ui-font-color3);
}

.lm-Menu-itemIcon {
  width: 21px;
  padding: 0px 2px 0px 4px;
  margin-top: -2px;
}

.lm-Menu-itemLabel {
  padding: 0px 32px 0px 2px;
}

.lm-Menu-itemMnemonic {
  text-decoration: underline;
}

.lm-Menu-itemShortcut {
  padding: 0px;
}

.lm-Menu-itemSubmenuIcon {
  width: 18px;
  padding: 0px 4px 0px 0px;
}

.lm-Menu-item[data-type='separator'] > div {
  padding: 0;
  height: 9px;
}

.lm-Menu-item[data-type='separator'] > div::after {
  content: '';
  display: block;
  position: relative;
  top: 4px;
  border-top: var(--jp-border-width) solid var(--jp-layout-color2);
}

/* gray out icon/caret for disable menu items */
.lm-Menu-item.lm-mod-disabled > .lm-Menu-itemIcon,
.lm-Menu-item[data-type='submenu'].lm-mod-disabled > .lm-Menu-itemSubmenuIcon {
  opacity: 0.4;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/*
 * Webkit scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-corner {
  background: var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-thumb {
  background: rgb(var(--jp-scrollbar-thumb-color));
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-right: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-bottom: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar */

[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-corner,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-corner {
  background-color: transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-thumb,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid transparent;
  border-right: var(--jp-scrollbar-endpad) solid transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid transparent;
  border-bottom: var(--jp-scrollbar-endpad) solid transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0px solid transparent;
  border-right: 0px solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0px solid transparent;
  border-bottom: 0px solid transparent;
}

/*
 * Phosphor
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  /* These need to be root because tabs get attached to the body during dragging. */
  --jp-private-horizontal-tab-height: 24px;
  --jp-private-horizontal-tab-width: 216px;
  --jp-private-horizontal-tab-active-top-border: 2px;
}

/*-----------------------------------------------------------------------------
| Tabs in the dock panel
|----------------------------------------------------------------------------*/

.lm-DockPanel-tabBar {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  overflow: visible;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  min-height: calc(
    var(--jp-private-horizontal-tab-height) + 2 * var(--jp-border-width)
  );
}

.lm-DockPanel-tabBar[data-orientation='vertical'] {
  min-width: 80px;
}

.lm-DockPanel-tabBar > .lm-TabBar-content {
  align-items: flex-end;
  min-width: 0;
  min-height: 0;
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  flex: 0 1 var(--jp-private-horizontal-tab-width);
  min-height: calc(
    var(--jp-private-horizontal-tab-height) + var(--jp-border-width)
  );
  min-width: 0px;
  margin-left: calc(-1 * var(--jp-border-width));
  line-height: var(--jp-private-horizontal-tab-height);
  padding: 0px 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-border-color1);
  border-bottom: none;
  position: relative;
}

.lm-DockPanel-tabBar .lm-TabBar-tab:hover:not(.lm-mod-current) {
  background: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab:first-child {
  margin-left: 0;
}

/* This is a current tab of a tab bar in the dock panel: each tab bar has 1. */
.lm-DockPanel-tabBar .lm-TabBar-tab.lm-mod-current {
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color0);
  min-height: calc(
    var(--jp-private-horizontal-tab-height) + 2 * var(--jp-border-width)
  );
  transform: translateY(var(--jp-border-width));
}

/* This is the main application level current tab: only 1 exists. */
.lm-DockPanel-tabBar .lm-TabBar-tab.jp-mod-current:before {
  position: absolute;
  top: calc(-1 * var(--jp-border-width));
  left: calc(-1 * var(--jp-border-width));
  content: '';
  height: var(--jp-private-horizontal-tab-active-top-border);
  width: calc(100% + 2 * var(--jp-border-width));
  background: var(--jp-brand-color1);
}

/* This is the left tab bar current tab: only 1 exists. */
.lm-TabBar-tab.lm-mod-current {
  color: var(--jp-ui-font-color0);
  background: var(--jp-layout-color1);
}

.lm-TabBar-tab.lm-mod-current:hover {
  background: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar.lm-mod-left .lm-TabBar-tab,
.lm-DockPanel-tabBar .lm-TabBar.lm-mod-right .lm-TabBar-tab {
  flex: 0 1 40px;
  margin-top: -1px;
  line-height: 40px;
}

.lm-DockPanel-tabBar .lm-TabBar.lm-mod-left .lm-TabBar-tab {
  border-right: none;
}

.lm-DockPanel-tabBar .lm-TabBar.lm-mod-right .lm-TabBar-tab {
  border-left: none;
}

.lm-DockPanel-tabBar .lm-TabBar.lm-mod-left .lm-TabBar-tab:first-child,
.lm-DockPanel-tabBar .lm-TabBar.lm-mod-right .lm-TabBar-tab:first-child {
  margin-top: 0;
}

.lm-DockPanel-tabBar .lm-TabBar.lm-mod-left .lm-TabBar-tab.lm-mod-current,
.lm-DockPanel-tabBar .lm-TabBar.lm-mod-right .lm-TabBar-tab.lm-mod-current {
  min-width: 80px;
  max-width: 80px;
}

.lm-DockPanel-tabBar .lm-TabBar.lm-mod-right .lm-TabBar-tab.lm-mod-current {
  transform: translateX(-1px);
}

.lm-DockPanel-tabBar .lm-TabBar-tab .lm-TabBar-tabIcon,
.lm-TabBar-tab.lm-mod-drag-image .lm-TabBar-tabIcon {
  width: 14px;
  background-position: left center;
  background-repeat: no-repeat;
  background-size: 14px;
  margin-right: 4px;
}

.lm-DockPanel-tabBar .lm-TabBar-tab.lm-mod-current .lm-TabBar-tabIcon {
  margin-bottom: var(--jp-border-width);
}

.lm-TabBar-WindowTabLabel {
  margin-top: 4px;
}

.lm-TabBar-tab.lm-mod-drag-image {
  background: var(--jp-layout-color1);
  border: var(--jp-border-width) solid var(--jp-border-color1);
  border-top: var(--jp-border-width) solid var(--jp-brand-color1);
  box-shadow: var(--jp-elevation-z4);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-horizontal-tab-height);
  min-height: var(--jp-private-horizontal-tab-height);
  min-width: var(--jp-private-horizontal-tab-width);
  padding: 0px 10px;
  transform: translateX(-40%) translateY(-58%);
}
</style><style>/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-flat-button-height: 24px;
  --jp-flat-button-padding: 8px 12px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button {
  border-radius: var(--jp-border-radius);
}

button.jp-mod-styled.jp-mod-accept {
  background: var(--md-blue-500);
  border: 0;
  color: white;
}

button.jp-mod-styled.jp-mod-accept:hover {
  background: var(--md-blue-600);
}

button.jp-mod-styled.jp-mod-accept:active {
  background: var(--md-blue-700);
}

button.jp-mod-styled.jp-mod-reject {
  background: var(--md-grey-500);
  border: 0;
  color: white;
}

button.jp-mod-styled.jp-mod-reject:hover {
  background: var(--md-grey-600);
}

button.jp-mod-styled.jp-mod-reject:active {
  background: var(--md-grey-700);
}

button.jp-mod-styled.jp-mod-warn {
  background: var(--jp-error-color1);
  border: 0;
  color: white;
}

button.jp-mod-styled.jp-mod-warn:hover {
  background: var(--md-red-600);
}

button.jp-mod-styled.jp-mod-warn:active {
  background: var(--md-red-700);
}

.jp-Button-flat {
  text-decoration: none;
  padding: var(--jp-flat-button-padding);
  color: var(--jp-warn-color1);
  font-weight: 500;
  background-color: transparent;
  height: var(--jp-private-running-shutdown-button-height);
  line-height: var(--jp-private-running-shutdown-button-height);
  transition: background-color 0.1s ease;
  border-radius: 2px;
}

.jp-Button-flat:hover {
  background-color: rgba(153, 153, 153, 0.1);
}

.jp-Button-flat:focus {
  border: none;
  box-shadow: none;
  background-color: rgba(153, 153, 153, 0.2);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-sidebar-tab-width: 32px;
}

/*-----------------------------------------------------------------------------
| SideBar
|----------------------------------------------------------------------------*/

.jp-SideBar {
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-SideBar.lm-TabBar {
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color2);
  font-size: var(--jp-ui-font-size1);
  min-width: calc(var(--jp-private-sidebar-tab-width) + var(--jp-border-width));
  max-width: calc(var(--jp-private-sidebar-tab-width) + var(--jp-border-width));
  overflow: visible;
  display: block;
}

.jp-SideBar .lm-TabBar-content,
.jp-SideBar .lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  align-items: stretch;
  list-style-type: none;
  height: var(--jp-private-sidebar-tab-width);
  transform-origin: 0 0 0;
}

.jp-SideBar .lm-TabBar-tab {
  padding: 0 16px;
  border: none;
  overflow: visible;
}

.jp-SideBar .lm-TabBar-tab.lm-mod-current {
  min-height: calc(
    var(--jp-private-sidebar-tab-width) + var(--jp-border-width)
  );
  max-height: calc(
    var(--jp-private-sidebar-tab-width) + var(--jp-border-width)
  );
  /* transform: translateY(var(--jp-border-width)); */
}

.jp-SideBar .lm-TabBar-tab:not(.lm-mod-current) {
  background: var(--jp-layout-color2);
}

.jp-SideBar .lm-TabBar-tabIcon.jp-SideBar-tabIcon {
  min-width: 20px;
  min-height: 20px;
  background-size: 20px;
  display: inline-block;
  vertical-align: middle;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-SideBar .lm-TabBar-tabLabel {
  line-height: var(--jp-private-sidebar-tab-width);
}

.jp-SideBar .lm-TabBar-tab:hover:not(.lm-mod-current) {
  background: var(--jp-layout-color1);
}

/* Left */

/* Borders */

.jp-SideBar.lm-TabBar.jp-mod-left {
  border-right: var(--jp-border-width) solid var(--jp-border-color0);
}

.jp-SideBar.lm-TabBar.jp-mod-left .lm-TabBar-tab + .lm-TabBar-tab {
  border-right: var(--jp-border-width) solid var(--jp-layout-color2);
}

.jp-SideBar.lm-TabBar.jp-mod-left
  .lm-TabBar-tab.lm-mod-current
  + .lm-TabBar-tab {
  border-right: var(--jp-border-width) solid var(--jp-border-color0);
}

.jp-SideBar.lm-TabBar.jp-mod-left
  .lm-TabBar-tab
  + .lm-TabBar-tab.lm-mod-current {
  border-right: var(--jp-border-width) solid var(--jp-border-color0);
}

.jp-SideBar.lm-TabBar.jp-mod-left .lm-TabBar-tab.lm-mod-current:last-child {
  border-left: var(--jp-border-width) solid var(--jp-border-color0);
}

/* Transforms */

.jp-SideBar.lm-TabBar.jp-mod-left .lm-TabBar-content {
  flex-direction: row-reverse;
  transform: rotate(-90deg) translateX(-100%);
}

.jp-SideBar.lm-TabBar.jp-mod-left
  .lm-TabBar-tab:not(.lm-mod-current)
  .lm-TabBar-tabIcon {
  transform: rotate(90deg);
}

.jp-SideBar.lm-TabBar.jp-mod-left
  .lm-TabBar-tab.lm-mod-current
  .lm-TabBar-tabIcon {
  transform: rotate(90deg)
    translate(
      calc(-0.5 * var(--jp-border-width)),
      calc(-0.5 * var(--jp-border-width))
    );
}

/* Right */

/* Borders */

.jp-SideBar.lm-TabBar.jp-mod-right {
  border-left: var(--jp-border-width) solid var(--jp-border-color0);
}

.jp-SideBar.lm-TabBar.jp-mod-right .lm-TabBar-tab + .lm-TabBar-tab {
  border-left: var(--jp-border-width) solid var(--jp-layout-color2);
}

.jp-SideBar.lm-TabBar.jp-mod-right
  .lm-TabBar-tab.lm-mod-current
  + .lm-TabBar-tab {
  border-left: var(--jp-border-width) solid var(--jp-border-color0);
}

.jp-SideBar.lm-TabBar.jp-mod-right
  .lm-TabBar-tab
  + .lm-TabBar-tab.lm-mod-current {
  border-left: var(--jp-border-width) solid var(--jp-border-color0);
}

.jp-SideBar.lm-TabBar.jp-mod-right .lm-TabBar-tab.lm-mod-current:last-child {
  border-right: var(--jp-border-width) solid var(--jp-border-color0);
}

/* Transforms */

.jp-SideBar.lm-TabBar.jp-mod-right .lm-TabBar-content {
  flex-direction: row;
  transform: rotate(90deg) translateY(-100%);
}

.jp-SideBar.lm-TabBar.jp-mod-right
  .lm-TabBar-tab:not(.lm-mod-current)
  .lm-TabBar-tabIcon {
  transform: rotate(-90deg);
}

.jp-SideBar.lm-TabBar.jp-mod-right
  .lm-TabBar-tab.lm-mod-current
  .lm-TabBar-tabIcon {
  transform: rotate(-90deg)
    translate(
      calc(0.5 * var(--jp-border-width)),
      calc(-0.5 * var(--jp-border-width))
    );
}

/* Stack panels */

#jp-left-stack > .lm-Widget,
#jp-right-stack > .lm-Widget {
  min-width: var(--jp-sidebar-min-width);
}

#jp-right-stack {
  border-left: var(--jp-border-width) solid var(--jp-border-color1);
}

#jp-left-stack {
  border-right: var(--jp-border-width) solid var(--jp-border-color1);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

body {
  font-family: var(--jp-ui-font-family);
  background: var(--jp-layout-color3);
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.jp-LabShell {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.jp-LabShell.jp-mod-devMode {
  border-top: 4px solid red;
}

#jp-main-dock-panel {
  padding: 5px;
}

#jp-top-panel {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color0);
  background: var(--jp-layout-color1);
  display: flex;
  min-height: var(--jp-private-menubar-height);
}

#jp-bottom-panel {
  background: var(--jp-layout-color1);
  display: flex;
}

/* Sibling imports */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2019, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-PropertyInspector {
  display: flex;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
}

.jp-PropertyInspector-content {
  flex-grow: 1;
}

.jp-PropertyInspector-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
}

.jp-PropertyInspector-placeholderContent {
  padding: 8px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-RedirectForm input {
  display: block;
  margin-top: 10px;
  width: 100%;
}

.jp-RedirectForm-warning {
  color: var(--jp-warn-color0);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

#jupyterlab-splash {
  z-index: 10;
  position: absolute;
  overflow: hidden;
  width: 100%;
  height: 100%;
  background-position: center 40%;
  background-repeat: no-repeat;
  background-size: cover;
}

#jupyterlab-splash.light {
  background-color: white;
}

#jupyterlab-splash.dark {
  background-color: var(--md-grey-900);
}

.splash-fade {
  animation: 0.5s fade-out forwards;
}

#galaxy {
  position: relative;
  width: 100%;
  height: 100%;
}

.planet {
  background-repeat: no-repeat;
  background-size: cover;
  animation-iteration-count: infinite;
  animation-name: orbit;
}

#moon1.orbit {
  opacity: 1;
  animation: orbit 2s ease;
  width: 200px;
  height: 140px;
  margin-top: -53px;
  margin-left: -54px;
}

#moon2.orbit {
  opacity: 1;
  animation: orbit 2s ease;
  width: 132px;
  height: 180px;
  margin-top: -66px;
  margin-left: -85px;
}

#moon3.orbit {
  opacity: 1;
  display: flex;
  align-items: flex-end;
  animation: orbit 2s ease;
  width: 220px;
  height: 166px;
  margin-top: -96px;
  margin-left: -50px;
}

#moon1 .planet {
  height: 12px;
  width: 12px;
  border-radius: 50%;
}

#moon2 .planet {
  height: 16px;
  width: 16px;
  border-radius: 50%;
  float: right;
}

#moon3 .planet {
  height: 20px;
  width: 20px;
  border-radius: 50%;
}

#jupyterlab-splash.light #moon1 .planet {
  background-color: #6f7070;
}

#jupyterlab-splash.light #moon2 .planet {
  background-color: #767677;
}

#jupyterlab-splash.light #moon3 .planet {
  background-color: #989798;
}

#jupyterlab-splash.dark #moon1 .planet,
#jupyterlab-splash.dark #moon2 .planet,
#jupyterlab-splash.dark #moon3 .planet {
  background-color: white;
}

.orbit {
  animation-iteration-count: 1;
  position: absolute;
  top: 50%;
  left: 50%;
  border-radius: 50%;
}

@keyframes orbit {
  0% {
    transform: rotateZ(0deg);
  }
  100% {
    transform: rotateZ(-720deg);
  }
}

@keyframes orbit2 {
  0% {
    transform: rotateZ(0deg);
  }
  100% {
    transform: rotateZ(720deg);
  }
}

@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes fade-out {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ body.p-mod-override-cursor *, /* </DEPRECATED> */
body.lm-mod-override-cursor * {
  cursor: inherit !important;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 300px;
  color: black;
  direction: ltr;
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
}
.CodeMirror-linenumbers {}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker { color: black; }
.CodeMirror-guttermarker-subtle { color: #999; }

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0 !important;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}
.cm-fat-cursor-mark {
  background-color: rgba(20, 255, 20, 0.5);
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
}
.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@-webkit-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {}

.cm-tab { display: inline-block; text-decoration: inherit; }

.CodeMirror-rulers {
  position: absolute;
  left: 0; right: 0; top: -50px; bottom: 0;
  overflow: hidden;
}
.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  top: 0; bottom: 0;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {color: blue;}
.cm-s-default .cm-quote {color: #090;}
.cm-negative {color: #d44;}
.cm-positive {color: #292;}
.cm-header, .cm-strong {font-weight: bold;}
.cm-em {font-style: italic;}
.cm-link {text-decoration: underline;}
.cm-strikethrough {text-decoration: line-through;}

.cm-s-default .cm-keyword {color: #708;}
.cm-s-default .cm-atom {color: #219;}
.cm-s-default .cm-number {color: #164;}
.cm-s-default .cm-def {color: #00f;}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {}
.cm-s-default .cm-variable-2 {color: #05a;}
.cm-s-default .cm-variable-3, .cm-s-default .cm-type {color: #085;}
.cm-s-default .cm-comment {color: #a50;}
.cm-s-default .cm-string {color: #a11;}
.cm-s-default .cm-string-2 {color: #f50;}
.cm-s-default .cm-meta {color: #555;}
.cm-s-default .cm-qualifier {color: #555;}
.cm-s-default .cm-builtin {color: #30a;}
.cm-s-default .cm-bracket {color: #997;}
.cm-s-default .cm-tag {color: #170;}
.cm-s-default .cm-attribute {color: #00c;}
.cm-s-default .cm-hr {color: #999;}
.cm-s-default .cm-link {color: #00c;}

.cm-s-default .cm-error {color: #f00;}
.cm-invalidchar {color: #f00;}

.CodeMirror-composing { border-bottom: 2px solid; }

/* Default styles for common addons */

div.CodeMirror span.CodeMirror-matchingbracket {color: #0b0;}
div.CodeMirror span.CodeMirror-nonmatchingbracket {color: #a22;}
.CodeMirror-matchingtag { background: rgba(255, 150, 0, .3); }
.CodeMirror-activeline-background {background: #e8f2ff;}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white;
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 30px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -30px; margin-right: -30px;
  padding-bottom: 30px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative;
}
.CodeMirror-sizer {
  position: relative;
  border-right: 30px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
}
.CodeMirror-vscrollbar {
  right: 0; top: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.CodeMirror-hscrollbar {
  bottom: 0; left: 0;
  overflow-y: hidden;
  overflow-x: scroll;
}
.CodeMirror-scrollbar-filler {
  right: 0; bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0; bottom: 0;
}

.CodeMirror-gutters {
  position: absolute; left: 0; top: 0;
  min-height: 100%;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  vertical-align: top;
  margin-bottom: -30px;
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0; bottom: 0;
  z-index: 4;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper ::selection { background-color: transparent }
.CodeMirror-gutter-wrapper ::-moz-selection { background-color: transparent }

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0; -webkit-border-radius: 0; border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-variant-ligatures: contextual;
  font-variant-ligatures: contextual;
}
.CodeMirror-wrap pre.CodeMirror-line,
.CodeMirror-wrap pre.CodeMirror-line-like {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0; right: 0; top: 0; bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  padding: 0.1px; /* Force widget margins to stay inside of the container */
}

.CodeMirror-widget {}

.CodeMirror-rtl pre { direction: rtl; }

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
  pointer-events: none;
}
.CodeMirror-measure pre { position: static; }

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
}

.CodeMirror-selected { background: #d9d9d9; }
.CodeMirror-focused .CodeMirror-selected { background: #d7d4f0; }
.CodeMirror-crosshair { cursor: crosshair; }
.CodeMirror-line::selection, .CodeMirror-line > span::selection, .CodeMirror-line > span > span::selection { background: #d7d4f0; }
.CodeMirror-line::-moz-selection, .CodeMirror-line > span::-moz-selection, .CodeMirror-line > span > span::-moz-selection { background: #d7d4f0; }

.cm-searching {
  background-color: #ffa;
  background-color: rgba(255, 255, 0, .4);
}

/* Used to force a border model for a node */
.cm-force-border { padding-right: .1px; }

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after { content: ''; }

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext { background: none; }
</style><style>.CodeMirror-dialog {
  position: absolute;
  left: 0; right: 0;
  background: inherit;
  z-index: 15;
  padding: .1em .8em;
  overflow: hidden;
  color: inherit;
}

.CodeMirror-dialog-top {
  border-bottom: 1px solid #eee;
  top: 0;
}

.CodeMirror-dialog-bottom {
  border-top: 1px solid #eee;
  bottom: 0;
}

.CodeMirror-dialog input {
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
}

.CodeMirror-dialog button {
  font-size: 70%;
}
</style><style>.CodeMirror-foldmarker {
  color: blue;
  text-shadow: #b9f 1px 1px 2px, #b9f -1px -1px 2px, #b9f 1px -1px 2px, #b9f -1px 1px 2px;
  font-family: arial;
  line-height: .3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: .7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.CodeMirror {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;
  /* Changed to auto to autogrow */
}

.CodeMirror pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* This causes https://github.com/jupyter/jupyterlab/issues/522 */
/* May not cause it not because we changed it! */
.CodeMirror-lines {
  padding: var(--jp-code-padding) 0;
}

.CodeMirror-linenumber {
  padding: 0 8px;
}

.jp-CodeMirrorEditor {
  cursor: text;
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.CodeMirror.jp-mod-readOnly .CodeMirror-cursor {
  display: none;
}

.CodeMirror-gutters {
  border-right: 1px solid var(--jp-border-color2);
  background-color: var(--jp-layout-color0);
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.CodeMirror-selectedtext.cm-searching {
  background-color: var(--jp-search-selected-match-background-color) !important;
  color: var(--jp-search-selected-match-color) !important;
}

.cm-searching {
  background-color: var(
    --jp-search-unselected-match-background-color
  ) !important;
  color: var(--jp-search-unselected-match-color) !important;
}

.CodeMirror-focused .CodeMirror-selected {
  background-color: var(--jp-editor-selected-focused-background);
}

.CodeMirror-selected {
  background-color: var(--jp-editor-selected-background);
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/**
 * Here is our jupyter theme for CodeMirror syntax highlighting
 * This is used in our marked.js syntax highlighting and CodeMirror itself
 * The string "jupyter" is set in ../codemirror/widget.DEFAULT_CODEMIRROR_THEME
 * This came from the classic notebook, which came form highlight.js/GitHub
 */

/**
 * CodeMirror themes are handling the background/color in this way. This works
 * fine for CodeMirror editors outside the notebook, but the notebook styles
 * these things differently.
 */
.CodeMirror.cm-s-jupyter {
  background: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* In the notebook, we want this styling to be handled by its container */
.jp-CodeConsole .CodeMirror.cm-s-jupyter,
.jp-Notebook .CodeMirror.cm-s-jupyter {
  background: transparent;
}

.cm-s-jupyter .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}
.cm-s-jupyter span.cm-keyword {
  color: var(--jp-mirror-editor-keyword-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-atom {
  color: var(--jp-mirror-editor-atom-color);
}
.cm-s-jupyter span.cm-number {
  color: var(--jp-mirror-editor-number-color);
}
.cm-s-jupyter span.cm-def {
  color: var(--jp-mirror-editor-def-color);
}
.cm-s-jupyter span.cm-variable {
  color: var(--jp-mirror-editor-variable-color);
}
.cm-s-jupyter span.cm-variable-2 {
  color: var(--jp-mirror-editor-variable-2-color);
}
.cm-s-jupyter span.cm-variable-3 {
  color: var(--jp-mirror-editor-variable-3-color);
}
.cm-s-jupyter span.cm-punctuation {
  color: var(--jp-mirror-editor-punctuation-color);
}
.cm-s-jupyter span.cm-property {
  color: var(--jp-mirror-editor-property-color);
}
.cm-s-jupyter span.cm-operator {
  color: var(--jp-mirror-editor-operator-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-comment {
  color: var(--jp-mirror-editor-comment-color);
  font-style: italic;
}
.cm-s-jupyter span.cm-string {
  color: var(--jp-mirror-editor-string-color);
}
.cm-s-jupyter span.cm-string-2 {
  color: var(--jp-mirror-editor-string-2-color);
}
.cm-s-jupyter span.cm-meta {
  color: var(--jp-mirror-editor-meta-color);
}
.cm-s-jupyter span.cm-qualifier {
  color: var(--jp-mirror-editor-qualifier-color);
}
.cm-s-jupyter span.cm-builtin {
  color: var(--jp-mirror-editor-builtin-color);
}
.cm-s-jupyter span.cm-bracket {
  color: var(--jp-mirror-editor-bracket-color);
}
.cm-s-jupyter span.cm-tag {
  color: var(--jp-mirror-editor-tag-color);
}
.cm-s-jupyter span.cm-attribute {
  color: var(--jp-mirror-editor-attribute-color);
}
.cm-s-jupyter span.cm-header {
  color: var(--jp-mirror-editor-header-color);
}
.cm-s-jupyter span.cm-quote {
  color: var(--jp-mirror-editor-quote-color);
}
.cm-s-jupyter span.cm-link {
  color: var(--jp-mirror-editor-link-color);
}
.cm-s-jupyter span.cm-error {
  color: var(--jp-mirror-editor-error-color);
}
.cm-s-jupyter span.cm-hr {
  color: #999;
}

.cm-s-jupyter span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}

.cm-s-jupyter .CodeMirror-activeline-background,
.cm-s-jupyter .CodeMirror-gutter {
  background-color: var(--jp-layout-color2);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0px;
  padding: 0px;
  line-height: normal;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}
.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}
.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
}
.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
}
.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}
.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}
.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0em;
}

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: 12px;
  table-layout: fixed;
  margin-left: auto;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon table {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0px;
}

.jp-RenderedHTMLCommon p {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}
/* ...or leave it untouched if they don't */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-dark-background {
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-light-background {
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}
.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}
.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}
.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}
.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}
.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}
.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}
.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}
.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: 0.8em;
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser {
  display: flex;
  flex-direction: column;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  border-bottom: none;
  height: auto;
  margin: var(--jp-toolbar-header-margin);
  box-shadow: none;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 4px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0px 2px;
  padding: 0px 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0px;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar.jp-Toolbar {
  padding: 0px;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  justify-content: space-evenly;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-Toolbar-item {
  flex: 1;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-ToolbarButtonComponent {
  width: 100%;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px 12px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: white;
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon:before {
  color: limegreen;
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0px;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-DirListing-deadSpace {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

.jp-FileDialog.jp-mod-conflict input {
  color: red;
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
}

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: flex;
  flex-direction: row;
}

.jp-OutputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-output {
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea-child .jp-OutputArea-output {
  flex-grow: 1;
  flex-shrink: 1;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0px;
  padding: 0px;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0px;
  flex: 1 1 auto;
}

.jp-OutputArea-executeResult.jp-RenderedText {
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-OutputArea-stdin {
  line-height: var(--jp-code-line-height);
  padding-top: var(--jp-code-padding);
  display: flex;
}

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;
  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0px;
  bottom: 0px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0px;
  width: 100%;
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: flex;
  flex-direction: row;
}

.jp-InputArea-editor {
  flex: 1 1 auto;
}

.jp-InputArea-editor {
  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0px;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: flex;
  flex-direction: row;
  flex: 1 1 auto;
}

.jp-Placeholder-prompt {
  box-sizing: border-box;
}

.jp-Placeholder-content {
  flex: 1 1 auto;
  border: none;
  background: transparent;
  height: 20px;
  box-sizing: border-box;
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0px;
  margin: 0px;
  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 200px;
  box-shadow: inset 0 0 6px 2px rgba(0, 0, 0, 0.3);
  margin-left: var(--jp-private-cell-scrolling-output-offset);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  flex: 0 0
    calc(
      var(--jp-cell-prompt-width) -
        var(--jp-private-cell-scrolling-output-offset)
    );
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  flex: 1 1 auto;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: 2px;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: flex;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0px;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-NotebookTools-tool {
  padding: 0px 12px 0 12px;
}

.jp-ActiveCellTool {
  padding: 12px;
  background-color: var(--jp-layout-color1);
  border-top: none !important;
}

.jp-ActiveCellTool .jp-InputArea-prompt {
  flex: 0 0 auto;
  padding-left: 0px;
}

.jp-ActiveCellTool .jp-InputArea-editor {
  flex: 1 1 auto;
  background: var(--jp-cell-editor-background);
  border-color: var(--jp-cell-editor-border-color);
}

.jp-ActiveCellTool .jp-InputArea-editor .CodeMirror {
  background: transparent;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0px 12px 0px;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label {
  line-height: 1.4;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>.tag {
  height: 32px;
  width: fit-content;
  border-radius: 35px;
  margin-right: 5px;
  margin-bottom: 10px;
  padding: 12px;
  font-size: var(--jp-ui-font-size-1);
  display: inline-flex;
  justify-content: center;
  align-items: center;
  max-width: calc(100% - 25px);
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.unapplied-tag {
  background-color: var(--jp-layout-color1);
  border: 1px solid var(--jp-ui-font-color2);
  color: var(--jp-ui-font-color2);
}

.applied-tag {
  background-color: var(--jp-layout-color2);
  border: 1px solid var(--jp-ui-font-color1);
  color: var(--jp-ui-font-color1);
}

.add-tag {
  white-space: nowrap;
  overflow: hidden;
  border: none;
  outline: none;
  resize: horizontal;
  font-size: var(--jp-ui-font-size-1);
  color: var(--jp-ui-font-color2);
  background-color: var(--jp-layout-color1);
}

.tag-holder {
  display: flex;
  justify-content: center;
  align-items: center;
}

.tag-hover {
  background-color: var(--jp-layout-color2);
}

.tag-header {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  flex: 0 0 auto;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0px;
  padding: 8px 12px;
  text-transform: uppercase;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-completer-item-height: 24px;
  /* Shift the baseline of the type character to align with the match text */
  --jp-private-completer-type-offset: 2px;
}

.jp-Completer {
  box-shadow: var(--jp-elevation-z6);
  background: var(--jp-layout-color1);
  color: var(--jp-content-font-color1);
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding: 0;
  display: flex;
  flex-direction: row;
  /* Position the completer relative to the text editor, align the '.' */
  margin: 4px 0 0 -30px;
  z-index: 10001;
}

.jp-Completer-docpanel {
  border-left: var(--jp-border-width) solid var(--jp-border-color1);
  width: 300px;
  overflow: scroll;
  padding: 8px;
  max-height: calc((10 * var(--jp-private-completer-item-height)) - 16px);
}

.jp-Completer-docpanel pre {
  border: none;
  margin: 0px;
  padding: 0px;
  white-space: pre-wrap;
}

.jp-Completer-list {
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow-y: scroll;
  overflow-x: auto;
  max-height: calc((10 * var(--jp-private-completer-item-height)));
  min-height: calc(var(--jp-private-completer-item-height));
}

.jp-Completer-item {
  display: table-row;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  height: var(--jp-private-completer-item-height);
  min-width: 150px;
}

.jp-Completer-item .jp-Completer-match {
  display: table-cell;
  box-sizing: border-box;
  margin: 0;
  padding: 0 8px 0 6px;
  height: var(--jp-private-completer-item-height);
  font-family: var(--jp-code-font-family);
  font-size: var(--jp-code-font-size);
  line-height: var(--jp-private-completer-item-height);
  vertical-align: middle;
}

.jp-Completer-deprecated .jp-Completer-match {
  text-decoration: line-through;
  color: var(--jp-content-font-color2);
}

.jp-Completer-item .jp-Completer-type {
  display: table-cell;
  box-sizing: border-box;
  height: var(--jp-private-completer-item-height);
  background: transparent;
  width: var(--jp-private-completer-item-height);
}

.jp-Completer-item .jp-Completer-icon {
  vertical-align: middle;
  /* Normal element size from LabIconStyle.ISheetOptions */
  height: 16px;
  width: 16px;
}

.jp-Completer-item .jp-Completer-monogram {
  text-align: center;
  color: white;
  width: var(--jp-private-completer-item-height);
  min-width: var(--jp-private-completer-item-height);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: calc(
    var(--jp-private-completer-item-height) -
      var(--jp-private-completer-type-offset)
  );
  padding-bottom: var(--jp-private-completer-type-offset);
}

.jp-Completer-item .jp-Completer-typeExtended {
  display: table-cell;
  box-sizing: border-box;
  height: var(--jp-private-completer-item-height);
  text-align: right;
  background: transparent;
  color: var(--jp-ui-font-color2);
  font-family: var(--jp-code-font-family);
  font-size: var(--jp-code-font-size);
  line-height: var(--jp-private-completer-item-height);
  padding-right: 8px;
  vertical-align: middle;
}

.jp-Completer-item:hover {
  background: var(--jp-layout-color2);
  opacity: 0.8;
}

.jp-Completer-item.jp-mod-active {
  background: var(--jp-brand-color1);
  color: white;
}

.jp-Completer-item .jp-Completer-match mark {
  font-weight: bold;
  background: inherit;
  color: inherit;
}

.jp-Completer-type[data-color-index='0'] {
  background: transparent;
}

.jp-Completer-type[data-color-index='1'] {
  background: #1f77b4;
}

.jp-Completer-type[data-color-index='2'] {
  background: #ff7f0e;
}

.jp-Completer-type[data-color-index='3'] {
  background: #2ca02c;
}

.jp-Completer-type[data-color-index='4'] {
  background: #d62728;
}

.jp-Completer-type[data-color-index='5'] {
  background: #9467bd;
}

.jp-Completer-type[data-color-index='6'] {
  background: #8c564b;
}

.jp-Completer-type[data-color-index='7'] {
  background: #e377c2;
}

.jp-Completer-type[data-color-index='8'] {
  background: #7f7f7f;
}

.jp-Completer-type[data-color-index='9'] {
  background: #bcbd22;
}

.jp-Completer-type[data-color-index='10'] {
  background: #17becf;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-ConsolePanel {
  display: flex;
  flex: 1 1 auto;
  flex-direction: column;
  margin-top: -1px;
  min-width: 240px;
  min-height: 120px;
}

.jp-ConsolePanel::before {
  content: '';
  display: block;
  height: var(--jp-toolbar-micro-height);
  background: var(--jp-toolbar-background);
  border-bottom: 1px solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 1;
}

.jp-CodeConsole {
  height: 100%;
  padding: 0;
  display: flex;
  flex-direction: column;
}

.jp-CodeConsole .jp-Cell {
  padding: var(--jp-cell-padding);
}

/*-----------------------------------------------------------------------------
| Content (already run cells)
|----------------------------------------------------------------------------*/

.jp-CodeConsole-content {
  background: var(--jp-layout-color0);
  flex: 1 1 auto;
  overflow: auto;
  padding: var(--jp-console-padding);
}

.jp-CodeConsole-content .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-inprompt-font-color);
  cursor: move;
}

.jp-CodeConsole-content .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-outprompt-font-color);
}

/* This rule is for styling cell run by another activity in this console */
.jp-CodeConsole-content .jp-Cell.jp-CodeConsole-foreignCell {
}

.jp-CodeConsole-content .jp-InputArea-editor.jp-InputArea-editor {
  background: transparent;
  border: 1px solid transparent;
}

.jp-CodeConsole-content .jp-CodeConsole-banner .jp-InputPrompt {
  display: none;
}

/* collapser is hovered */
.jp-CodeConsole-content .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/*-----------------------------------------------------------------------------
| Input/prompt cell
|----------------------------------------------------------------------------*/

.jp-CodeConsole-input {
  max-height: 80%;
  flex: 0 0 auto;
  overflow: auto;
  border-top: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  padding: var(--jp-cell-padding) var(--jp-console-padding);
  /* This matches the box shadow on the notebook toolbar, eventually we should create
   * CSS variables for this */
  box-shadow: 0px 0.4px 6px 0px rgba(0, 0, 0, 0.1);
  background: var(--jp-layout-color1);
}

.jp-CodeConsole-input .jp-CodeConsole-prompt .jp-InputArea {
  height: 100%;
  min-height: 100%;
}

.jp-CodeConsole-promptCell .jp-InputArea-editor.jp-mod-focused {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-CodeConsole {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-CodeConsole .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-CodeConsole .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-CSVViewer {
  display: flex;
  flex-direction: column;
  outline: none;
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-CSVDelimiter {
  display: flex;
  flex: 0 0 auto;
  flex-direction: row;
  border: none;
  min-height: 24px;
  background: var(--jp-toolbar-background);
  z-index: 1;
}

.jp-CSVDelimiter .jp-CSVDelimiter-label {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  padding-left: 8px;
  padding-right: 8px;
}

.jp-CSVDelimiter .jp-CSVDelimiter-dropdown {
  flex: 0 0 auto;
  vertical-align: middle;
  border-radius: 0;
  outline: none;
  height: 20px;
  margin-top: 2px;
  margin-bottom: 2px;
}

.jp-CSVDelimiter .jp-CSVDelimiter-dropdown select.jp-mod-styled {
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
  height: 20px;
  padding-right: 20px;
}

.jp-CSVViewer-grid {
  flex: 1 1 auto;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-overlay * {
  color: var(--jp-ui-font-color0);
  background-position: center;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-focused-input {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-input-wrapper * {
  background-color: var(--jp-layout-color0);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
  background-repeat: no-repeat;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: 20px;
  height: 20px;
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button:before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 43px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: 20px;
  height: 20px;
  background-repeat: no-repeat;
  background-position: center;
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-ellipses-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-ellipses-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-ellipses-button-enabled {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-ellipses-button-enabled:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 200px;
  display: block;
}
.jp-DocumentSearch-search-options-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-options input {
  float: right;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-entry {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  font-size: var(--jp-ui-font-size1);
  width: 186px;
  margin: 2px;
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: 2px;
}

.jp-DocumentSearch-replace-entry:focus,
.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-font-color1);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*
  Main widget layout and styling
*/

.jp-extensionmanager-view {
  padding-bottom: 0px;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  display: flex;
  flex-direction: column;
  font-size: var(--jp-ui-font-size1);
}

.jp-extensionmanager-content {
  overflow: auto;
  overflow-x: hidden;
}

/*
  Jupyter Org
*/

.jp-extensionmanager-is-jupyter-org {
  font-size: var(--jp-ui-font-size0);
  color: var(--jp-ui-font-color2);
}

/*
  List view layout and styling
*/

.jp-extensionmanager-listview-wrapper {
  margin: 0;
  padding: 0;
  padding-bottom: 8px;
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
}

.jp-extensionmanager-listview {
  list-style-type: none;
  margin: 0;
  padding: 0;
  min-height: 0;
}

/*
  Section headers
*/

.jp-extensionmanager-view header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  margin: 0px;
  padding-bottom: 8px;
  font-weight: 600;
  text-transform: uppercase;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  letter-spacing: 1px;
  font-size: var(--jp-ui-font-size0);
  line-height: 24px;
  height: 24px;
  padding: 4px;
}

.jp-extensionmanager-view header > .jp-ToolbarButtonComponent {
  padding: 0px 2px;
}

.jp-extensionmanager-view header .jp-extensionmanager-headerText {
  flex: 1 0 auto;
  margin: 0px 4px;
}

.jp-extensionmanager-view header .jp-extensionmanager-headerTextDisabled {
  flex: 1 0 auto;
  margin: 0px 4px;
  color: var(--jp-layout-color3);
}

.jp-extensionmanager-view header > .jp-ToolbarButtonComponent {
  border: 1px solid transparent;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
}

.jp-extensionmanager-view header > .jp-ToolbarButtonComponent:hover {
  /* border: 1px solid var(--jp-brand-color1); */
}

/*
  Listing messages
*/
.jp-extensionmanager-listingmessage {
  background-color: var(--jp-brand-color1);
  color: var(--jp-ui-inverse-font-color1);
  padding: 4px 8px;
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
}

/*
  Error messages
*/
.jp-extensionmanager-view .jp-extensionmanager-error pre {
  white-space: pre-wrap;
}

/*
  Search bar layout and styling
*/

.jp-extensionmanager-search-bar {
  padding: 4px;
}

.jp-extensionmanager-disclaimer {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: normal;
  margin: 8px 8px 8px 32px;
}

.jp-extensionmanager-search-wrapper input {
  background: transparent;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
  box-sizing: border-box;
  border-radius: 0;
}

.jp-extensionmanager-search-wrapper input:focus {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

/*
  List view pagination styling
*/

.jp-extensionmanager-view ul.pagination {
  display: inline-block;
  padding-left: 0px;
  padding-right: 0px;
}

.jp-extensionmanager-view .pagination li {
  display: inline-block;
}

.jp-extensionmanager-view .pagination li a {
  padding: 0 5px;
  margin: 0 5px;
}

.jp-extensionmanager-view .pagination li.active a {
  background: var(--jp-brand-color1);
  color: #fff;
}

.jp-extensionmanager-view .pagination li a:hover {
  background-color: var(--jp-layout-color2);
  color: unset;
}

.jp-extensionmanager-view .pagination .break a {
  cursor: default;
}

.jp-extensionmanager-pagination {
  display: flex;
  justify-content: center;
}
/*
  Entry layout and styling
*/

.jp-extensionmanager-entry {
  padding: 8px;
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
}

.jp-extensionmanager-entry-description {
  min-width: 0;
  flex-grow: 1;
}

.jp-extensionmanager-entry-title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.jp-extensionmanager-entry.jp-extensionmanager-entry-should-be-uninstalled {
  background-color: var(--jp-error-color3);
}

/* Precedence order update/error/warning matters! */
.jp-extensionmanager-entry.jp-extensionmanager-entry-update {
  border-left: solid 8px var(--jp-brand-color2);
  padding-left: 4px;
}

.jp-extensionmanager-entry.jp-extensionmanager-entry-error {
  border-left: solid 8px var(--jp-error-color2);
  padding-left: 4px;
}

.jp-extensionmanager-entry.jp-extensionmanager-entry-warning {
}

.jp-extensionmanager-entry-name {
  font-size: var(--jp-ui-font-size1);
  font-weight: 600;
  padding: 0 8px 0 0;
  margin-bottom: 4px;
  overflow-wrap: anywhere;
}

.jp-extensionmanager-entry-name a:link {
  color: var(--jp-content-link-color);
  text-decoration: none;
}

.jp-extensionmanager-entry-name a:visited {
  color: var(--jp-content-link-color);
  text-decoration: none;
}

.jp-extensionmanager-entry-name a:hover {
  color: var(--jp-content-link-color);
  text-decoration: underline;
}

.jp-extensionmanager-entry-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
  font-weight: 400;
}

.jp-extensionmanager-loader,
.jp-extensionmanager-error,
.jp-extensionmanager-listview-message {
  padding: 4px 12px;
}

.jp-extensionmanager-listview-message {
  font-size: var(--jp-ui-font-size1);
}

.jp-extensionmanager-entry-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/*
  Pending entry progress indicator
*/

.jp-extensionmanager-pending {
  height: 4px;
  width: 100%;
  position: relative;
  overflow: hidden;
  flex: 0 0 auto;
  background-color: var(--jp-layout-color1);
}

.jp-extensionmanager-pending.jp-mod-hasPending:before {
  display: block;
  position: absolute;
  content: '';
  left: -200px;
  width: 200px;
  height: 4px;
  border-radius: 4px;
  background-color: var(--jp-brand-color1);
  animation: loading 2s linear infinite;
}

@keyframes loading {
  from {
    left: -200px;
    width: 30%;
  }
  50% {
    width: 30%;
  }
  70% {
    width: 70%;
  }
  80% {
    left: 50%;
  }
  95% {
    left: 120%;
  }
  to {
    left: 100%;
  }
}

/*
  Disclaimer buttons
*/

.jp-extensionmanager-disclaimer-disable {
  background-color: var(--jp-brand-color1) !important;
  color: white !important;
  border: 0;
  background-image: none !important;
}

.jp-extensionmanager-disclaimer-enable {
  background-color: var(--jp-error-color1) !important;
  color: white !important;
  border: 0;
  background-image: none !important;
}

/*
  Entry buttons layout and styling
*/

.jp-extensionmanager-entry-buttons {
  display: flex;
  flex-direction: row;
  padding-top: 4px;
}

/*
  Rebuild prompt dialog
*/

.jp-extensionmanager-buildprompt {
  background-color: var(--jp-brand-color1);
  color: var(--jp-ui-inverse-font-color1);
  padding: 4px 8px;
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
}

.jp-extensionmanager-buildprompt button {
  border: none;
  background-color: transparent;
  color: var(--jp-ui-inverse-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 600;
  float: right;
  margin: 4px;
}

/*
  Companion packages dialog
*/

input[type='checkbox'] {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

/*
  Generic dialog
*/
.jp-extensionmanager-dialog .jp-extensionmanager-dialog-subheader {
  font-size: var(--jp-ui-font-size1);
  font-weight: 600;
  color: var(--jp-ui-font-color0);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

#filebrowser.jp-mod-restoring .jp-DirListing-content {
  display: none;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileEditor {
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-FileEditor {
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-inspector-tab-height: 24px;
  --jp-private-inspector-tab-width: 60px;
}

/*-----------------------------------------------------------------------------
| Inspector
|----------------------------------------------------------------------------*/

.jp-Inspector {
  outline: none;
  min-width: 120px;
  min-height: 120px;
}

.jp-Inspector-content {
  background: var(--jp-layout-color1);
  border: none;
}

.jp-Inspector-content {
  padding: 8px;
  width: 100%;
  height: 100%;
  overflow: auto;
}

.jp-Inspector-content pre {
  font-size: var(--jp-code-font-size);
  line-height: var(--jp-code-line-height);
  margin: 0;
  white-space: pre-wrap;
}

.jp-Inspector-default-content {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: xx-large;
  font-style: italic;
  color: darkgray;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Help {
  min-width: 240px;
  min-height: 240px;
  background: white;
  outline: none;
}

.jp-Help > iframe {
  border: none;
}

.jp-About-body {
  display: flex;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  text-align: left;
  flex-direction: column;
  width: 100%;
  min-width: 360px;
  overflow: visible;
}

.jp-About-version-info {
  color: var(--jp-ui-font-color1);
  /* Dialog-header sets the font size to 3, we reset to 1 */
  font-size: var(--jp-ui-font-size1);
  width: 200px;
  font-weight: 400;
  letter-spacing: 0.4px;
  text-align: left;
  line-height: 1.12;
}

.jp-Dialog
  .jp-Dialog-content
  .jp-Dialog-footer
  .jp-Dialog-button.jp-About-button {
  margin-right: 0px;
}

.jp-About-version {
  display: block;
}

.jp-About-version {
  padding-top: 8px;
}

.jp-About-externalLinks {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 12px;
}

.jp-About-externalLinks .jp-Button-flat {
  color: #f37726;
}

.jp-About-copyright {
  padding-top: 25px;
}

.jp-About-header {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.jp-About-body pre {
  white-space: pre-wrap;
}

.jp-About-header-info {
  display: flex;
  flex-direction: column;
  margin-left: 16px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Document styles */
.jp-HTMLViewer {
  overflow: hidden;
}

.jp-HTMLViewer {
  min-width: 100px;
  min-height: 100px;
  width: 100%;
  height: 100%;
}

.jp-HTMLViewer > iframe {
  border: none;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occuring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-HTMLViewer {
  position: relative;
}

body.lm-mod-override-cursor .jp-HTMLViewer:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-ImageViewer {
  overflow: auto;
}

.jp-ImageViewer > img {
  box-sizing: border-box;
  transform-origin: top left;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/* Copyright (c) Jupyter Development Team.
Distributed under the terms of the Modified BSD License. */

.jp-RenderedJavaScript {
  padding: var(--jp-code-padding);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/**
  Copyright (c) Jupyter Development Team.
  Distributed under the terms of the Modified BSD License.
*/

/* Base styles */
.jp-RenderedJSON {
  width: 100%;
  height: 100%;
  padding: 0;
  overflow: hidden;
}

/* Override react-json-tree inline styles */
.jp-RenderedJSON *:not(mark) {
  background-color: transparent !important;
}

.jp-RenderedJSON ul {
  margin: 0 !important;
}

.jp-RenderedJSON .container {
  position: relative;
  width: 100%;
  min-height: 30px;
}

.jp-RenderedJSON .filter {
  position: absolute;
  top: 0;
  right: 0;
  width: 33%;
  max-width: 150px;
  z-index: 10;
}

/* Document styles */
.jp-MimeDocument .jp-RenderedJSON {
  padding: 5px 5px 5px 20px;
  overflow-y: auto;
}

/* Output styles */
/* .jp-OutputArea .jp-RenderedJSON {

} */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Private CSS variables */

:root {
  --jp-private-launcher-top-padding: 16px;
  --jp-private-launcher-side-padding: 32px;
  --jp-private-launcher-card-size: 100px;
  --jp-private-launcher-card-label-height: 32px;
  --jp-private-launcher-card-icon-height: 68px;
  --jp-private-launcher-large-icon-size: 52px;
  --jp-private-launcher-small-icon-size: 32px;
}

/* Launcher */

.jp-Launcher {
  margin: 0;
  padding: 0;
  outline: none;
  background: var(--jp-layout-color0);
  box-sizing: border-box;
  min-width: 120px;
  min-height: 120px;
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-Launcher-body {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  overflow: auto;
  display: flex;
  justify-content: center;
}

.jp-Launcher-cwd h3 {
  font-size: var(--jp-ui-font-size2);
  font-weight: normal;
  color: var(--jp-ui-font-color1);
  margin: 1em 0px;
}

.jp-Launcher-content {
  width: 85%;
  height: 100%;
  padding-top: var(--jp-private-launcher-top-padding);
  padding-left: var(--jp-private-launcher-side-padding);
  padding-right: var(--jp-private-launcher-side-padding);
  box-sizing: border-box;
}

/* Launcher section */

.jp-Launcher-section {
  width: 100%;
  box-sizing: border-box;
  padding-bottom: 12px;
}

.jp-Launcher-sectionHeader {
  display: flex;
  flex-direction: row;
  align-items: center;
  box-sizing: border-box;
  /* This is custom tuned to get the section header to align with the cards */
  margin-left: 5px;
  border-bottom: 1px solid var(--jp-border-color2);
  padding-bottom: 0px;
  margin-bottom: 8px;
}

.jp-Launcher-sectionTitle {
  font-size: var(--jp-ui-font-size2);
  font-weight: normal;
  color: var(--jp-ui-font-color1);
  box-sizing: border-box;
}

/* Launcher cards */

.jp-Launcher-cardContainer {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.jp-LauncherCard {
  display: flex;
  flex-direction: column;
  cursor: pointer;
  width: var(--jp-private-launcher-card-size);
  height: var(--jp-private-launcher-card-size);
  margin: 8px;
  padding: 0px;
  border: 1px solid var(--jp-border-color2);
  background: var(--jp-layout-color0);
  box-shadow: var(--jp-elevation-z2);
  transition: 0.2s box-shadow;
  border-radius: var(--jp-border-radius);
}

.jp-LauncherCard:focus:not(:active) {
  border: 1px solid var(--jp-brand-color1);
  box-shadow: var(--jp-elevation-z6);
}

.jp-LauncherCard:hover {
  box-shadow: var(--jp-elevation-z6);
  background: var(--jp-layout-color1);
}

.jp-LauncherCard:active {
  box-shadow: var(--jp-elevation-z4);
}

.jp-LauncherCard-icon {
  width: 100%;
  height: var(--jp-private-launcher-card-icon-height);
  box-sizing: border-box;
  margin: 0px;
  padding: 0px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.jp-LauncherCard-noKernelIcon {
  font-weight: normal;
  font-size: var(--jp-private-launcher-large-icon-size);
}

.jp-LauncherCard[data-category='Notebook'] .jp-LauncherCard-noKernelIcon {
  /* This color is copied from the notebook icon. */
  color: #ef6c00;
}

.jp-LauncherCard[data-category='Console'] .jp-LauncherCard-noKernelIcon {
  /* This color is copied from the console icon. */
  color: #0288d1;
}

.jp-LauncherCard-label {
  width: 100%;
  height: var(--jp-private-launcher-card-label-height);
  padding: 0 4px 4px 4px;
  box-sizing: border-box;
  overflow: hidden;
}

.jp-LauncherCard-label p {
  height: 28px;
  word-break: break-word;
  text-align: center;
  color: var(--jp-ui-font-color1);
  line-height: 14px;
  font-size: 12px;
  overflow: hidden;
}

/* kernel icons */

.jp-Launcher-kernelIcon {
  width: var(--jp-private-launcher-large-icon-size);
  height: var(--jp-private-launcher-large-icon-size);
  margin: 0px;
  padding: 0px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-LogConsolePanel {
  overflow-y: auto;
}

.jp-LogConsolePanel .jp-OutputArea-child {
  border-bottom: 1px solid var(--jp-border-color3);
}

.jp-LogConsolePanel .jp-OutputArea-prompt {
  width: 85px;
  color: var(--jp-ui-font-color2);
  font-size: 13px;
  padding: 2px;
}

.jp-LogConsolePanel .jp-OutputArea-prompt[data-log-level='info'] {
  background-color: var(--jp-info-color1);
  color: var(--jp-ui-inverse-font-color1);
}

.jp-LogConsolePanel .jp-OutputArea-prompt[data-log-level='warning'] {
  background-color: var(--jp-warn-color1);
  color: var(--jp-ui-inverse-font-color1);
}

.jp-LogConsolePanel .jp-OutputArea-prompt[data-log-level='error'] {
  background-color: var(--jp-error-color1);
  color: var(--jp-ui-inverse-font-color1);
}

.jp-LogConsolePanel .jp-OutputArea-prompt[data-log-level='critical'] {
  background-color: var(--jp-error-color0);
  color: var(--jp-ui-inverse-font-color0);
}

.jp-LogConsoleListPlaceholder {
  padding: 5px;
  font-size: 13px;
  color: var(--jp-ui-font-color3);
}

.jp-Scrolling {
  overflow-y: auto;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

@keyframes flash {
  0% {
    background-color: var(--jp-brand-color1);
  }
  50% {
    color: unset;
    background-color: unset;
  }
  100% {
    background-color: var(--jp-brand-color1);
  }
}

.jp-LogConsoleStatusItem.jp-LogConsole-flash {
  animation: flash 300ms both;
}

.jp-LogConsoleStatusItem.jp-mod-selected {
  background-color: var(--jp-brand-color1);
}

/* Need to be very specific to override the typestyle styles on status bar components */
.jp-LogConsoleStatusItem.jp-mod-selected,
.jp-LogConsoleStatusItem.jp-mod-selected div,
.jp-LogConsoleStatusItem.jp-mod-selected div span {
  color: white;
}

.jp-LogConsole .jp-ClearIcon {
  transform: rotate(90deg);
  margin-top: -1px;
  padding: 0px 8px;
}

.jp-Toolbar-item.jp-LogConsole-toolbarLogLevel {
  align-items: center;
  padding: 0px 6px;
}

/* Matches the disabled style elsewhere in JupyterLab */
.jp-LogConsole-toolbarLogLevel-disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

/* Copied from the notebook cell type dropdown styling */
.jp-LogConsole-toolbarLogLevelDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

/* Copied from the notebook cell type dropdown styling */
.jp-LogConsole-toolbarLogLevelDropdown span {
  top: 5px !important;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-markdownviewer-padding: 32px;
}

.jp-Document .jp-MarkdownViewer .jp-RenderedMarkdown {
  padding-top: var(--jp-private-markdownviewer-padding);
  padding-right: var(--jp-private-markdownviewer-padding);
  padding-bottom: var(--jp-private-markdownviewer-padding);
  padding-left: var(--jp-private-markdownviewer-padding);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-MarkdownViewer .jp-RenderedHTMLCommon {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Left-justify the MathJax preview in cell outputs. */
.jp-OutputArea-output.jp-RenderedLatex .MathJax_Preview .MJXp-display {
  padding: var(--jp-code-padding);
  text-align: left !important;
}

/* Left-justify the MathJax display equation in cell outputs. */
.jp-OutputArea-output.jp-RenderedLatex .MathJax_Display {
  text-align: left !important;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-PDFContainer iframe {
  position: absolute;
  z-index: 0;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
}

.jp-OutputArea .jp-PDFContainer {
  min-height: 512px;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
This reuses the same CSS selector logic as jp-IFrame to prevent embedded
PDFs from swallowing cursor events.
*/
body.lm-mod-override-cursor .jp-PDFContainer {
  position: relative;
}

body.lm-mod-override-cursor .jp-PDFContainer:before {
  content: '';
  position: absolute;
  z-index: 10;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-running-button-height: 28px;
  --jp-private-running-button-width: 48px;
  --jp-private-running-item-height: 24px;
  --jp-private-running-shutdown-button-height: 24px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-RunningSessions {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-RunningSessions-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}

.jp-RunningSessions-section {
  display: flex;
  flex: 0 1 auto;
  flex-direction: column;
  overflow: auto;
}

.jp-RunningSessions-sectionHeader {
  flex: 0 0 auto;
  align-items: center;
  justify-content: space-between;
  height: 28px;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  margin-top: 8px;
}

.jp-RunningSessions-sectionHeader h2 {
  flex: 0 0 auto;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: var(--jp-ui-font-size0);
  padding: 8px 8px 8px 12px;
  margin: 0px;
}

.jp-RunningSessions-sectionHeader .jp-ToolbarButtonComponent {
  flex: 0 0 auto;
}

.jp-RunningSessions-sectionContainer {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  overflow: auto;
}

.jp-RunningSessions-sectionList {
  margin: 0;
  padding: 0;
  list-style-type: none;
}

.jp-RunningSessions-item {
  display: flex;
  flex-direction: row;
  color: var(--jp-ui-font-color1);
  height: var(--jp-private-running-item-height);
  line-height: var(--jp-private-running-item-height);
}

.jp-RunningSessions-itemLabel {
  font-size: var(--jp-ui-font-size1);
  flex: 1 1 auto;
  margin-right: 4px;
  padding-left: 4px;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
  transition: background-color 0.1s ease;
}

.jp-RunningSessions-itemLabel:hover {
  background-color: var(--jp-layout-color2);
}

.jp-RunningSessions-itemLabel:focus {
  background-color: rgba(153, 153, 153, 0.2);
}

.jp-RunningSessions-itemShutdown.jp-mod-styled {
  margin: 0px 4px;
  color: var(--jp-warn-color1);
  font-weight: 500;
  background-color: transparent;
  height: var(--jp-private-running-shutdown-button-height);
  line-height: var(--jp-private-running-shutdown-button-height);
  transition: background-color 0.1s ease;
  border-radius: 2px;
}

.jp-RunningSessions-itemShutdown.jp-mod-styled:hover {
  background-color: rgba(153, 153, 153, 0.1);
}

.jp-RunningSessions-itemShutdown.jp-mod-styled:focus {
  border: none;
  box-shadow: none;
  background-color: rgba(153, 153, 153, 0.2);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-settingeditor-debug-height: 28px;
  --jp-private-settingeditor-key-width: 150px;
  --jp-private-settingeditor-legend-height: 16px;
  --jp-private-settingeditor-row-height: 16px;
  --jp-private-settingeditor-toolbar-height: 28px;
  --jp-private-settingeditor-type-width: 75px;
}

#setting-editor {
  min-width: 360px;
  min-height: 240px;
  background-color: var(--jp-layout-color0);
  margin-top: -1px;
  outline: none;
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

#setting-editor > .lm-Widget {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

#setting-editor .lm-SplitPanel-handle {
  background-color: var(--jp-border-color2);
}

#setting-editor .jp-SettingEditorInstructions {
  text-align: center;
}

#setting-editor .jp-SettingEditorInstructions-icon {
  display: inline-block;
  height: 78px;
  margin: 2px 5px 2px 8px;
  width: 60px;
}

#setting-editor .jp-SettingEditorInstructions-title {
  color: var(--jp-ui-font-color0);
  font-size: 32px;
  font-weight: 200;
  line-height: 78px;
  vertical-align: top;
}

#setting-editor .jp-SettingEditorInstructions-text {
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size2);
}

#setting-editor .jp-PluginList {
  min-width: 175px;
  max-width: 275px;
}

#setting-editor .jp-PluginList ul {
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow-y: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

#setting-editor .jp-PluginList li {
  display: flex;
  flex-direction: row;
  border: 1px solid transparent;
  overflow: hidden;
  padding: 4px 0 4px 4px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

#setting-editor .jp-PluginList li:hover {
  background-color: var(--jp-layout-color2);
  border: 1px solid var(--jp-border-color2);
}

#setting-editor .jp-PluginList li.jp-mod-selected {
  background-color: var(--jp-brand-color1);
  color: white;
  border: 1px solid var(--jp-brand-color1);
}

#setting-editor
  ul.jp-PluginList
  li.jp-mod-selected
  span.jp-PluginList-icon.jp-FileIcon {
  background-image: var(--jp-icon-file-selected);
}

#setting-editor .jp-PluginList-icon {
  display: inline-block;
  height: 20px;
  width: 20px;
  margin-right: 3px;
  position: relative;
}

#setting-editor .jp-SettingsRawEditor .jp-Toolbar {
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  height: var(--jp-private-settingeditor-toolbar-height);
  max-height: var(--jp-private-settingeditor-toolbar-height);
}

#setting-editor
  .jp-SettingsRawEditor
  .jp-Toolbar
  .jp-ToolbarButtonComponent-label {
  display: none;
}

#setting-editor .jp-SettingsRawEditor .jp-Toolbar-item {
  margin-top: 1px;
  align-items: center;
}

.jp-ToolbarButtonComponent-label
  #setting-editor
  .jp-SettingsRawEditor.jp-mod-error
  .jp-Toolbar-item.jp-BugIcon::after {
  color: red;
  content: '\25CF'; /* Unicode circle character (error dot) */
  font-size: 7px;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 4px;
  left: 6px;
}

#setting-editor .jp-SettingsRawEditor .jp-Inspector {
  border-top: 2px solid var(--jp-layout-color2);
  min-height: var(--jp-private-settingeditor-debug-height);
  max-height: var(--jp-private-settingeditor-debug-height);
}

#setting-editor
  .jp-SettingsRawEditor
  .jp-Inspector.jp-SettingsDebug
  .jp-RenderedHTMLCommon {
  padding: 2px 5px 2px 0;
  width: 100%;
}

#setting-editor
  .jp-SettingsRawEditor
  .jp-Inspector.jp-SettingsDebug
  .jp-RenderedHTMLCommon
  p {
  text-align: right;
}

#setting-editor .jp-SettingsTableEditor {
  border: 1px solid var(--jp-brand-color1);
  margin: 0;
  padding: 0;
}

#setting-editor .jp-SettingsTableEditor legend {
  color: var(--jp-brand-color1);
  font-size: 70%;
  font-weight: bold;
  margin-left: 15px;
  height: var(--jp-private-settingeditor-legend-height);
}

#setting-editor .jp-SettingsTableEditor-wrapper {
  position: absolute;
  top: var(--jp-private-settingeditor-legend-height);
  bottom: 0;
  overflow-y: auto;
}

#setting-editor .jp-SettingsTableEditor table {
  table-layout: fixed;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  padding: 2px;
  width: calc(100% - 4px);
  overflow: hidden;
}

#setting-editor .jp-SettingsTableEditor tr {
  color: var(--jp-ui-font-color2);
  height: var(--jp-private-settingeditor-row-height);
  overflow: hidden;
}

#setting-editor .jp-SettingsTableEditor th {
  background-color: var(--jp-layout-color3);
  border: 1px solid transparent;
  font-weight: bold;
  height: var(--jp-private-settingeditor-row-height);
}

#setting-editor .jp-SettingsTableEditor td {
  border: 1px solid transparent;
  height: var(--jp-private-settingeditor-row-height);
}

#setting-editor .jp-SettingsTableEditor th.jp-SettingsTableEditor-key {
  width: var(--jp-private-settingeditor-key-width);
}

#setting-editor .jp-SettingsTableEditor th.jp-SettingsTableEditor-type {
  width: var(--jp-private-settingeditor-type-width);
}

#setting-editor .jp-SettingsTableEditor td.jp-SettingsTableEditor-key {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

#setting-editor .jp-SettingsTableEditor td.jp-SettingsTableEditor-value {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

#setting-editor .jp-SettingsTableEditor td.jp-SettingsTableEditor-type {
  text-align: right;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-tab-manager-active-top-border: 2px;
  --jp-private-tab-manager-tab-height: 24px;
  --jp-private-tab-manager-tab-padding-top: 8px;
}

/*-----------------------------------------------------------------------------
| Tabs in the dock panel
|----------------------------------------------------------------------------*/

#tab-manager {
  background: var(--jp-layout-color1);
  overflow: visible;
  color: var(--jp-ui-font-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

#tab-manager header {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  flex: 0 0 auto;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0px;
  padding: 8px 12px;
  text-transform: uppercase;
}

#tab-manager .lm-TabBar-tab {
  height: var(--jp-private-tab-manager-tab-height);
  padding: 0px 12px;
  border: none;
  position: relative;
  overflow: visible;
}

#tab-manager .lm-TabBar-tab:hover:not(.jp-mod-active) {
  background: var(--jp-layout-color2);
}

#tab-manager .lm-TabBar-tab:first-child {
  margin-left: 0;
}

#tab-manager .lm-TabBar-tab.jp-mod-active {
  color: white;
  background: var(--jp-brand-color1);
}

#tab-manager .lm-TabBar-tabLabel {
  line-height: var(--jp-private-tab-manager-tab-height);
  padding-left: 4px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/**
 * Copyright (c) 2014 The xterm.js authors. All rights reserved.
 * Copyright (c) 2012-2013, Christopher Jeffrey (MIT License)
 * https://github.com/chjj/term.js
 * @license MIT
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * Originally forked from (with the author's permission):
 *   Fabrice Bellard's javascript vt100 for jslinux:
 *   http://bellard.org/jslinux/
 *   Copyright (c) 2011 Fabrice Bellard
 *   The original design remains. The terminal itself
 *   has been extended to include xterm CSI codes, among
 *   other features.
 */

/**
 *  Default styles for xterm.js
 */

.xterm {
    font-feature-settings: "liga" 0;
    position: relative;
    user-select: none;
    -ms-user-select: none;
    -webkit-user-select: none;
}

.xterm.focus,
.xterm:focus {
    outline: none;
}

.xterm .xterm-helpers {
    position: absolute;
    top: 0;
    /**
     * The z-index of the helpers must be higher than the canvases in order for
     * IMEs to appear on top.
     */
    z-index: 5;
}

.xterm .xterm-helper-textarea {
    /*
     * HACK: to fix IE's blinking cursor
     * Move textarea out of the screen to the far left, so that the cursor is not visible.
     */
    position: absolute;
    opacity: 0;
    left: -9999em;
    top: 0;
    width: 0;
    height: 0;
    z-index: -5;
    /** Prevent wrapping so the IME appears against the textarea at the correct position */
    white-space: nowrap;
    overflow: hidden;
    resize: none;
}

.xterm .composition-view {
    /* TODO: Composition position got messed up somewhere */
    background: #000;
    color: #FFF;
    display: none;
    position: absolute;
    white-space: nowrap;
    z-index: 1;
}

.xterm .composition-view.active {
    display: block;
}

.xterm .xterm-viewport {
    /* On OS X this is required in order for the scroll bar to appear fully opaque */
    background-color: #000;
    overflow-y: scroll;
    cursor: default;
    position: absolute;
    right: 0;
    left: 0;
    top: 0;
    bottom: 0;
}

.xterm .xterm-screen {
    position: relative;
}

.xterm .xterm-screen canvas {
    position: absolute;
    left: 0;
    top: 0;
}

.xterm .xterm-scroll-area {
    visibility: hidden;
}

.xterm-char-measure-element {
    display: inline-block;
    visibility: hidden;
    position: absolute;
    top: 0;
    left: -9999em;
    line-height: normal;
}

.xterm {
    cursor: text;
}

.xterm.enable-mouse-events {
    /* When mouse events are enabled (eg. tmux), revert to the standard pointer cursor */
    cursor: default;
}

.xterm.xterm-cursor-pointer {
    cursor: pointer;
}

.xterm.column-select.focus {
    /* Column selection mode */
    cursor: crosshair;
}

.xterm .xterm-accessibility,
.xterm .xterm-message {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    z-index: 10;
    color: transparent;
}

.xterm .live-region {
    position: absolute;
    left: -9999px;
    width: 1px;
    height: 1px;
    overflow: hidden;
}

.xterm-dim {
    opacity: 0.5;
}

.xterm-underline {
    text-decoration: underline;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Terminal {
  min-width: 240px;
  min-height: 120px;
}

.jp-Terminal-body {
  padding: 8px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Tooltip {
  background: var(--jp-layout-color1);
  border: var(--jp-border-width) solid var(--jp-border-color1);
  font-size: var(--jp-ui-font-size0);
  box-shadow: var(--jp-elevation-z6);
  max-width: 650px;
  z-index: 10001;
  padding: 4px;
  display: flex;
}

.jp-Tooltip-content {
  overflow: auto;
}

.jp-Tooltip:focus {
  outline: 0;
}

.jp-Tooltip pre {
  white-space: pre-wrap;
  margin: 0;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
</style><style>/**
  Copyright (c) Jupyter Development Team.
  Distributed under the terms of the Modified BSD License.
*/

/* Base styles */
.jp-RenderedVDOM {
  width: 100%;
  height: 100%;
  padding: 0;
  overflow: auto;
}

/* Document styles */
.jp-MimeDocument .jp-RenderedVDOM {
  padding: 5px;
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-RenderedVegaCommon4 {
  margin-left: 8px;
  margin-top: 8px;
}

.jp-MimeDocument .jp-RenderedVegaCommon4 {
  padding: 16px;
}

.vega canvas {
  background: var(--jp-vega-background);
}
</style><style>/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */
</style><style>/* This is a generated file of CSS imports */
/* It was generated by @jupyterlab/buildutils in Build.ensureAssets() */
</style><style>.fwu96q8{background:black;border:1px solid black;border-radius:3px;height:10px;margin-left:4px;overflow:hidden;width:100px}.fgn7udo{background:var(--jp-brand-color2);height:10px}.f1235lqo{color:var(--jp-ui-font-color1);font-family:var(--jp-ui-font-family);font-size:var(--jp-ui-font-size1);line-height:24px}.f1fvo1r7{background-color:#FFD2D2;color:#D8000C;font-family:var(--jp-ui-font-family);font-size:var(--jp-ui-font-size1)}.f2s1awa{align-items:center;display:flex;flex-direction:row}.f17wptjy{align-items:center;background:var(--jp-layout-color2);display:flex;justify-content:space-between;min-height:24px;padding-left:10px;padding-right:10px}.fddsvlq{align-items:center;display:flex}.fy1visq{flex-direction:row}.f1fwtl1j{flex-direction:row-reverse}.f1ydny4p{color:var(--jp-ui-font-color1);height:24px;margin-left:2px;margin-right:2px;max-height:24px;padding-left:6px;padding-right:6px;text-overflow:ellipsis;white-space:nowrap}.f1rbgl4n{background-color:var(--jp-brand-color1)}.f1rbgl4n .f1235lqo{color:white}.fwgmxe9:hover{background-color:var(--jp-layout-color3)}.fzt5yh7{box-shadow:0px 4px 4px rgba(0, 0, 0, 0.25)}.f1mm715f{background-color:var(--jp-layout-color2);box-shadow:var(--jp-toolbar-box-shadow);font-size:var(--jp-ui-font-size1);padding:4px 12px;z-index:2}.f4ilvu8{color:var(--jp-ui-font-color0);font-size:var(--jp-ui-font-size0);line-height:var(--jp-ui-font-size1);margin-top:4px}.f1958oj{background-position:center;background-repeat:no-repeat;background-size:16px;border:none;border-radius:0px;height:24px;outline:none;padding:0px 12px;position:absolute;right:8px;top:4px;width:12px}.fb0mcj4{background-color:var(--jp-brand-color1);background-position:center;background-repeat:no-repeat;background-size:16px;border:none;border-radius:0px;box-sizing:border-box;height:100%;outline:none;padding:4px 6px;position:absolute;right:0px;top:0px;width:100%}.fya4nu5{background-color:transparent;background-position:center;background-repeat:no-repeat;background-size:16px;border:none;border-radius:0px;box-sizing:border-box;height:100%;outline:none;position:absolute;right:0px;top:0px;width:100%}.f123ynex{background-color:var(--jp-input-active-background);border:1px solid var(--jp-border-color0);height:22px;overflow:hidden;padding:0px 8px}.f1bwa14q{border:var(--jp-border-width) solid var(--md-blue-500);box-shadow:inset 0 0 4px var(--md-blue-300)}.f13uy5em{background:transparent;border:none;color:var(--jp-ui-font-color0);height:100%;line-height:28px;outline:none;width:200px}.f189oo9n{align-items:center;animation:0.3s fade-in linear forwards;display:flex;height:100%;width:100%;z-index:1}.f189oo9n svg{display:block;margin:0 auto;width:100px}.f1xpzunt{align-items:center;display:flex}.f1xpzunt svg{display:block;height:auto;margin:2px 2px 2px 8px;width:16px}.fvaq30{align-items:center;display:flex}.fvaq30 svg{display:block;height:16px;margin:0 auto;width:16px}.f1qewoua{align-items:center;display:flex;height:14px;margin:0 14px 0 auto}.f1qewoua svg{display:block;height:14px;margin:0 auto;width:14px}.f1dvozo{align-items:center;display:flex}.jp-SideBar.jp-mod-left .lm-TabBar-tab .f1dvozo{transform:rotate(90deg)}.jp-SideBar.jp-mod-left .lm-TabBar-tab.lm-mod-current .f1dvozo{transform:rotate(90deg)
    translate(
      calc(-0.5 * var(--jp-border-width)),
      calc(-0.5 * var(--jp-border-width))
    )}.jp-SideBar.jp-mod-right .lm-TabBar-tab .f1dvozo{transform:rotate(-90deg)}.jp-SideBar.jp-mod-right .lm-TabBar-tab.lm-mod-current .f1dvozo{transform:rotate(-90deg)
    translate(
      calc(0.5 * var(--jp-border-width)),
      calc(-0.5 * var(--jp-border-width))
    )}.f1dvozo svg{display:block;height:auto;margin:0 auto;width:20px}.f1vya9e0{align-items:center;display:inline-block;vertical-align:middle}.f1vya9e0 svg{display:block;height:16px;margin:0 auto;width:16px}.f1q2iu0g svg{height:18px;left:1px;position:relative;top:3px;width:20px}.f1m7xje8 svg{height:18px;left:0px;position:relative;top:2px;width:20px}.f9v3xdu:first-child svg{bottom:1px;margin-left:0px;position:relative}.f9v3xdu:hover{background-color:var(--jp-layout-color2)}.jp-mod-dropTarget.f9v3xdu{background-color:var(--jp-brand-color2);opacity:0.7}.f9v3xdu svg{border-radius:var(--jp-border-radius);cursor:pointer;height:16px;margin:0px 2px;padding:0px 2px;vertical-align:middle;width:16px}.fllbajr{align-items:center;display:inline;height:16px;width:16px}.fllbajr svg{display:block;float:right;height:auto;margin:-2px 0 0 0;width:20px}.f1rp7tpl{align-items:center;display:flex}.f1rp7tpl svg{display:block;height:28px;margin:0 0 0 auto}.f1st5hdn{pointer-events:none}.f1st5hdn svg{height:auto;position:absolute;right:8px;top:5px;width:18px}.f1wdfp6t svg{margin-left:8px}.fuyqggs{align-items:center;display:flex}.fuyqggs svg{display:block;height:18px;margin:0 auto;margin-left:3px;margin-right:-5px;width:18px}.f1xliy8o{align-items:center;display:inline-block;margin:auto;vertical-align:middle}.f1xliy8o svg{display:block;height:16px;margin:0 auto;width:16px}.f14jk5uf{align-items:center;display:inline-block;margin:auto;vertical-align:middle}.f14jk5uf svg{align-self:normal;display:block;height:24px;margin:0 auto;width:16px}.f1ozlkqi{pointer-events:none}.f1ozlkqi svg{height:auto;position:absolute;right:7px;top:5px;width:16px}.fix2bjg{align-items:center;display:flex}.lm-DockPanel-tabBar .fix2bjg{margin-right:4px}#tab-manager .fix2bjg{margin-right:2px;position:relative}.fix2bjg svg{display:block;margin:0 auto;width:100%}.lm-DockPanel-tabBar .fix2bjg svg{height:14px;width:14px}#tab-manager .fix2bjg svg{height:16px;width:16px}.f188lp99{align-items:center;display:inline-block;margin:auto;vertical-align:middle}.f188lp99 svg{display:block;height:auto;margin:0 auto;width:20px}.fratzd0{align-items:center;display:flex;margin:0px 4px 0px 12px}.fratzd0 svg{display:block;height:16px;margin:0 auto;width:16px}.fm5u5yq{align-items:center;display:flex;flex:0 0 20px;margin-right:4px;position:relative}.fm5u5yq svg{display:block;height:16px;margin:0 auto;width:16px}.f1hgkb35{align-items:center;box-sizing:border-box;display:flex;height:32px;margin-right:12px;width:32px}.f1hgkb35 svg{display:block;height:32px;margin:0 auto;width:32px}.f187g4yd{align-items:center;display:flex;height:52px;width:52px}.f187g4yd svg{display:block;height:52px;margin:0 auto;width:52px}</style><script type="text/javascript" src="./asssignment01_files/MathJax.js.download" charset="utf-8"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888; display: contents}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">div.MathJax_MathML {text-align: center; margin: .75em 0px; display: block!important}
.MathJax_MathML {font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
span.MathJax_MathML {display: inline!important}
.MathJax_mmlExBox {display: block!important; overflow: hidden; height: 1px; width: 60ex; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0}
[class="MJX-tex-oldstyle"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-oldstyle-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
[class="MJX-tex-caligraphic"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-caligraphic-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
@font-face /*1*/ {font-family: MathJax_Caligraphic-WEB; src: url('http://localhost:8890/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf')}
@font-face /*2*/ {font-family: MathJax_Caligraphic-WEB; font-weight: bold; src: url('http://localhost:8890/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf')}
[mathvariant="double-struck"] {font-family: MathJax_AMS, MathJax_AMS-WEB}
[mathvariant="script"] {font-family: MathJax_Script, MathJax_Script-WEB}
[mathvariant="fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB}
[mathvariant="bold-script"] {font-family: MathJax_Script, MathJax_Caligraphic-WEB; font-weight: bold}
[mathvariant="bold-fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB; font-weight: bold}
[mathvariant="monospace"] {font-family: monospace}
[mathvariant="sans-serif"] {font-family: sans-serif}
[mathvariant="bold-sans-serif"] {font-family: sans-serif; font-weight: bold}
[mathvariant="sans-serif-italic"] {font-family: sans-serif; font-style: italic}
[mathvariant="sans-serif-bold-italic"] {font-family: sans-serif; font-style: italic; font-weight: bold}
@font-face /*3*/ {font-family: MathJax_AMS-WEB; src: url('http://localhost:8890/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf')}
@font-face /*4*/ {font-family: MathJax_Script-WEB; src: url('http://localhost:8890/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf')}
@font-face /*5*/ {font-family: MathJax_Fraktur-WEB; src: url('http://localhost:8890/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf')}
@font-face /*6*/ {font-family: MathJax_Fraktur-WEB; font-weight: bold; src: url('http://localhost:8890/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf')}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script charset="utf-8" src="./asssignment01_files/4.69406a7d6939b46f4e98.js.download"></script></head>
<body data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light" data-jp-theme-scrollbars="false"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div>

<script type="text/javascript">
  /* Remove token from URL. */
  (function () {
    var location = window.location;
    var search = location.search;

    // If there is no query string, bail.
    if (search.length <= 1) {
      return;
    }

    // Rebuild the query string without the `token`.
    var query = '?' + search.slice(1).split('&')
      .filter(function (param) { return param.split('=')[0] !== 'token'; })
      .join('&');

    // Rebuild the URL with the new query string.
    var url = location.origin + location.pathname +
      (query !== '?' ? query : '') + location.hash;

    if (url === location.href) {
      return;
    }

    window.history.replaceState({ }, '', url);
  })();
</script>

<script type="text/javascript" src="./asssignment01_files/main.7aaa2340f7c631eb6cc8.js.download"></script><script type="text/javascript" src="./asssignment01_files/vendors_main.d6ae31c7fff1f92f0bb6.js.download"></script>
<link rel="stylesheet" type="text/css" href="./asssignment01_files/index.css"><div class="lm-Widget p-Widget jp-LabShell" id="main" data-direction="top-to-bottom" data-alignment="start" data-shell-mode="multiple-document" style="min-width: 227px; min-height: 118px;"><div class="lm-Widget p-Widget lm-Panel p-Panel lm-BoxPanel p-BoxPanel lm-mod-hidden p-mod-hidden" data-direction="top-to-bottom" data-alignment="start" id="jp-header-panel" style="position: absolute; min-width: 0px; min-height: 0px;"></div><div class="lm-Widget p-Widget lm-Panel p-Panel" id="jp-top-panel" style="position: absolute; top: 0px; left: 0px; width: 1920px; height: 28px;"><div class="lm-Widget p-Widget f1xpzunt" id="jp-MainLogo"><svg xmlns="http://www.w3.org/2000/svg" width="39" height="51" viewBox="0 0 39 51" data-icon="ui-components:jupyter" data-icon-id="d482cbbe-b987-4881-8ac2-428e034e1154"><g transform="translate(-1638 -2281)"><g class="jp-icon-warn0" fill="#F37726"><path transform="translate(1639.74 2311.98)" d="M 18.2646 7.13411C 10.4145 7.13411 3.55872 4.2576 0 0C 1.32539 3.8204 3.79556 7.13081 7.0686 9.47303C 10.3417 11.8152 14.2557 13.0734 18.269 13.0734C 22.2823 13.0734 26.1963 11.8152 29.4694 9.47303C 32.7424 7.13081 35.2126 3.8204 36.538 0C 32.9705 4.2576 26.1148 7.13411 18.2646 7.13411Z"></path><path transform="translate(1639.73 2285.48)" d="M 18.2733 5.93931C 26.1235 5.93931 32.9793 8.81583 36.538 13.0734C 35.2126 9.25303 32.7424 5.94262 29.4694 3.6004C 26.1963 1.25818 22.2823 0 18.269 0C 14.2557 0 10.3417 1.25818 7.0686 3.6004C 3.79556 5.94262 1.32539 9.25303 0 13.0734C 3.56745 8.82463 10.4232 5.93931 18.2733 5.93931Z"></path></g><g class="jp-icon3" fill="#616161"><path transform="translate(1669.3 2281.31)" d="M 5.89353 2.844C 5.91889 3.43165 5.77085 4.01367 5.46815 4.51645C 5.16545 5.01922 4.72168 5.42015 4.19299 5.66851C 3.6643 5.91688 3.07444 6.00151 2.49805 5.91171C 1.92166 5.8219 1.38463 5.5617 0.954898 5.16401C 0.52517 4.76633 0.222056 4.24903 0.0839037 3.67757C -0.0542483 3.10611 -0.02123 2.50617 0.178781 1.95364C 0.378793 1.4011 0.736809 0.920817 1.20754 0.573538C 1.67826 0.226259 2.24055 0.0275919 2.82326 0.00267229C 3.60389 -0.0307115 4.36573 0.249789 4.94142 0.782551C 5.51711 1.31531 5.85956 2.05676 5.89353 2.844Z"></path><path transform="translate(1639.8 2323.81)" d="M 7.42789 3.58338C 7.46008 4.3243 7.27355 5.05819 6.89193 5.69213C 6.51031 6.32607 5.95075 6.83156 5.28411 7.1446C 4.61747 7.45763 3.87371 7.56414 3.14702 7.45063C 2.42032 7.33712 1.74336 7.0087 1.20184 6.50695C 0.660328 6.0052 0.27861 5.35268 0.105017 4.63202C -0.0685757 3.91135 -0.0262361 3.15494 0.226675 2.45856C 0.479587 1.76217 0.931697 1.15713 1.52576 0.720033C 2.11983 0.282935 2.82914 0.0334395 3.56389 0.00313344C 4.54667 -0.0374033 5.50529 0.316706 6.22961 0.987835C 6.95393 1.65896 7.38484 2.59235 7.42789 3.58338L 7.42789 3.58338Z"></path><path transform="translate(1638.36 2286.06)" d="M 2.27471 4.39629C 1.84363 4.41508 1.41671 4.30445 1.04799 4.07843C 0.679268 3.8524 0.385328 3.52114 0.203371 3.12656C 0.0214136 2.73198 -0.0403798 2.29183 0.0258116 1.86181C 0.0920031 1.4318 0.283204 1.03126 0.575213 0.710883C 0.867222 0.39051 1.24691 0.164708 1.66622 0.0620592C 2.08553 -0.0405897 2.52561 -0.0154714 2.93076 0.134235C 3.33591 0.283941 3.68792 0.551505 3.94222 0.90306C 4.19652 1.25462 4.34169 1.67436 4.35935 2.10916C 4.38299 2.69107 4.17678 3.25869 3.78597 3.68746C 3.39516 4.11624 2.85166 4.37116 2.27471 4.39629L 2.27471 4.39629Z"></path></g></g>&gt;</svg></div><div tabindex="-1" class="lm-Widget p-Widget lm-MenuBar p-MenuBar" id="jp-MainMenu"><ul class="lm-MenuBar-content p-MenuBar-content"><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">File</div></li><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">Edit</div></li><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">View</div></li><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">Run</div></li><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">Kernel</div></li><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">Tabs</div></li><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">Settings</div></li><li class="lm-MenuBar-item p-MenuBar-item"><div class="lm-MenuBar-itemIcon p-MenuBar-itemIcon"></div><div class="lm-MenuBar-itemLabel p-MenuBar-itemLabel">Help</div></li></ul></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel lm-BoxPanel p-BoxPanel" data-direction="left-to-right" data-alignment="start" id="jp-main-content-panel" style="position: absolute; min-width: 227px; min-height: 66px; top: 28px; left: 0px; width: 1920px; height: 989px;"><div class="lm-Widget p-Widget lm-TabBar p-TabBar jp-SideBar jp-mod-left lm-BoxPanel-child p-BoxPanel-child" data-orientation="horizontal" style="position: absolute; top: 0px; left: 0px; width: 33px; height: 989px;"><ul class="lm-TabBar-content p-TabBar-content"><li title="File Browser (Ctrl+Shift+F)" class="lm-TabBar-tab p-TabBar-tab lm-mod-current p-mod-current" data-id="filebrowser" style="z-index: 6;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon f1dvozo"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:folder" data-icon-id="70e74f7c-f391-4c07-844e-ee10a7fdedf0"><path class="jp-icon3 jp-icon-selectable" fill="#616161" d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"></path></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel"></div><div class="lm-TabBar-tabCloseIcon p-TabBar-tabCloseIcon"></div></li><li title="Running Terminals and Kernels" class="lm-TabBar-tab p-TabBar-tab" data-id="jp-running-sessions" style="z-index: 4;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon f1dvozo"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 512 512" data-icon="ui-components:running" data-icon-id="1d3d44a7-2fb7-4d2c-9200-7f41e9891ee5"><g class="jp-icon3" fill="#616161"><path d="M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm96 328c0 8.8-7.2 16-16 16H176c-8.8 0-16-7.2-16-16V176c0-8.8 7.2-16 16-16h160c8.8 0 16 7.2 16 16v160z"></path></g></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel"></div><div class="lm-TabBar-tabCloseIcon p-TabBar-tabCloseIcon"></div></li><li title="Commands (Ctrl+Shift+C)" class="lm-TabBar-tab p-TabBar-tab" data-id="command-palette" style="z-index: 3;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon f1dvozo"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:palette" data-icon-id="f9761842-08bb-4662-b948-9a30f2556270"><g class="jp-icon3" fill="#616161"><path d="M18 13V20H4V6H9.02C9.07 5.29 9.24 4.62 9.5 4H4C2.9 4 2 4.9 2 6V20C2 21.1 2.9 22 4 22H18C19.1 22 20 21.1 20 20V15L18 13ZM19.3 8.89C19.74 8.19 20 7.38 20 6.5C20 4.01 17.99 2 15.5 2C13.01 2 11 4.01 11 6.5C11 8.99 13.01 11 15.49 11C16.37 11 17.19 10.74 17.88 10.3L21 13.42L22.42 12L19.3 8.89ZM15.5 9C14.12 9 13 7.88 13 6.5C13 5.12 14.12 4 15.5 4C16.88 4 18 5.12 18 6.5C18 7.88 16.88 9 15.5 9Z"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M4 6H9.01894C9.00639 6.16502 9 6.33176 9 6.5C9 8.81577 10.211 10.8487 12.0343 12H9V14H16V12.9811C16.5703 12.9377 17.12 12.8207 17.6396 12.6396L18 13V20H4V6ZM8 8H6V10H8V8ZM6 12H8V14H6V12ZM8 16H6V18H8V16ZM9 16H16V18H9V16Z"></path></g></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel"></div><div class="lm-TabBar-tabCloseIcon p-TabBar-tabCloseIcon"></div></li><li title="Property Inspector" class="lm-TabBar-tab p-TabBar-tab" data-id="jp-property-inspector" style="z-index: 2;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon f1dvozo"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:build" data-icon-id="0b489b04-5c94-4717-855a-a7470d6888cb"><g class="jp-icon3" fill="#616161"><path d="M14.9 17.45C16.25 17.45 17.35 16.35 17.35 15C17.35 13.65 16.25 12.55 14.9 12.55C13.54 12.55 12.45 13.65 12.45 15C12.45 16.35 13.54 17.45 14.9 17.45ZM20.1 15.68L21.58 16.84C21.71 16.95 21.75 17.13 21.66 17.29L20.26 19.71C20.17 19.86 20 19.92 19.83 19.86L18.09 19.16C17.73 19.44 17.33 19.67 16.91 19.85L16.64 21.7C16.62 21.87 16.47 22 16.3 22H13.5C13.32 22 13.18 21.87 13.15 21.7L12.89 19.85C12.46 19.67 12.07 19.44 11.71 19.16L9.96002 19.86C9.81002 19.92 9.62002 19.86 9.54002 19.71L8.14002 17.29C8.05002 17.13 8.09002 16.95 8.22002 16.84L9.70002 15.68L9.65001 15L9.70002 14.31L8.22002 13.16C8.09002 13.05 8.05002 12.86 8.14002 12.71L9.54002 10.29C9.62002 10.13 9.81002 10.07 9.96002 10.13L11.71 10.84C12.07 10.56 12.46 10.32 12.89 10.15L13.15 8.28998C13.18 8.12998 13.32 7.99998 13.5 7.99998H16.3C16.47 7.99998 16.62 8.12998 16.64 8.28998L16.91 10.15C17.33 10.32 17.73 10.56 18.09 10.84L19.83 10.13C20 10.07 20.17 10.13 20.26 10.29L21.66 12.71C21.75 12.86 21.71 13.05 21.58 13.16L20.1 14.31L20.15 15L20.1 15.68Z"></path><path d="M7.32966 7.44454C8.0831 7.00954 8.33932 6.05332 7.90432 5.29988C7.46932 4.54643 6.5081 4.28156 5.75466 4.71656C5.39176 4.92608 5.12695 5.27118 5.01849 5.67594C4.91004 6.08071 4.96682 6.51198 5.17634 6.87488C5.61134 7.62832 6.57622 7.87954 7.32966 7.44454ZM9.65718 4.79593L10.8672 4.95179C10.9628 4.97741 11.0402 5.07133 11.0382 5.18793L11.0388 6.98893C11.0455 7.10054 10.9616 7.19518 10.855 7.21054L9.66001 7.38083L9.23915 8.13188L9.66961 9.25745C9.70729 9.36271 9.66934 9.47699 9.57408 9.53199L8.01523 10.432C7.91131 10.492 7.79337 10.4677 7.72105 10.3824L6.98748 9.43188L6.10931 9.43083L5.34704 10.3905C5.28909 10.4702 5.17383 10.4905 5.07187 10.4339L3.51245 9.53293C3.41049 9.47633 3.37647 9.35741 3.41075 9.25679L3.86347 8.14093L3.61749 7.77488L3.42347 7.37883L2.23075 7.21297C2.12647 7.19235 2.04049 7.10342 2.04245 6.98682L2.04187 5.18582C2.04383 5.06922 2.11909 4.97958 2.21704 4.96922L3.42065 4.79393L3.86749 4.02788L3.41105 2.91731C3.37337 2.81204 3.41131 2.69776 3.51523 2.63776L5.07408 1.73776C5.16934 1.68276 5.28729 1.70704 5.35961 1.79231L6.11915 2.72788L6.98001 2.73893L7.72496 1.78922C7.79156 1.70458 7.91548 1.67922 8.00879 1.74082L9.56821 2.64182C9.67017 2.69842 9.71285 2.81234 9.68723 2.90797L9.21718 4.03383L9.46316 4.39988L9.65718 4.79593Z"></path></g></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel"></div><div class="lm-TabBar-tabCloseIcon p-TabBar-tabCloseIcon"></div></li><li title="Open Tabs" class="lm-TabBar-tab p-TabBar-tab" data-id="tab-manager" style="z-index: 1;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon f1dvozo"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:tab" data-icon-id="663a8fe9-b853-4213-a0be-6c1e14085d3e"><g class="jp-icon3" fill="#616161"><path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h10v4h8v10z"></path></g></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel"></div><div class="lm-TabBar-tabCloseIcon p-TabBar-tabCloseIcon"></div></li><li title="Extension Manager" class="lm-TabBar-tab p-TabBar-tab" data-id="extensionmanager.main-view" style="z-index: 0;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon f1dvozo"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:extension" data-icon-id="be57ad79-3d9f-4620-b4de-97165a28a1fe"><g class="jp-icon3" fill="#616161"><path d="M20.5 11H19V7c0-1.1-.9-2-2-2h-4V3.5C13 2.12 11.88 1 10.5 1S8 2.12 8 3.5V5H4c-1.1 0-1.99.9-1.99 2v3.8H3.5c1.49 0 2.7 1.21 2.7 2.7s-1.21 2.7-2.7 2.7H2V20c0 1.1.9 2 2 2h3.8v-1.5c0-1.49 1.21-2.7 2.7-2.7 1.49 0 2.7 1.21 2.7 2.7V22H17c1.1 0 2-.9 2-2v-4h1.5c1.38 0 2.5-1.12 2.5-2.5S21.88 11 20.5 11z"></path></g></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel"></div><div class="lm-TabBar-tabCloseIcon p-TabBar-tabCloseIcon"></div></li></ul></div><div class="lm-Widget p-Widget lm-Panel p-Panel lm-SplitPanel p-SplitPanel lm-BoxPanel-child p-BoxPanel-child" data-orientation="horizontal" data-alignment="start" id="jp-main-split-panel" style="position: absolute; min-width: 194px; min-height: 66px; top: 0px; left: 33px; width: 1887px; height: 989px;"><div class="lm-Widget p-Widget lm-Panel p-Panel lm-StackedPanel p-StackedPanel lm-SplitPanel-child p-SplitPanel-child" id="jp-left-stack" style="position: absolute; min-width: 181px; min-height: 0px; top: 0px; left: 0px; width: 419.333px; height: 989px;"><div class="lm-Widget p-Widget lm-CommandPalette p-CommandPalette lm-StackedPanel-child p-StackedPanel-child lm-mod-hidden p-mod-hidden" id="command-palette" style="position: absolute; z-index: 2; top: 0px; left: 0px; width: 418px; height: 989px;"><div class="lm-CommandPalette-search p-CommandPalette-search"><div class="lm-CommandPalette-wrapper p-CommandPalette-wrapper"><input class="lm-CommandPalette-input p-CommandPalette-input" spellcheck="false" placeholder="SEARCH"><button class="lm-close-icon" style="display: none;"></button></div></div><ul class="lm-CommandPalette-content p-CommandPalette-content"><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Console<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:change-kernel"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change Kernel…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:clear"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Clear Console Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:close-and-shutdown"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Close and Shut Down…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:linebreak"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Insert Line Break</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:interrupt-kernel"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Interrupt Kernel</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="console:create"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">New Console</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:restart-kernel"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Restart Kernel…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:run-forced"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run Cell (forced)</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:run-unforced"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run Cell (unforced)</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="console:toggle-show-all-kernel-activity"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Show All Kernel Activity</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Extension Manager<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-toggled p-mod-toggled" data-command="extensionmanager:toggle"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Enable Extension Manager</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">File Operations<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-toggled p-mod-toggled" data-command="docmanager:toggle-autosave"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Autosave Documents</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="docmanager:download"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Download</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Download the file to your computer</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="filebrowser:open-path"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Open from Path…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Open from path</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="docmanager:reload"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Reload Notebook from Disk</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Reload contents from disk</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="docmanager:restore-checkpoint"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Revert Notebook to Checkpoint</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Revert contents to previous checkpoint</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="docmanager:save"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Save Notebook</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Save and create checkpoint</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+S</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="docmanager:save-as"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Save Notebook As…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Save with new path</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+S</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="filebrowser:toggle-navigate-to-current-directory"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Show Active File in File Browser</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="htmlviewer:trust-html"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Trust HTML File</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Help<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="help:open"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Jupyter Reference</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="help:open"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">JupyterLab FAQ</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="help:open"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">JupyterLab Reference</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="help:launch-classic-notebook"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Launch Classic Notebook</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="help:open"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Markdown Reference</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:reset"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Reset Application State</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Image Viewer<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:flip-horizontal"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Flip image horizontally</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">H</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:flip-vertical"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Flip image vertically</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">V</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:invert-colors"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Invert Colors</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">I</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:reset-image"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Reset Image</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">0</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:rotate-clockwise"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Rotate Clockwise</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">]</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:rotate-counterclockwise"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Rotate Counterclockwise</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">[</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:zoom-in"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Zoom In</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">=</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="imageviewer:zoom-out"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Zoom Out</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">-</div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Kernel Operations<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="kernelmenu:shutdownAll"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Shut Down All Kernels…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Launcher<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="launcher:create"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">New Launcher</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Main Area<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:activate-next-tab"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Activate Next Tab</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+]</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:activate-next-tab-bar"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Activate Next Tab Bar</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+.</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:activate-previous-tab"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Activate Previous Tab</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+[</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:activate-previous-tab-bar"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Activate Previous Tab Bar</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+,</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="tabsmenu:activate-previously-used-tab"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Activate Previously Used Tab</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+'</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:close-other-tabs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Close All Other Tabs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:close-all"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Close All Tabs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:close"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Close Tab</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Alt+W</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="application:close-right-tabs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Close Tabs to Right</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="documentsearch:highlightNext"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Find Next</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+G</div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="documentsearch:highlightPrevious"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Find Previous</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+G</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="documentsearch:start"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Find…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+F</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="filemenu:logout"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Log Out</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Log out of JupyterLab</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:toggle-presentation-mode"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Presentation Mode</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-toggled p-mod-toggled" data-command="application:toggle-left-area"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Show Left Sidebar</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+B</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="logconsole:open"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Show Log Console</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-toggled p-mod-toggled" data-command="statusbar:toggle"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Show Status Bar</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="filemenu:shutdown"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Shut Down</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Shut down JupyterLab</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="application:toggle-mode"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Single-Document Mode</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+D</div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Notebook Cell Operations<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-code"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Code Cell Type</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Y</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-heading-1"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Heading 1</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">1</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-heading-2"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Heading 2</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">2</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-heading-3"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Heading 3</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">3</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-heading-4"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Heading 4</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">4</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-heading-5"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Heading 5</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">5</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-heading-6"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Heading 6</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">6</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-markdown"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Markdown Cell Type</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">M</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-cell-to-raw"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change to Raw Cell Type</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">R</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:clear-cell-output"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Clear Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:hide-all-cell-code"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Collapse All Code</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:hide-all-cell-outputs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Collapse All Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:hide-cell-code"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Collapse Selected Code</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:hide-cell-outputs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Collapse Selected Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:copy-cell"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Copy Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">C</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:cut-cell"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Cut Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">X</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:delete-cell"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Delete Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">D, D</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:disable-output-scrolling"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Disable Scrolling for Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:enable-output-scrolling"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Enable Scrolling for Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:show-all-cell-code"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Expand All Code</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:show-all-cell-outputs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Expand All Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:show-cell-code"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Expand Selected Code</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:show-cell-outputs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Expand Selected Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:extend-marked-cells-above"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Extend Selection Above</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+K</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:extend-marked-cells-below"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Extend Selection Below</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+J</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:extend-marked-cells-bottom"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Extend Selection to Bottom</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+End</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:extend-marked-cells-top"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Extend Selection to Top</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+Home</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:insert-cell-above"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Insert Cell Above</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">A</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:insert-cell-below"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Insert Cell Below</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">B</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:merge-cells"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Merge Selected Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+M</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:move-cell-down"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Move Cells Down</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:move-cell-up"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Move Cells Up</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:paste-cell-above"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Paste Cells Above</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:paste-and-replace-cell"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Paste Cells and Replace</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:paste-cell-below"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Paste Cells Below</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">V</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:redo-cell-action"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Redo Cell Operation</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+Z</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:run-cell-and-select-next"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run Selected Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+Enter</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:run-cell"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run Selected Cells and Don't Advance</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Enter</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:run-cell-and-insert-below"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run Selected Cells and Insert Below</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Alt+Enter</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:run-in-console"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run Selected Text or Current Line in Console</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:move-cursor-up"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Select Cell Above</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">K</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:move-cursor-down"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Select Cell Below</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">J</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:split-cell-at-cursor"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Split Cell</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+Shift+-</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:undo-cell-action"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Undo Cell Operation</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Z</div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Notebook Operations<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:change-kernel"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Change Kernel…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:clear-all-cell-outputs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Clear All Outputs</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:close-and-shutdown"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Close and Shut Down</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:deselect-all"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Deselect All Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:enter-command-mode"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Enter Command Mode</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+M</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:enter-edit-mode"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Enter Edit Mode</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Enter</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to Asciidoc</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to Executable Script</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to HTML</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to LaTeX</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to Markdown</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to PDF</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to ReStructured Text</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to Reveal.js Slides</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:export-to-format"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Export Notebook to Webpdf</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:interrupt-kernel"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Interrupt Kernel</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:create-console"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">New Console for Notebook</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:create-new"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">New Notebook</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Create a new notebook</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:reconnect-to-kernel"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Reconnect To Kernel</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:render-all-markdown"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Render All Markdown Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:restart-clear-output"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Restart Kernel and Clear All Outputs…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:restart-run-all"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Restart Kernel and Run All Cells…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:restart-and-run-to-selected"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Restart Kernel and Run up to Selected Cell…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:restart-kernel"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Restart Kernel…</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="notebook:run-all-above"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run All Above Selected Cell</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:run-all-cells"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run All Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="notebook:run-all-below"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Run Selected Cell and All Below</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:select-all"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Select All Cells</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+A</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:toggle-all-cell-line-numbers"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Toggle All Line Numbers</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Shift+L</div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="notebook:trust"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Trust Notebook</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Settings<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="settingeditor:open"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Advanced Settings Editor</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+,</div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Show Contextual Help<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="inspector:open"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Show Contextual Help</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Live updating code documentation from the active kernel</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut">Ctrl+I</div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Terminal<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="terminal:decrease-font"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Decrease Terminal Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="terminal:increase-font"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Increase Terminal Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="terminal:create-new"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">New Terminal</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Start a new terminal session</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-disabled p-mod-disabled" data-command="terminal:refresh"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Refresh Terminal</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Refresh the current terminal session</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="terminal:set-theme"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Use Dark Terminal Theme</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Set the terminal theme</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-toggled p-mod-toggled" data-command="terminal:set-theme"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Use Inherit Terminal Theme</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Set the terminal theme</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="terminal:set-theme"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Use Light Terminal Theme</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Set the terminal theme</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Text Editor<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:change-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Decrease Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:change-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Increase Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:change-tabs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Indent with Tab</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:create-new-markdown-file"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">New Markdown File</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Create a new markdown file</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:create-new"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">New Text File</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption">Create a new text file</div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:change-tabs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Spaces: 1 </div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:change-tabs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Spaces: 2 </div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-toggled p-mod-toggled" data-command="fileeditor:change-tabs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Spaces: 4 </div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="fileeditor:change-tabs"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Spaces: 8 </div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-header jp-icon-hoverShow p-CommandPalette-header">Theme<span class="f1qewoua"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:filter-list" data-icon-id="e4fb6507-2416-4649-b26c-ab78335c9299"><g class="jp-icon3" fill="#616161"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g></svg></span></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:decr-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Decrease Code Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:decr-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Decrease Content Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:decr-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Decrease UI Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:incr-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Increase Code Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:incr-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Increase Content Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:incr-font-size"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Increase UI Font Size</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:theme-scrollbars"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Theme Scrollbars</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item" data-command="apputils:change-theme"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Use JupyterLab Dark Theme</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li><li class="lm-CommandPalette-item p-CommandPalette-item lm-mod-toggled p-mod-toggled" data-command="apputils:change-theme"><div class="fvaq30 lm-CommandPalette-itemIcon p-CommandPalette-itemIcon"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></div><div class="lm-CommandPalette-itemContent p-CommandPalette-itemContent"><div class="lm-CommandPalette-itemLabel p-CommandPalette-itemLabel">Use JupyterLab Light Theme</div><div class="lm-CommandPalette-itemCaption p-CommandPalette-itemCaption"></div></div><div class="lm-CommandPalette-itemShortcut p-CommandPalette-itemShortcut"></div></li></ul></div><div class="lm-Widget p-Widget jp-PropertyInspector lm-mod-hidden p-mod-hidden lm-StackedPanel-child p-StackedPanel-child" id="jp-property-inspector" style="position: absolute;"><div class="lm-Widget p-Widget jp-NotebookTools jp-PropertyInspector-content" id="notebook-tools"><div class="lm-Widget p-Widget jp-RankedPanel"><div class="lm-Widget p-Widget jp-ActiveCellTool jp-InputArea jp-NotebookTools-tool"><div class="lm-Widget p-Widget jp-InputPrompt jp-InputArea-prompt">[ ]:</div><div class="lm-Widget p-Widget jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline"><div class="CodeMirror cm-s-jupyter CodeMirror-wrap jp-mod-readOnly"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 0px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="display: block; bottom: 0px;"><div style="min-width: 1px; height: 42px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"><pre class="CodeMirror-line" role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">num1</span><span class="cm-operator">=</span> <span class="cm-builtin">float</span> (<span class="cm-builtin">input</span> (<span class="cm-builtin">print</span>(<span class="cm-string">"Enter your first number: "</span>)))</span></pre></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"></div><div class="CodeMirror-code" role="presentation"></div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; border-bottom: 0px solid transparent;"></div><div class="CodeMirror-gutters" style="display: none;"></div></div></div></div></div><header class="tag-header">Tags in Notebook</header><div class="lm-Widget p-Widget jp-NotebookTools-tool"><div class="lm-Widget p-Widget tag unapplied-tag" id="add-tag"><div class="tag-holder"><input contenteditable="true" class="add-tag" style="width: 49px;"><span class="fuyqggs"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:add" data-icon-id="c72584f8-4a80-4f4f-b667-e2abf00141fc"><g class="jp-icon3" fill="#616161"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg></span></div></div></div><div class="lm-Widget p-Widget jp-KeySelector jp-NotebookTools-tool"><label>Slide Type<div class="jp-select-wrapper"><select class="jp-mod-styled"><option value="null">-</option><option value="&quot;slide&quot;">Slide</option><option value="&quot;subslide&quot;">Sub-Slide</option><option value="&quot;fragment&quot;">Fragment</option><option value="&quot;skip&quot;">Skip</option><option value="&quot;notes&quot;">Notes</option></select><span class="f1st5hdn"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-down-empty" data-icon-id="cec803f1-c626-4c1e-af5e-906414f613e5"><g class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M5.2,5.9L9,9.7l3.8-3.8l1.2,1.2l-4.9,5l-4.9-5L5.2,5.9z"></path></g></svg></span></div></label></div><div class="lm-Widget p-Widget jp-KeySelector jp-NotebookTools-tool"><label>Raw NBConvert Format<div class="jp-select-wrapper"><select class="jp-mod-styled" disabled=""><option value="null">None</option><option value="&quot;text/asciidoc&quot;">Asciidoc</option><option value="&quot;text/html&quot;">HTML</option><option value="&quot;text/latex&quot;">LaTeX</option><option value="&quot;text/markdown&quot;">Markdown</option><option value="&quot;text/x-python&quot;">Python</option><option value="&quot;text/restructuredtext&quot;">ReStructured Text</option><option value="&quot;text/html&quot;">Webpdf</option></select><span class="f1st5hdn"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-down-empty" data-icon-id="cec803f1-c626-4c1e-af5e-906414f613e5"><g class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M5.2,5.9L9,9.7l3.8-3.8l1.2,1.2l-4.9,5l-4.9-5L5.2,5.9z"></path></g></svg></span></div></label></div></div><div class="lm-Widget p-Widget jp-Collapse"><div class="lm-Widget p-Widget jp-Collapse-header f1rp7tpl">Advanced Tools<svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-up" data-icon-id="141f7446-ba87-46f5-9059-dc6a5a22d93c"><g class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M5.2,10.5L9,6.8l3.8,3.8H5.2z"></path></g></svg></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-Collapse-contents lm-mod-hidden p-mod-hidden"><div class="lm-Widget p-Widget jp-RankedPanel"><div class="lm-Widget p-Widget jp-MetadataEditorTool jp-NotebookTools-tool"><label class="lm-Widget p-Widget">Cell Metadata</label><div class="lm-Widget p-Widget jp-JSONEditor"><div class="jp-JSONEditor-header"><span title="Revert changes to data" hidden=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:undo" data-icon-id="c53dda2d-581c-4463-9710-f6dadb2d64b0"><g class="jp-icon3" fill="#616161"><path d="M12.5 8c-2.65 0-5.05.99-6.9 2.6L2 7v9h9l-3.62-3.62c1.39-1.16 3.16-1.88 5.12-1.88 3.54 0 6.55 2.31 7.6 5.5l2.37-.78C21.08 11.03 17.15 8 12.5 8z"></path></g></svg></span><span title="Commit changes to data" class="f1wdfp6t" hidden=""><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></span></div><div class="jp-JSONEditor-host jp-CodeMirrorEditor jp-Editor" data-type="inline"><div class="CodeMirror cm-s-jupyter CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 0px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="display: block; bottom: 0px;"><div style="min-width: 1px; height: 31px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"></div><div class="CodeMirror-code" role="presentation"></div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; border-bottom: 0px solid transparent;"></div><div class="CodeMirror-gutters" style="display: none;"></div></div></div></div></div></div><div class="lm-Widget p-Widget jp-MetadataEditorTool jp-NotebookTools-tool"><label class="lm-Widget p-Widget">Notebook Metadata</label><div class="lm-Widget p-Widget jp-JSONEditor"><div class="jp-JSONEditor-header"><span title="Revert changes to data" hidden=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:undo" data-icon-id="c53dda2d-581c-4463-9710-f6dadb2d64b0"><g class="jp-icon3" fill="#616161"><path d="M12.5 8c-2.65 0-5.05.99-6.9 2.6L2 7v9h9l-3.62-3.62c1.39-1.16 3.16-1.88 5.12-1.88 3.54 0 6.55 2.31 7.6 5.5l2.37-.78C21.08 11.03 17.15 8 12.5 8z"></path></g></svg></span><span title="Commit changes to data" class="f1wdfp6t" hidden=""><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:check" data-icon-id="b019c424-a59c-452c-b953-c1f685d1bb87"><g class="jp-icon3" fill="#616161"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg></span></div><div class="jp-JSONEditor-host jp-CodeMirrorEditor jp-Editor" data-type="inline"><div class="CodeMirror cm-s-jupyter CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 0px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="display: block; bottom: 0px;"><div style="min-width: 1px; height: 124px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"></div><div class="CodeMirror-code" role="presentation"></div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; border-bottom: 0px solid transparent;"></div><div class="CodeMirror-gutters" style="display: none;"></div></div></div></div></div></div></div></div></div></div></div><div class="lm-Widget p-Widget jp-RunningSessions lm-StackedPanel-child p-StackedPanel-child lm-mod-hidden p-mod-hidden" id="jp-running-sessions" style="position: absolute; z-index: 1; top: 0px; left: 0px; width: 418px; height: 989px;"><div class="jp-RunningSessions-header"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Refresh List"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:refresh"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M9 13.5c-2.49 0-4.5-2.01-4.5-4.5S6.51 4.5 9 4.5c1.24 0 2.36.52 3.17 1.33L10 8h5V3l-1.76 1.76C12.15 3.68 10.66 3 9 3 5.69 3 3.01 5.69 3.01 9S5.69 15 9 15c2.97 0 5.43-2.16 5.9-5h-1.52c-.46 2-2.24 3.5-4.38 3.5z"></path></g></svg></span></span></button></div><div class="jp-RunningSessions-section"><header class="jp-RunningSessions-sectionHeader"><h2>Kernel Sessions</h2><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Shut Down All Kernel Sessions…"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:close"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-none jp-icon-selectable-inverse jp-icon3-hover" fill="none"><circle cx="12" cy="12" r="11"></circle></g><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3 jp-icon-selectable jp-icon-accent2-hover" fill="#616161"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-none jp-icon-busy" fill="none"><circle cx="12" cy="12" r="7"></circle></g></svg></span></span></button></header><div class="jp-RunningSessions-sectionContainer"><ul class="jp-RunningSessions-sectionList"><li class="jp-RunningSessions-item"><span class="fratzd0"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:notebook"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-warn0 jp-icon-selectable" fill="#EF6C00"><path d="M18.7 3.3v15.4H3.3V3.3h15.4m1.5-1.5H1.8v18.3h18.3l.1-18.3z"></path><path d="M16.5 16.5l-5.4-4.3-5.6 4.3v-11h11z"></path></g></svg></span><span class="jp-RunningSessions-itemLabel" title="Path: Documents/Python Scripts/Untitled.ipynb
Kernel: Python 3">Untitled.ipynb</span><button class="jp-RunningSessions-itemShutdown jp-mod-styled">SHUT&nbsp;DOWN</button></li><li class="jp-RunningSessions-item"><span class="fratzd0"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:notebook"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-warn0 jp-icon-selectable" fill="#EF6C00"><path d="M18.7 3.3v15.4H3.3V3.3h15.4m1.5-1.5H1.8v18.3h18.3l.1-18.3z"></path><path d="M16.5 16.5l-5.4-4.3-5.6 4.3v-11h11z"></path></g></svg></span><span class="jp-RunningSessions-itemLabel" title="Path: Desktop/python/Untitled.ipynb
Kernel: Python 3">Untitled.ipynb</span><button class="jp-RunningSessions-itemShutdown jp-mod-styled">SHUT&nbsp;DOWN</button></li></ul></div></div><div class="jp-RunningSessions-section"><header class="jp-RunningSessions-sectionHeader"><h2>Terminal Sessions</h2><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Shut Down All Terminal Sessions…"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:close"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-none jp-icon-selectable-inverse jp-icon3-hover" fill="none"><circle cx="12" cy="12" r="11"></circle></g><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3 jp-icon-selectable jp-icon-accent2-hover" fill="#616161"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-none jp-icon-busy" fill="none"><circle cx="12" cy="12" r="7"></circle></g></svg></span></span></button></header><div class="jp-RunningSessions-sectionContainer"><ul class="jp-RunningSessions-sectionList"><li class="jp-RunningSessions-item"><span class="fratzd0"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:terminal"><rect xmlns="http://www.w3.org/2000/svg" class="jp-icon2 jp-icon-selectable" width="20" height="20" transform="translate(2 2)" fill="#333333"></rect><path xmlns="http://www.w3.org/2000/svg" class="jp-icon-accent2 jp-icon-selectable-inverse" d="M5.05664 8.76172C5.05664 8.59766 5.03125 8.45312 4.98047 8.32812C4.93359 8.19922 4.85547 8.08203 4.74609 7.97656C4.64062 7.87109 4.5 7.77539 4.32422 7.68945C4.15234 7.59961 3.94336 7.51172 3.69727 7.42578C3.30273 7.28516 2.94336 7.13672 2.61914 6.98047C2.29492 6.82422 2.01758 6.64258 1.78711 6.43555C1.56055 6.22852 1.38477 5.98828 1.25977 5.71484C1.13477 5.4375 1.07227 5.10938 1.07227 4.73047C1.07227 4.39844 1.12891 4.0957 1.24219 3.82227C1.35547 3.54492 1.51562 3.30469 1.72266 3.10156C1.92969 2.89844 2.17969 2.73437 2.47266 2.60938C2.76562 2.48438 3.0918 2.4043 3.45117 2.36914V1.10938H4.38867V2.38086C4.74023 2.42773 5.05664 2.52344 5.33789 2.66797C5.61914 2.8125 5.85742 3.00195 6.05273 3.23633C6.25195 3.4668 6.4043 3.74023 6.50977 4.05664C6.61914 4.36914 6.67383 4.7207 6.67383 5.11133H5.04492C5.04492 4.63867 4.9375 4.28125 4.72266 4.03906C4.50781 3.79297 4.2168 3.66992 3.84961 3.66992C3.65039 3.66992 3.47656 3.69727 3.32812 3.75195C3.18359 3.80273 3.06445 3.87695 2.9707 3.97461C2.87695 4.06836 2.80664 4.17969 2.75977 4.30859C2.7168 4.4375 2.69531 4.57812 2.69531 4.73047C2.69531 4.88281 2.7168 5.01953 2.75977 5.14062C2.80664 5.25781 2.88281 5.36719 2.98828 5.46875C3.09766 5.57031 3.24023 5.66797 3.41602 5.76172C3.5918 5.85156 3.81055 5.94336 4.07227 6.03711C4.4668 6.18555 4.82422 6.33984 5.14453 6.5C5.46484 6.65625 5.73828 6.83984 5.96484 7.05078C6.19531 7.25781 6.37109 7.5 6.49219 7.77734C6.61719 8.05078 6.67969 8.375 6.67969 8.75C6.67969 9.09375 6.62305 9.4043 6.50977 9.68164C6.39648 9.95508 6.23438 10.1914 6.02344 10.3906C5.8125 10.5898 5.55859 10.75 5.26172 10.8711C4.96484 10.9883 4.63281 11.0645 4.26562 11.0996V12.248H3.33398V11.0996C3.00195 11.0684 2.67969 10.9961 2.36719 10.8828C2.05469 10.7656 1.77734 10.5977 1.53516 10.3789C1.29688 10.1602 1.10547 9.88477 0.960938 9.55273C0.816406 9.2168 0.744141 8.81445 0.744141 8.3457H2.37891C2.37891 8.62695 2.41992 8.86328 2.50195 9.05469C2.58398 9.24219 2.68945 9.39258 2.81836 9.50586C2.95117 9.61523 3.10156 9.69336 3.26953 9.74023C3.4375 9.78711 3.60938 9.81055 3.78516 9.81055C4.20312 9.81055 4.51953 9.71289 4.73438 9.51758C4.94922 9.32227 5.05664 9.07031 5.05664 8.76172ZM13.418 12.2715H8.07422V11H13.418V12.2715Z" transform="translate(3.95264 6)" fill="white"></path></svg></span><span class="jp-RunningSessions-itemLabel" title="">terminals/1</span><button class="jp-RunningSessions-itemShutdown jp-mod-styled">SHUT&nbsp;DOWN</button></li></ul></div></div></div><div class="lm-Widget p-Widget lm-TabBar p-TabBar lm-StackedPanel-child p-StackedPanel-child lm-mod-hidden p-mod-hidden" data-orientation="vertical" id="tab-manager" style="position: absolute; z-index: 4; top: 0px; left: 0px; width: 418px; height: 989px;"><header>Open Tabs</header><ul class="lm-TabBar-content p-TabBar-content"><li title="" class="lm-TabBar-tab p-TabBar-tab        lm-mod-closable p-mod-closable lm-mod-current p-mod-current" data-id="launcher-0" style="z-index: 2;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon fix2bjg"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:launcher" data-icon-id="94409f6a-2330-4c66-b90d-cf2e788d65d4"><path class="jp-icon3 jp-icon-selectable" fill="#616161" d="M19 19H5V5h7V3H5a2 2 0 00-2 2v14a2 2 0 002 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel">Launcher</div><div class="jp-icon-hover lm-TabBar-tabCloseIcon fvaq30"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:close" data-icon-id="4505d2c6-1a49-487e-a8cd-1b14d350bc4e"><g class="jp-icon-none jp-icon-selectable-inverse jp-icon3-hover" fill="none"><circle cx="12" cy="12" r="11"></circle></g><g class="jp-icon3 jp-icon-selectable jp-icon-accent2-hover" fill="#616161"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g><g class="jp-icon-none jp-icon-busy" fill="none"><circle cx="12" cy="12" r="7"></circle></g></svg></div></li><li title="Name: Untitled.ipynb
Path: Desktop/python/Untitled.ipynb
Last Saved: 2021-01-08 13:36
Last Checkpoint: 2021-01-08 13:35" class="lm-TabBar-tab p-TabBar-tab   jp-mod-current        jp-mod-active lm-mod-closable p-mod-closable" data-type="document-title" data-id="id-f8e6f125-2161-4a87-b0c3-7943859df25c" style="z-index: 0;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon fix2bjg"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:notebook" data-icon-id="3d88fa5d-d794-4476-be84-690c3938827f"><g class="jp-icon-warn0 jp-icon-selectable" fill="#EF6C00"><path d="M18.7 3.3v15.4H3.3V3.3h15.4m1.5-1.5H1.8v18.3h18.3l.1-18.3z"></path><path d="M16.5 16.5l-5.4-4.3-5.6 4.3v-11h11z"></path></g></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel">Untitled.ipynb</div><div class="jp-icon-hover lm-TabBar-tabCloseIcon fvaq30"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:close" data-icon-id="4505d2c6-1a49-487e-a8cd-1b14d350bc4e"><g class="jp-icon-none jp-icon-selectable-inverse jp-icon3-hover" fill="none"><circle cx="12" cy="12" r="11"></circle></g><g class="jp-icon3 jp-icon-selectable jp-icon-accent2-hover" fill="#616161"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g><g class="jp-icon-none jp-icon-busy" fill="none"><circle cx="12" cy="12" r="7"></circle></g></svg></div></li></ul></div><div class="lm-Widget p-Widget jp-extensionmanager-view lm-StackedPanel-child p-StackedPanel-child lm-mod-hidden p-mod-hidden" id="extensionmanager.main-view" style="position: absolute; z-index: 5; top: 0px; left: 0px; width: 418px; height: 989px;"><div class="jp-extensionmanager-search-bar"><div class="bp3-input-group bp3-disabled jp-extensionmanager-search-wrapper jp-InputGroup"><input type="text" class="bp3-input" placeholder="SEARCH" disabled="" value="" style="padding-right: 28px;"><span class="bp3-input-action"><div class="jp-InputGroupAction"><span icon="search" class="bp3-icon bp3-icon-search jp-BPIcon"><svg data-icon="search" width="16" height="16" viewBox="0 0 16 16"><desc>search</desc><path d="M15.55 13.43l-2.67-2.68a6.94 6.94 0 001.11-3.76c0-3.87-3.13-7-7-7s-7 3.13-7 7 3.13 7 7 7c1.39 0 2.68-.42 3.76-1.11l2.68 2.67a1.498 1.498 0 102.12-2.12zm-8.56-1.44c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z" fill-rule="evenodd"></path></svg></span></div></span></div></div><div class="jp-extensionmanager-pending "></div><div class="jp-extensionmanager-content"><header><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f188lp99"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-down"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M5.2,7.5L9,11.2l3.8-3.8H5.2z"></path></g></svg></span></span></button><span class="jp-extensionmanager-headerText">Warning</span></header><div class="bp3-collapse" style="height: auto; overflow-y: visible; transition: none 0s ease 0s;"><div class="bp3-collapse-body" aria-hidden="false" style="transform: translateY(0px); transition: none 0s ease 0s;"><div class="jp-extensionmanager-disclaimer"><div>The JupyterLab development team is excited to have a robust third-party extension community. However, we do not review third-party extensions, and some extensions may introduce security risks or contain malicious code that runs on your machine.</div><div style="padding-top: 8px;"><button type="button" class="bp3-button jp-extensionmanager-disclaimer-enable jp-Button"><span class="bp3-button-text">Enable</span></button></div></div></div></div><header><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f188lp99"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-right"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M7.2,5.2L10.9,9l-3.8,3.8V5.2H7.2z"></path></g></svg></span></span></button><span class="jp-extensionmanager-headerTextDisabled">Installed</span></header><div class="bp3-collapse"><div class="bp3-collapse-body" aria-hidden="false"></div></div><header><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f188lp99"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-right"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M7.2,5.2L10.9,9l-3.8,3.8V5.2H7.2z"></path></g></svg></span></span></button><span class="jp-extensionmanager-headerTextDisabled">Discover</span></header><div class="bp3-collapse"><div class="bp3-collapse-body" aria-hidden="false"></div></div></div></div><div class="lm-Widget p-Widget jp-FileBrowser lm-StackedPanel-child p-StackedPanel-child" id="filebrowser" style="position: absolute; z-index: 0; top: 0px; left: 0px; width: 418px; height: 989px;"><div class="lm-Widget p-Widget jp-Toolbar jp-scrollbar-tiny jp-FileBrowser-toolbar" style="min-height: var(--jp-private-toolbar-height);"><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="New Launcher"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:add"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="New Folder"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:new-folder"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M20 6h-8l-2-2H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-1 8h-3v3h-2v-3h-3v-2h3V9h2v3h3v2z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-id-upload jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Upload Files"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:file-upload"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M9 16h6v-6h4l-7-7-7 7h4zm-4 2h14v2H5z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Refresh File List"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:refresh"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M9 13.5c-2.49 0-4.5-2.01-4.5-4.5S6.51 4.5 9 4.5c1.24 0 2.36.52 3.17 1.33L10 8h5V3l-1.76 1.76C12.15 3.68 10.66 3 9 3 5.69 3 3.01 5.69 3.01 9S5.69 15 9 15c2.97 0 5.43-2.16 5.9-5h-1.52c-.46 2-2.24 3.5-4.38 3.5z"></path></g></svg></span></span></button></div></div><div class="lm-Widget p-Widget jp-BreadCrumbs jp-FileBrowser-crumbs"><span title="C:/Users/Khaled" class="jp-BreadCrumbs-home f9v3xdu"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:folder" data-icon-id="70e74f7c-f391-4c07-844e-ee10a7fdedf0"><path class="jp-icon3 jp-icon-selectable" fill="#616161" d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"></path></svg></span><span>/</span><span class="jp-BreadCrumbs-item" title="Desktop">Desktop</span><span>/</span><span class="jp-BreadCrumbs-item" title="Desktop/python">python</span><span>/</span></div><div tabindex="1" class="lm-Widget p-Widget jp-DirListing jp-FileBrowser-listing jp-mod-selected"><div class="jp-DirListing-header"><div class="jp-DirListing-headerItem jp-id-name jp-mod-selected jp-mod-descending"><span class="jp-DirListing-headerItemText">Name</span><span class="jp-DirListing-headerItemIcon fllbajr"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-down" data-icon-id="b059fbe7-0cc6-41e5-8100-b6db7427204e"><g class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M5.2,7.5L9,11.2l3.8-3.8H5.2z"></path></g></svg></span></div><div class="jp-DirListing-headerItem jp-id-modified"><span class="jp-DirListing-headerItemText">Last Modified</span><span class="jp-DirListing-headerItemIcon"></span></div></div><ul class="jp-DirListing-content"><li class="jp-DirListing-item" title="Name: asssignment1.py_files
Path: Desktop/python
Created: 2021-01-08 13:29:35
Modified: 2021-01-08 13:29:35
Writable: true" data-file-type="directory" data-isdir="true"><span class="jp-DirListing-itemIcon fm5u5yq"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:folder" data-icon-id="70e74f7c-f391-4c07-844e-ee10a7fdedf0"><path class="jp-icon3 jp-icon-selectable" fill="#616161" d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"></path></svg></span><span class="jp-DirListing-itemText">asssignment1.py_files</span><span class="jp-DirListing-itemModified" title="Jan 8, 2021 1:29 PM">7 minutes ago</span></li><li class="jp-DirListing-item jp-mod-selected jp-mod-running" title="Name: Untitled.ipynb
Size: 1.8 KB
Path: Desktop/python
Created: 2021-01-08 13:35:06
Modified: 2021-01-08 13:36:02
Writable: true
Kernel: Python 3" data-file-type="notebook" data-isdir="false"><span class="jp-DirListing-itemIcon fm5u5yq"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:notebook" data-icon-id="3d88fa5d-d794-4476-be84-690c3938827f"><g class="jp-icon-warn0 jp-icon-selectable" fill="#EF6C00"><path d="M18.7 3.3v15.4H3.3V3.3h15.4m1.5-1.5H1.8v18.3h18.3l.1-18.3z"></path><path d="M16.5 16.5l-5.4-4.3-5.6 4.3v-11h11z"></path></g></svg></span><span class="jp-DirListing-itemText">Untitled.ipynb</span><span class="jp-DirListing-itemModified" title="Jan 8, 2021 1:36 PM">seconds ago</span></li><li class="jp-DirListing-item" title="Name: test.py
Size: 54 Bytes
Path: Desktop/python
Created: 2021-01-07 18:29:51
Modified: 2021-01-07 18:29:51
Writable: true" data-file-type="python" data-isdir="false"><span class="jp-DirListing-itemIcon fm5u5yq"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:python" data-icon-id="843be2cc-fd63-458e-ae9d-09193c83b8db"><g class="jp-icon-brand0 jp-icon-selectable" fill="#0D47A1"><path d="M11.1 6.9V5.8H6.9c0-.5 0-1.3.2-1.6.4-.7.8-1.1 1.7-1.4 1.7-.3 2.5-.3 3.9-.1 1 .1 1.9.9 1.9 1.9v4.2c0 .5-.9 1.6-2 1.6H8.8c-1.5 0-2.4 1.4-2.4 2.8v2.2H4.7C3.5 15.1 3 14 3 13.1V9c-.1-1 .6-2 1.8-2 1.5-.1 6.3-.1 6.3-.1z"></path><path d="M10.9 15.1v1.1h4.2c0 .5 0 1.3-.2 1.6-.4.7-.8 1.1-1.7 1.4-1.7.3-2.5.3-3.9.1-1-.1-1.9-.9-1.9-1.9v-4.2c0-.5.9-1.6 2-1.6h3.8c1.5 0 2.4-1.4 2.4-2.8V6.6h1.7C18.5 6.9 19 8 19 8.9V13c0 1-.7 2.1-1.9 2.1h-6.2z"></path></g></svg></span><span class="jp-DirListing-itemText">test.py</span><span class="jp-DirListing-itemModified" title="Jan 7, 2021 6:29 PM">19 hours ago</span></li><li class="jp-DirListing-item" title="Name: asssignment1.py.html
Size: 882.6 KB
Path: Desktop/python
Created: 2021-01-08 13:29:35
Modified: 2021-01-08 13:29:35
Writable: true" data-file-type="html" data-isdir="false"><span class="jp-DirListing-itemIcon fm5u5yq"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 512 512" data-icon="ui-components:html5" data-icon-id="e4ae904e-ef9c-416c-a701-0d5a7a5e0d20"><path class="jp-icon0 jp-icon-selectable" fill="#000" d="M108.4 0h23v22.8h21.2V0h23v69h-23V46h-21v23h-23.2M206 23h-20.3V0h63.7v23H229v46h-23m53.5-69h24.1l14.8 24.3L313.2 0h24.1v69h-23V34.8l-16.1 24.8-16.1-24.8V69h-22.6m89.2-69h23v46.2h32.6V69h-55.6"></path><path class="jp-icon-selectable" fill="#e44d26" d="M107.6 471l-33-370.4h362.8l-33 370.2L255.7 512"></path><path class="jp-icon-selectable" fill="#f16529" d="M256 480.5V131h148.3L376 447"></path><path class="jp-icon-selectable-inverse" fill="#ebebeb" d="M142 176.3h114v45.4h-64.2l4.2 46.5h60v45.3H154.4m2 22.8H202l3.2 36.3 50.8 13.6v47.4l-93.2-26"></path><path class="jp-icon-selectable-inverse" fill="#fff" d="M369.6 176.3H255.8v45.4h109.6m-4.1 46.5H255.8v45.4h56l-5.3 59-50.7 13.6v47.2l93-25.8"></path></svg></span><span class="jp-DirListing-itemText">asssignment1.py.html</span><span class="jp-DirListing-itemModified" title="Jan 8, 2021 1:29 PM">7 minutes ago</span></li></ul></div></div></div><div class="lm-SplitPanel-handle p-SplitPanel-handle" style="position: absolute; top: 0px; left: 419.333px; width: 1px; height: 989px;"></div><div class="lm-Widget p-Widget lm-DockPanel p-DockPanel lm-SplitPanel-child p-SplitPanel-child" data-mode="multiple-document" id="jp-main-dock-panel" style="position: absolute; top: 0px; left: 420.333px; width: 1466.67px; height: 989px; min-width: 12px; min-height: 66px;"><div class="lm-DockPanel-overlay lm-mod-hidden p-DockPanel-overlay p-mod-hidden" style="position: absolute;"></div><div class="lm-Widget p-Widget lm-TabBar p-TabBar lm-DockPanel-tabBar jp-Activity" data-orientation="horizontal" style="position: absolute; top: 5px; left: 5px; width: 1457px; height: 26px;"><ul class="lm-TabBar-content p-TabBar-content"><li title="" class="lm-TabBar-tab p-TabBar-tab        lm-mod-closable p-mod-closable" data-id="launcher-0" style="z-index: 1;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon fix2bjg"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:launcher" data-icon-id="94409f6a-2330-4c66-b90d-cf2e788d65d4"><path class="jp-icon3 jp-icon-selectable" fill="#616161" d="M19 19H5V5h7V3H5a2 2 0 00-2 2v14a2 2 0 002 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel">Launcher</div><div class="jp-icon-hover lm-TabBar-tabCloseIcon fvaq30"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:close" data-icon-id="4505d2c6-1a49-487e-a8cd-1b14d350bc4e"><g class="jp-icon-none jp-icon-selectable-inverse jp-icon3-hover" fill="none"><circle cx="12" cy="12" r="11"></circle></g><g class="jp-icon3 jp-icon-selectable jp-icon-accent2-hover" fill="#616161"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g><g class="jp-icon-none jp-icon-busy" fill="none"><circle cx="12" cy="12" r="7"></circle></g></svg></div></li><li title="Name: Untitled.ipynb
Path: Desktop/python/Untitled.ipynb
Last Saved: 2021-01-08 13:36
Last Checkpoint: 2021-01-08 13:35" class="lm-TabBar-tab p-TabBar-tab   jp-mod-current        jp-mod-active lm-mod-closable p-mod-closable lm-mod-current p-mod-current" data-type="document-title" data-id="id-f8e6f125-2161-4a87-b0c3-7943859df25c" style="z-index: 2;"><div class="lm-TabBar-tabIcon p-TabBar-tabIcon fix2bjg"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:notebook" data-icon-id="3d88fa5d-d794-4476-be84-690c3938827f"><g class="jp-icon-warn0 jp-icon-selectable" fill="#EF6C00"><path d="M18.7 3.3v15.4H3.3V3.3h15.4m1.5-1.5H1.8v18.3h18.3l.1-18.3z"></path><path d="M16.5 16.5l-5.4-4.3-5.6 4.3v-11h11z"></path></g></svg></div><div class="lm-TabBar-tabLabel p-TabBar-tabLabel">Untitled.ipynb</div><div class="jp-icon-hover lm-TabBar-tabCloseIcon fvaq30"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:close" data-icon-id="4505d2c6-1a49-487e-a8cd-1b14d350bc4e"><g class="jp-icon-none jp-icon-selectable-inverse jp-icon3-hover" fill="none"><circle cx="12" cy="12" r="11"></circle></g><g class="jp-icon3 jp-icon-selectable jp-icon-accent2-hover" fill="#616161"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g><g class="jp-icon-none jp-icon-busy" fill="none"><circle cx="12" cy="12" r="7"></circle></g></svg></div></li></ul></div><div class="lm-Widget p-Widget jp-MainAreaWidget jp-Activity lm-DockPanel-widget p-DockPanel-widget lm-mod-hidden p-mod-hidden" id="launcher-0" data-direction="top-to-bottom" data-alignment="start" style="position: absolute; min-width: 122px; min-height: 129px; top: 31px; left: 5px; width: 1457px; height: 953px;"><div class="lm-Widget p-Widget jp-Toolbar jp-scrollbar-tiny" style="position: absolute; top: 0px; left: 0px; width: 1455px; height: 8px;"></div><div class="lm-Widget p-Widget jp-Launcher" id="id-de2ddb58-250b-4118-ab52-fb3487ef1678" tabindex="-1" style="position: absolute; top: 8px; left: 0px; width: 1455px; height: 944px;"><div class="jp-Launcher-body"><div class="jp-Launcher-content"><div class="jp-Launcher-cwd"><h3>Desktop/python</h3></div><div class="jp-Launcher-section"><div class="jp-Launcher-sectionHeader"><div class="f1hgkb35"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:notebook"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-warn0 jp-icon-selectable" fill="#EF6C00"><path d="M18.7 3.3v15.4H3.3V3.3h15.4m1.5-1.5H1.8v18.3h18.3l.1-18.3z"></path><path d="M16.5 16.5l-5.4-4.3-5.6 4.3v-11h11z"></path></g></svg></div><h2 class="jp-Launcher-sectionTitle">Notebook</h2></div><div class="jp-Launcher-cardContainer"><div class="jp-LauncherCard" title="Python 3" tabindex="100" data-category="Notebook"><div class="jp-LauncherCard-icon"><img src="./asssignment01_files/logo-64x64.png" class="jp-Launcher-kernelIcon"></div><div class="jp-LauncherCard-label" title="Python 3"><p>Python 3</p></div></div></div></div><div class="jp-Launcher-section"><div class="jp-Launcher-sectionHeader"><div class="f1hgkb35"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 200 200" data-icon="ui-components:console"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-brand1 jp-icon-selectable" fill="#0288D1"><path d="M20 19.8h160v159.9H20z"></path></g><g xmlns="http://www.w3.org/2000/svg" class="jp-icon-selectable-inverse" fill="#fff"><path d="M105 127.3h40v12.8h-40zM51.1 77L74 99.9l-23.3 23.3 10.5 10.5 23.3-23.3L95 99.9 84.5 89.4 61.6 66.5z"></path></g></svg></div><h2 class="jp-Launcher-sectionTitle">Console</h2></div><div class="jp-Launcher-cardContainer"><div class="jp-LauncherCard" title="Python 3" tabindex="100" data-category="Console"><div class="jp-LauncherCard-icon"><img src="./asssignment01_files/logo-64x64.png" class="jp-Launcher-kernelIcon"></div><div class="jp-LauncherCard-label" title="Python 3"><p>Python 3</p></div></div></div></div><div class="jp-Launcher-section"><div class="jp-Launcher-sectionHeader"><div class="f1hgkb35"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:terminal"><rect xmlns="http://www.w3.org/2000/svg" class="jp-icon2 jp-icon-selectable" width="20" height="20" transform="translate(2 2)" fill="#333333"></rect><path xmlns="http://www.w3.org/2000/svg" class="jp-icon-accent2 jp-icon-selectable-inverse" d="M5.05664 8.76172C5.05664 8.59766 5.03125 8.45312 4.98047 8.32812C4.93359 8.19922 4.85547 8.08203 4.74609 7.97656C4.64062 7.87109 4.5 7.77539 4.32422 7.68945C4.15234 7.59961 3.94336 7.51172 3.69727 7.42578C3.30273 7.28516 2.94336 7.13672 2.61914 6.98047C2.29492 6.82422 2.01758 6.64258 1.78711 6.43555C1.56055 6.22852 1.38477 5.98828 1.25977 5.71484C1.13477 5.4375 1.07227 5.10938 1.07227 4.73047C1.07227 4.39844 1.12891 4.0957 1.24219 3.82227C1.35547 3.54492 1.51562 3.30469 1.72266 3.10156C1.92969 2.89844 2.17969 2.73437 2.47266 2.60938C2.76562 2.48438 3.0918 2.4043 3.45117 2.36914V1.10938H4.38867V2.38086C4.74023 2.42773 5.05664 2.52344 5.33789 2.66797C5.61914 2.8125 5.85742 3.00195 6.05273 3.23633C6.25195 3.4668 6.4043 3.74023 6.50977 4.05664C6.61914 4.36914 6.67383 4.7207 6.67383 5.11133H5.04492C5.04492 4.63867 4.9375 4.28125 4.72266 4.03906C4.50781 3.79297 4.2168 3.66992 3.84961 3.66992C3.65039 3.66992 3.47656 3.69727 3.32812 3.75195C3.18359 3.80273 3.06445 3.87695 2.9707 3.97461C2.87695 4.06836 2.80664 4.17969 2.75977 4.30859C2.7168 4.4375 2.69531 4.57812 2.69531 4.73047C2.69531 4.88281 2.7168 5.01953 2.75977 5.14062C2.80664 5.25781 2.88281 5.36719 2.98828 5.46875C3.09766 5.57031 3.24023 5.66797 3.41602 5.76172C3.5918 5.85156 3.81055 5.94336 4.07227 6.03711C4.4668 6.18555 4.82422 6.33984 5.14453 6.5C5.46484 6.65625 5.73828 6.83984 5.96484 7.05078C6.19531 7.25781 6.37109 7.5 6.49219 7.77734C6.61719 8.05078 6.67969 8.375 6.67969 8.75C6.67969 9.09375 6.62305 9.4043 6.50977 9.68164C6.39648 9.95508 6.23438 10.1914 6.02344 10.3906C5.8125 10.5898 5.55859 10.75 5.26172 10.8711C4.96484 10.9883 4.63281 11.0645 4.26562 11.0996V12.248H3.33398V11.0996C3.00195 11.0684 2.67969 10.9961 2.36719 10.8828C2.05469 10.7656 1.77734 10.5977 1.53516 10.3789C1.29688 10.1602 1.10547 9.88477 0.960938 9.55273C0.816406 9.2168 0.744141 8.81445 0.744141 8.3457H2.37891C2.37891 8.62695 2.41992 8.86328 2.50195 9.05469C2.58398 9.24219 2.68945 9.39258 2.81836 9.50586C2.95117 9.61523 3.10156 9.69336 3.26953 9.74023C3.4375 9.78711 3.60938 9.81055 3.78516 9.81055C4.20312 9.81055 4.51953 9.71289 4.73438 9.51758C4.94922 9.32227 5.05664 9.07031 5.05664 8.76172ZM13.418 12.2715H8.07422V11H13.418V12.2715Z" transform="translate(3.95264 6)" fill="white"></path></svg></div><h2 class="jp-Launcher-sectionTitle">Other</h2></div><div class="jp-Launcher-cardContainer"><div class="jp-LauncherCard" title="Start a new terminal session" tabindex="100" data-category="Other"><div class="jp-LauncherCard-icon"><div class="f187g4yd"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:terminal"><rect xmlns="http://www.w3.org/2000/svg" class="jp-icon2 jp-icon-selectable" width="20" height="20" transform="translate(2 2)" fill="#333333"></rect><path xmlns="http://www.w3.org/2000/svg" class="jp-icon-accent2 jp-icon-selectable-inverse" d="M5.05664 8.76172C5.05664 8.59766 5.03125 8.45312 4.98047 8.32812C4.93359 8.19922 4.85547 8.08203 4.74609 7.97656C4.64062 7.87109 4.5 7.77539 4.32422 7.68945C4.15234 7.59961 3.94336 7.51172 3.69727 7.42578C3.30273 7.28516 2.94336 7.13672 2.61914 6.98047C2.29492 6.82422 2.01758 6.64258 1.78711 6.43555C1.56055 6.22852 1.38477 5.98828 1.25977 5.71484C1.13477 5.4375 1.07227 5.10938 1.07227 4.73047C1.07227 4.39844 1.12891 4.0957 1.24219 3.82227C1.35547 3.54492 1.51562 3.30469 1.72266 3.10156C1.92969 2.89844 2.17969 2.73437 2.47266 2.60938C2.76562 2.48438 3.0918 2.4043 3.45117 2.36914V1.10938H4.38867V2.38086C4.74023 2.42773 5.05664 2.52344 5.33789 2.66797C5.61914 2.8125 5.85742 3.00195 6.05273 3.23633C6.25195 3.4668 6.4043 3.74023 6.50977 4.05664C6.61914 4.36914 6.67383 4.7207 6.67383 5.11133H5.04492C5.04492 4.63867 4.9375 4.28125 4.72266 4.03906C4.50781 3.79297 4.2168 3.66992 3.84961 3.66992C3.65039 3.66992 3.47656 3.69727 3.32812 3.75195C3.18359 3.80273 3.06445 3.87695 2.9707 3.97461C2.87695 4.06836 2.80664 4.17969 2.75977 4.30859C2.7168 4.4375 2.69531 4.57812 2.69531 4.73047C2.69531 4.88281 2.7168 5.01953 2.75977 5.14062C2.80664 5.25781 2.88281 5.36719 2.98828 5.46875C3.09766 5.57031 3.24023 5.66797 3.41602 5.76172C3.5918 5.85156 3.81055 5.94336 4.07227 6.03711C4.4668 6.18555 4.82422 6.33984 5.14453 6.5C5.46484 6.65625 5.73828 6.83984 5.96484 7.05078C6.19531 7.25781 6.37109 7.5 6.49219 7.77734C6.61719 8.05078 6.67969 8.375 6.67969 8.75C6.67969 9.09375 6.62305 9.4043 6.50977 9.68164C6.39648 9.95508 6.23438 10.1914 6.02344 10.3906C5.8125 10.5898 5.55859 10.75 5.26172 10.8711C4.96484 10.9883 4.63281 11.0645 4.26562 11.0996V12.248H3.33398V11.0996C3.00195 11.0684 2.67969 10.9961 2.36719 10.8828C2.05469 10.7656 1.77734 10.5977 1.53516 10.3789C1.29688 10.1602 1.10547 9.88477 0.960938 9.55273C0.816406 9.2168 0.744141 8.81445 0.744141 8.3457H2.37891C2.37891 8.62695 2.41992 8.86328 2.50195 9.05469C2.58398 9.24219 2.68945 9.39258 2.81836 9.50586C2.95117 9.61523 3.10156 9.69336 3.26953 9.74023C3.4375 9.78711 3.60938 9.81055 3.78516 9.81055C4.20312 9.81055 4.51953 9.71289 4.73438 9.51758C4.94922 9.32227 5.05664 9.07031 5.05664 8.76172ZM13.418 12.2715H8.07422V11H13.418V12.2715Z" transform="translate(3.95264 6)" fill="white"></path></svg></div></div><div class="jp-LauncherCard-label" title="Start a new terminal session"><p>Terminal</p></div></div><div class="jp-LauncherCard" title="Create a new text file" tabindex="100" data-category="Other"><div class="jp-LauncherCard-icon"><div class="f187g4yd"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:text-editor"><path xmlns="http://www.w3.org/2000/svg" class="jp-icon3 jp-icon-selectable" fill="#616161" d="M15 15H3v2h12v-2zm0-8H3v2h12V7zM3 13h18v-2H3v2zm0 8h18v-2H3v2zM3 3v2h18V3H3z"></path></svg></div></div><div class="jp-LauncherCard-label" title="Create a new text file"><p>Text File</p></div></div><div class="jp-LauncherCard" title="Create a new markdown file" tabindex="100" data-category="Other"><div class="jp-LauncherCard-icon"><div class="f187g4yd"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 22 22" data-icon="ui-components:markdown"><path xmlns="http://www.w3.org/2000/svg" class="jp-icon-contrast0 jp-icon-selectable" fill="#7B1FA2" d="M5 14.9h12l-6.1 6zm9.4-6.8c0-1.3-.1-2.9-.1-4.5-.4 1.4-.9 2.9-1.3 4.3l-1.3 4.3h-2L8.5 7.9c-.4-1.3-.7-2.9-1-4.3-.1 1.6-.1 3.2-.2 4.6L7 12.4H4.8l.7-11h3.3L10 5c.4 1.2.7 2.7 1 3.9.3-1.2.7-2.6 1-3.9l1.2-3.7h3.3l.6 11h-2.4l-.3-4.2z"></path></svg></div></div><div class="jp-LauncherCard-label" title="Create a new markdown file"><p>Markdown File</p></div></div><div class="jp-LauncherCard" title="Live updating code documentation from the active kernel" tabindex="100" data-category="Other"><div class="jp-LauncherCard-icon"><div class="f187g4yd"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:inspector"><path xmlns="http://www.w3.org/2000/svg" class="jp-icon3 jp-icon-selectable" fill="#616161" d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-5 14H4v-4h11v4zm0-5H4V9h11v4zm5 5h-4V9h4v9z"></path></svg></div></div><div class="jp-LauncherCard-label" title="Live updating code documentation from the active kernel"><p>Show Contextual Help</p></div></div></div></div></div></div></div></div><div class="lm-Widget p-Widget jp-MainAreaWidget jp-NotebookPanel jp-Document jp-Activity lm-DockPanel-widget p-DockPanel-widget jp-mod-searchable" id="id-f8e6f125-2161-4a87-b0c3-7943859df25c" data-direction="top-to-bottom" data-alignment="start" style="position: absolute; min-width: 2px; min-height: 30px; top: 31px; left: 5px; width: 1457px; height: 953px;"><div class="lm-Widget p-Widget jp-Toolbar jp-scrollbar-tiny jp-NotebookPanel-toolbar" style="position: absolute; top: 0px; left: 0px; width: 1455px; height: 29px; min-height: var(--jp-private-toolbar-height);"><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Save the notebook contents and create checkpoint"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24" data-icon="ui-components:save"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M17 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V7l-4-4zm-5 16c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-10H5V5h10v4z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Insert a cell below"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:add"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Cut the selected cells"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" data-icon="ui-components:cut"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M9.64 7.64c.23-.5.36-1.05.36-1.64 0-2.21-1.79-4-4-4S2 3.79 2 6s1.79 4 4 4c.59 0 1.14-.13 1.64-.36L10 12l-2.36 2.36C7.14 14.13 6.59 14 6 14c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4c0-.59-.13-1.14-.36-1.64L12 14l7 7h3v-1L9.64 7.64zM6 8c-1.1 0-2-.89-2-2s.9-2 2-2 2 .89 2 2-.9 2-2 2zm0 12c-1.1 0-2-.89-2-2s.9-2 2-2 2 .89 2 2-.9 2-2 2zm6-7.5c-.28 0-.5-.22-.5-.5s.22-.5.5-.5.5.22.5.5-.22.5-.5.5zM19 3l-6 6 2 2 7-7V3z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Copy the selected cells"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" width="16" data-icon="ui-components:copy"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M11.9,1H3.2C2.4,1,1.7,1.7,1.7,2.5v10.2h1.5V2.5h8.7V1z M14.1,3.9h-8c-0.8,0-1.5,0.7-1.5,1.5v10.2c0,0.8,0.7,1.5,1.5,1.5h8 c0.8,0,1.5-0.7,1.5-1.5V5.4C15.5,4.6,14.9,3.9,14.1,3.9z M14.1,15.5h-8V5.4h8V15.5z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Paste cells from the clipboard"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24" data-icon="ui-components:paste"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M19 2h-4.18C14.4.84 13.3 0 12 0c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm7 18H5V4h2v3h10V4h2v16z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Run the selected cells and advance"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24" data-icon="ui-components:run"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M8 5v14l11-7z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Interrupt the kernel"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24" data-icon="ui-components:stop"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M0 0h24v24H0z" fill="none"></path><path d="M6 6h12v12H6z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Restart the kernel"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:refresh"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M9 13.5c-2.49 0-4.5-2.01-4.5-4.5S6.51 4.5 9 4.5c1.24 0 2.36.52 3.17 1.33L10 8h5V3l-1.76 1.76C12.15 3.68 10.66 3 9 3 5.69 3 3.01 5.69 3.01 9S5.69 15 9 15c2.97 0 5.43-2.16 5.9-5h-1.52c-.46 2-2.24 3.5-4.38 3.5z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-ToolbarButton jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-ToolbarButtonComponent minimal jp-Button" title="Restart the kernel, then re-run the whole notebook"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-icon f1xliy8o"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-icon="ui-components:fast-forward"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161"><path d="M4 18l8.5-6L4 6v12zm9-12v12l8.5-6L13 6z"></path></g></svg></span></span></button></div><div class="lm-Widget p-Widget jp-Notebook-toolbarCellType jp-Toolbar-item"><div class="jp-HTMLSelect jp-DefaultStyle jp-Notebook-toolbarCellTypeDropdown"><select aria-label="Cell type"><option value="-">-</option><option value="code">Code</option><option value="markdown">Markdown</option><option value="raw">Raw</option></select><span class="f1ozlkqi"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 18 18" data-icon="ui-components:caret-down-empty"><g xmlns="http://www.w3.org/2000/svg" class="jp-icon3" fill="#616161" shape-rendering="geometricPrecision"><path d="M5.2,5.9L9,9.7l3.8-3.8l1.2,1.2l-4.9,5l-4.9-5L5.2,5.9z"></path></g></svg></span></div></div><div class="lm-Widget p-Widget jp-Toolbar-spacer jp-Toolbar-item"></div><div class="lm-Widget p-Widget jp-KernelName jp-Toolbar-item"><button type="button" class="bp3-button bp3-minimal jp-Toolbar-kernelName jp-ToolbarButtonComponent minimal jp-Button" title="Switch kernel"><span class="bp3-button-text"><span class="jp-ToolbarButtonComponent-label">Python 3</span></span></button></div><div class="lm-Widget p-Widget jp-Toolbar-kernelStatus f14jk5uf jp-Toolbar-item" title="Kernel Idle"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:circle-empty" data-icon-id="2b5522e9-b15f-45a6-9f50-0be4f64350d7"><g class="jp-icon3" fill="#616161"><path d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></g></svg></div></div><div class="lm-Widget p-Widget jp-Notebook jp-mod-scrollPastEnd jp-NotebookPanel-notebook jp-mod-commandMode" data-jp-kernel-user="true" data-jp-undoer="true" tabindex="-1" data-lm-dragscroll="true" id="id-68b0568d-a47d-45eb-8ee6-de86e0b70ccc" style="position: absolute; top: 29px; left: 0px; width: 1455px; height: 923px;" data-jp-code-runner="true"><div class="lm-Widget p-Widget jp-Cell jp-CodeCell jp-Notebook-cell"><div class="lm-Widget p-Widget jp-CellHeader jp-Cell-header"></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-Cell-inputWrapper"><div class="lm-Widget p-Widget jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"><div class="jp-Collapser-child"></div></div><div class="lm-Widget p-Widget jp-InputArea jp-Cell-inputArea"><div class="lm-Widget p-Widget jp-InputPrompt jp-InputArea-prompt">[1]:</div><div class="lm-Widget p-Widget jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline"><div class="CodeMirror cm-s-jupyter"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 22px; left: 175.609px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 285.828px; margin-bottom: -17px; border-right-width: 13px; min-height: 44px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 175.609px; top: 17px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">name</span> <span class="cm-operator">=</span> <span class="cm-builtin">input</span>(<span class="cm-builtin">print</span>(<span class="cm-string">"Enter your name "</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span> <span class=" CodeMirror-matchingbracket">(</span><span class="cm-string">"Welcome "</span>,<span class="cm-variable">name</span> <span class=" CodeMirror-matchingbracket">)</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 44px;"></div><div class="CodeMirror-gutters" style="display: none; height: 57px;"></div></div></div></div></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-Cell-outputWrapper"><div class="lm-Widget p-Widget jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"><div class="jp-Collapser-child"></div></div><div class="lm-Widget p-Widget jp-OutputArea jp-Cell-outputArea"><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>Enter your name 
</pre></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>None khaled
</pre></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>Welcome  khaled
</pre></div></div></div></div><div class="lm-Widget p-Widget jp-CellFooter jp-Cell-footer"></div></div><div class="lm-Widget p-Widget jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-active jp-mod-selected"><div class="lm-Widget p-Widget jp-CellHeader jp-Cell-header"></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-Cell-inputWrapper"><div class="lm-Widget p-Widget jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"><div class="jp-Collapser-child"></div></div><div class="lm-Widget p-Widget jp-InputArea jp-Cell-inputArea"><div class="lm-Widget p-Widget jp-InputPrompt jp-InputArea-prompt">[2]:</div><div class="lm-Widget p-Widget jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline"><div class="CodeMirror cm-s-jupyter"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 414.5px; margin-bottom: -17px; border-right-width: 13px; min-height: 78px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">num1</span><span class="cm-operator">=</span> <span class="cm-builtin">float</span> (<span class="cm-builtin">input</span> (<span class="cm-builtin">print</span>(<span class="cm-string">"Enter your first number: "</span>)))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">num2</span><span class="cm-operator">=</span> <span class="cm-builtin">float</span> (<span class="cm-builtin">input</span> (<span class="cm-builtin">print</span>(<span class="cm-string">"Enter your second number: "</span>)))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">eq</span> <span class="cm-operator">=</span> <span class="cm-variable">num1</span><span class="cm-operator">+</span><span class="cm-variable">num2</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span> (<span class="cm-variable">eq</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 78px;"></div><div class="CodeMirror-gutters" style="display: none; height: 91px;"></div></div></div></div></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-Cell-outputWrapper"><div class="lm-Widget p-Widget jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"><div class="jp-Collapser-child"></div></div><div class="lm-Widget p-Widget jp-OutputArea jp-Cell-outputArea"><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>Enter your first number: 
</pre></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>None 4.2
</pre></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>Enter your second number: 
</pre></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>None 3.8
</pre></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel jp-OutputArea-child"><div class="lm-Widget p-Widget jp-OutputPrompt jp-OutputArea-prompt"></div><div class="lm-Widget p-Widget jp-RenderedText jp-mod-trusted jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stdout"><pre>8.0
</pre></div></div></div></div><div class="lm-Widget p-Widget jp-CellFooter jp-Cell-footer"></div></div></div></div></div><div class="lm-SplitPanel-handle p-SplitPanel-handle lm-mod-hidden p-mod-hidden" style="position: absolute; top: 0px; left: 1887px; width: 1px; height: 989px;"></div><div class="lm-Widget p-Widget lm-Panel p-Panel lm-StackedPanel p-StackedPanel lm-mod-hidden p-mod-hidden lm-SplitPanel-child p-SplitPanel-child" id="jp-right-stack" style="position: absolute; min-width: 1px; min-height: 0px;"></div><div class="lm-SplitPanel-handle p-SplitPanel-handle lm-mod-hidden p-mod-hidden" style="position: absolute;"></div></div><div class="lm-Widget p-Widget lm-TabBar p-TabBar lm-mod-hidden p-mod-hidden jp-SideBar jp-mod-right lm-BoxPanel-child p-BoxPanel-child" data-orientation="horizontal" style="position: absolute;"><ul class="lm-TabBar-content p-TabBar-content"></ul></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel lm-BoxPanel p-BoxPanel" data-direction="bottom-to-top" data-alignment="start" id="jp-bottom-panel" style="position: absolute; top: 1017px; left: 0px; width: 1920px; height: 24px; min-width: 0px; min-height: 24px;"><div class="lm-Widget p-Widget f17wptjy lm-BoxPanel-child p-BoxPanel-child" id="jp-main-statusbar" style="position: absolute; top: 0px; left: 0px; width: 1920px; height: 24px;"><div class="lm-Widget p-Widget lm-Panel p-Panel fddsvlq fy1visq"><div class="lm-Widget p-Widget fwgmxe9 f1ydny4p"><div class="f2s1awa"><div style="margin-right: 4px;"><div class="f2s1awa"><div style="margin-right: 4px;"><span class="f1235lqo">1</span></div><div style="margin-left: 4px;"><div class="f1q2iu0g"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:terminal"><rect xmlns="http://www.w3.org/2000/svg" class="jp-icon2 jp-icon-selectable" width="20" height="20" transform="translate(2 2)" fill="#333333"></rect><path xmlns="http://www.w3.org/2000/svg" class="jp-icon-accent2 jp-icon-selectable-inverse" d="M5.05664 8.76172C5.05664 8.59766 5.03125 8.45312 4.98047 8.32812C4.93359 8.19922 4.85547 8.08203 4.74609 7.97656C4.64062 7.87109 4.5 7.77539 4.32422 7.68945C4.15234 7.59961 3.94336 7.51172 3.69727 7.42578C3.30273 7.28516 2.94336 7.13672 2.61914 6.98047C2.29492 6.82422 2.01758 6.64258 1.78711 6.43555C1.56055 6.22852 1.38477 5.98828 1.25977 5.71484C1.13477 5.4375 1.07227 5.10938 1.07227 4.73047C1.07227 4.39844 1.12891 4.0957 1.24219 3.82227C1.35547 3.54492 1.51562 3.30469 1.72266 3.10156C1.92969 2.89844 2.17969 2.73437 2.47266 2.60938C2.76562 2.48438 3.0918 2.4043 3.45117 2.36914V1.10938H4.38867V2.38086C4.74023 2.42773 5.05664 2.52344 5.33789 2.66797C5.61914 2.8125 5.85742 3.00195 6.05273 3.23633C6.25195 3.4668 6.4043 3.74023 6.50977 4.05664C6.61914 4.36914 6.67383 4.7207 6.67383 5.11133H5.04492C5.04492 4.63867 4.9375 4.28125 4.72266 4.03906C4.50781 3.79297 4.2168 3.66992 3.84961 3.66992C3.65039 3.66992 3.47656 3.69727 3.32812 3.75195C3.18359 3.80273 3.06445 3.87695 2.9707 3.97461C2.87695 4.06836 2.80664 4.17969 2.75977 4.30859C2.7168 4.4375 2.69531 4.57812 2.69531 4.73047C2.69531 4.88281 2.7168 5.01953 2.75977 5.14062C2.80664 5.25781 2.88281 5.36719 2.98828 5.46875C3.09766 5.57031 3.24023 5.66797 3.41602 5.76172C3.5918 5.85156 3.81055 5.94336 4.07227 6.03711C4.4668 6.18555 4.82422 6.33984 5.14453 6.5C5.46484 6.65625 5.73828 6.83984 5.96484 7.05078C6.19531 7.25781 6.37109 7.5 6.49219 7.77734C6.61719 8.05078 6.67969 8.375 6.67969 8.75C6.67969 9.09375 6.62305 9.4043 6.50977 9.68164C6.39648 9.95508 6.23438 10.1914 6.02344 10.3906C5.8125 10.5898 5.55859 10.75 5.26172 10.8711C4.96484 10.9883 4.63281 11.0645 4.26562 11.0996V12.248H3.33398V11.0996C3.00195 11.0684 2.67969 10.9961 2.36719 10.8828C2.05469 10.7656 1.77734 10.5977 1.53516 10.3789C1.29688 10.1602 1.10547 9.88477 0.960938 9.55273C0.816406 9.2168 0.744141 8.81445 0.744141 8.3457H2.37891C2.37891 8.62695 2.41992 8.86328 2.50195 9.05469C2.58398 9.24219 2.68945 9.39258 2.81836 9.50586C2.95117 9.61523 3.10156 9.69336 3.26953 9.74023C3.4375 9.78711 3.60938 9.81055 3.78516 9.81055C4.20312 9.81055 4.51953 9.71289 4.73438 9.51758C4.94922 9.32227 5.05664 9.07031 5.05664 8.76172ZM13.418 12.2715H8.07422V11H13.418V12.2715Z" transform="translate(3.95264 6)" fill="white"></path></svg></div></div></div></div><div style="margin-left: 4px;"><div class="f2s1awa"><div style="margin-right: 4px;"><span class="f1235lqo">2</span></div><div style="margin-left: 4px;"><div class="f1m7xje8"><svg xmlns="http://www.w3.org/2000/svg" width="16" viewBox="0 0 24 24" data-icon="ui-components:kernel"><path xmlns="http://www.w3.org/2000/svg" class="jp-icon2" fill="#616161" d="M15 9H9v6h6V9zm-2 4h-2v-2h2v2zm8-2V9h-2V7c0-1.1-.9-2-2-2h-2V3h-2v2h-2V3H9v2H7c-1.1 0-2 .9-2 2v2H3v2h2v2H3v2h2v2c0 1.1.9 2 2 2h2v2h2v-2h2v2h2v-2h2c1.1 0 2-.9 2-2v-2h2v-2h-2v-2h2zm-4 6H7V7h10v10z"></path></svg></div></div></div></div></div></div><div class="lm-Widget p-Widget fwgmxe9 jp-LogConsoleStatusItem f1ydny4p lm-mod-hidden p-mod-hidden"></div><div class="lm-Widget p-Widget fwgmxe9 f1ydny4p lm-mod-hidden p-mod-hidden"><span class="f1235lqo"></span></div><div class="lm-Widget p-Widget fwgmxe9 f1ydny4p"><span class="f1235lqo" title="Change kernel for Untitled.ipynb">Python 3 | Idle</span></div><div class="lm-Widget p-Widget f1ydny4p lm-mod-hidden p-mod-hidden"><span class="f1235lqo" title="Current mem usage">Mem: 0.00 B</span></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel fddsvlq"><div class="lm-Widget p-Widget f1ydny4p"><span class="f1235lqo">Saving completed</span></div><div class="lm-Widget p-Widget f1ydny4p lm-mod-hidden p-mod-hidden"><div class="f2s1awa"><div style="margin-right: 4px;"><span class="f1235lqo">Uploading…</span></div><div style="margin-left: 4px;"><div class="fwu96q8"><div class="fgn7udo" style="width: 100px;"></div></div></div></div></div></div><div class="lm-Widget p-Widget lm-Panel p-Panel fddsvlq f1fwtl1j"><div class="lm-Widget p-Widget f1ydny4p" title=""><span class="f1235lqo" title="Desktop/python/Untitled.ipynb">Untitled.ipynb</span></div><div class="lm-Widget p-Widget fwgmxe9 f1ydny4p lm-mod-hidden p-mod-hidden"><span class="f1235lqo" title="Change Tab indentation…">Spaces: 4</span></div><div class="lm-Widget p-Widget fwgmxe9 f1ydny4p"><span class="f1235lqo" title="Go to line number…">Ln 1, Col 1</span></div><div class="lm-Widget p-Widget f1ydny4p" title="Notebook trusted: 2 of 2 cells trusted."><div><div class="f1m7xje8"><svg xmlns="http://www.w3.org/2000/svg" fill="none" width="16" viewBox="0 0 24 25" data-icon="ui-components:trusted"><path xmlns="http://www.w3.org/2000/svg" class="jp-icon2" stroke="#333333" stroke-width="2" transform="translate(2 3)" d="M1.86094 11.4409C0.826448 8.77027 0.863779 6.05764 1.24907 4.19932C2.48206 3.93347 4.08068 3.40347 5.60102 2.8449C7.23549 2.2444 8.85666 1.5815 9.9876 1.09539C11.0597 1.58341 12.6094 2.2444 14.218 2.84339C15.7503 3.41394 17.3995 3.95258 18.7539 4.21385C19.1364 6.07177 19.1709 8.77722 18.139 11.4409C17.0303 14.3032 14.6668 17.1844 9.99999 18.9354C5.3332 17.1844 2.96968 14.3032 1.86094 11.4409Z"></path><path xmlns="http://www.w3.org/2000/svg" class="jp-icon2" fill="#333333" stroke="#333333" transform="translate(8 9.86719)" d="M2.86015 4.86535L0.726549 2.99959L0 3.63045L2.86015 6.13157L8 0.630872L7.27857 0L2.86015 4.86535Z"></path></svg></div></div></div><div class="lm-Widget p-Widget f1ydny4p" title="Notebook is in command mode"><span class="f1235lqo">Mode: Command</span></div></div></div></div></div><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal;"></div></div><div class="lm-Widget p-Widget jp-Completer lm-mod-hidden p-mod-hidden"></div></body></html>