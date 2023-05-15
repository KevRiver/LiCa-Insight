import { apiInstance } from '@/api';

const api = apiInstance();

function getVisitTrack(params, success, fail) {
  api.get(`/visit/track`, { params: params }).then(success).catch(fail);
}

function getVisitDaily(params, success, fail) {
  api
    .get(`/visit/daily-visitor-statistics`, { params: params })
    .then(success)
    .catch(fail);
}

export { getVisitTrack, getVisitDaily };
