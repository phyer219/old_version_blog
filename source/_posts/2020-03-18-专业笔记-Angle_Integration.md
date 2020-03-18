---
title: 角度积分
date: 2020/03/18
categories: 专业笔记
tags: [积分, 数值计算]
---

<!-- toc -->

<!-- more -->

# 积分

$$
I(\Omega) =
\int_0^{\infty}\mathrm{d}q\int_{-1}^1\mathrm{d}x \cdot\mathrm{Im}\left[ 
    \frac{q^2}{q^2-16qx+2(\Omega+14)+\mathrm{i}0^+}
  \right]
$$

# 解析地积

$$
\begin{align}
I(\Omega) =&\int_0^{\infty}\mathrm{d}q \cdot \frac{q}{16}\mathrm{Im}\left[
   \ln\left(q^2+16q+2(\Omega+14)+\mathrm{i}0^+\right)
  -\ln\left(q^2-16q+2(\Omega+14)+\mathrm{i}0^+\right)
    \right] \\
    =& -\pi \theta(18-\Omega)\sqrt{2(18-\Omega)}
\end{align}
$$

# Supplementary

$$
 \begin{align}I(\Omega) =&\int_0^{\infty}\mathrm{d}q \cdot \frac{q}{16}\mathrm{Im}\left[   \ln\left(q^2+16q+2(\Omega+14)+\mathrm{i}0^+\right)  -\ln\left(q^2-16q+2(\Omega+14)+\mathrm{i}0^+\right)    \right] \\    =& -\pi \theta(18-\Omega)\sqrt{2(18-\Omega)}\end{align}
$$

上式中第二个等号的计算细节.

只有当第一个对数中大于零, 第二个对数中小于零时积分才不为零.

二次函数根的判别式相同, 为
$$
\begin{align}
\Delta = 16^2-8(\Omega + 14)\\
\Delta > 0 \Rightarrow \Omega < 18 \\
\sqrt{\Delta} > 16 \Rightarrow \Omega < 14
\end{align}
$$
第一项的根为
$$
q^{\pm}= \frac{-16 \pm \sqrt{\Delta}}{2}
$$


第二项的根为
$$
q^{\pm}= \frac{16 \pm \sqrt{\Delta}}{2}
$$
积分不为零的条件为
$$
\begin{align}
0<\frac{\sqrt{\Delta}-16}{2}<q<\frac{\sqrt{\Delta}+16}{2},\quad \mathrm{if}\quad \sqrt{\Delta}>14 \\
0<\frac{16-\sqrt{\Delta}}{2}<q<\frac{16+\sqrt{\Delta}}{2},\quad \mathrm{if}\quad \sqrt{\Delta}<14
\end{align}
$$
所以积分结果为
$$
\begin{align}
I(\Omega) =& -\pi\left[ 
\theta(14-\Omega)\left.\frac{q^2}{32}\right|_{q=\frac{\sqrt{\Delta}-16}{2}}^{q=\frac{\sqrt{\Delta}+16}{2}}
+\theta(\Omega-14)\theta(18-\Omega)\left.\frac{q^2}{32}\right|_{q=\frac{16-\sqrt{\Delta}}{2}}^{q =\frac{16+\sqrt{\Delta}}{2}}
\right]\\
=&-\pi \theta(18-\Omega)\frac{\sqrt{\Delta}}{2} \\
=& -\pi \theta(18-\Omega)\sqrt{2(18-\Omega)}
\end{align}
$$
