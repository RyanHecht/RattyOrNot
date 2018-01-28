/**
 *
 * Example route for API
 *
 */

import { Router } from 'express';

const router = Router();

router.route('/info').get(getInfo);

function getInfo(req, res) {
  res.status(200).json({
    message: 'GET INFO'
  });
}

function getEateries(req, res) {

}

function getItems(req, res) {

}

function getMenu(req, res) {

}

function getWhen(req, res) {

}

export default router;
