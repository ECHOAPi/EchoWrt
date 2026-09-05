# EchoWrt 迁移说明

2026-09-05 从 `ECHOAPi/EchoWrt-Rockchip` 的 `maintenance/legacy-cleanup` 分支迁入独立仓库 `ECHOAPi/EchoWrt`，默认分支为 `main`。

- 来源提交：[`ab248b7471d0759f324c313e83d176b8adc539f4`](https://github.com/ECHOAPi/EchoWrt-Rockchip/commit/ab248b7471d0759f324c313e83d176b8adc539f4)。
- 来源验证：[仓库回归测试、standard/docker 配置解析及 GN 预检通过](https://github.com/ECHOAPi/EchoWrt-Rockchip/actions/runs/33945744296)。
- 保留：17 台设备配置、现有插件清单及固定来源、管理地址 192.168.8.1、首次登录自行设置密码、构建与发布校验、GPL-3.0 许可证和上游致谢。
- 不导入：旧 Git 历史、旧构建运行和 Artifact、已删除的专用分支、源码下载缓存和固件二进制。
- 简化：发布改用手动输入本仓库构建 ID，移除旧仓库 Build #5 发布请求；构建目录和镜像由 .gitignore 排除，并由仓库检查阻止意外提交大文件。

现有正式固件继续通过[旧仓库 Build #5 Release](https://github.com/ECHOAPi/EchoWrt-Rockchip/releases/tag/2026.08.29-standard-r5)下载，不重复存储到 Git。该版本只有 15 台设备镜像；R2C、R2S 已加入当前配置，需后续编译和实机验证。

原仓库保留作为来源记录和已有固件的下载站。源码中的版权及许可声明继续有效；独立仓库不改变第三方软件的归属与许可证。
